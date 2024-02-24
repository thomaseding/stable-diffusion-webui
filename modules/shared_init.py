import os

import torch

from modules import shared
from modules.shared import cmd_opts


def initialize():
    """Initializes fields inside the shared module in a controlled manner.

    Should be called early because some other modules you can import mingt need these fields to be already set.
    """

    if not cmd_opts.ckpt_dir:
        cmd_opts.ckpt_dir = []
    if not cmd_opts.vae_dir:
        cmd_opts.vae_dir = []

    THOMAS_LYCO_INSTALLED = False  # hack to avoid undefined cmd_opts.lyco_dir access

    if not cmd_opts.embeddings_dir:
        cmd_opts.embeddings_dir = [os.path.join(data_path, 'embeddings')]
    if not cmd_opts.lora_dir:
        cmd_opts.lora_dir = [os.path.join(models_path, 'Lora')]
    if THOMAS_LYCO_INSTALLED and not cmd_opts.lyco_dir:
        cmd_opts.lyco_dir = [os.path.join(models_path, 'LyCORIS')]
    if not cmd_opts.hypernetwork_dir:
        cmd_opts.hypernetwork_dir = [os.path.join(models_path, 'hypernetworks')]

    for dir in cmd_opts.hypernetwork_dir:
        os.makedirs(dir, exist_ok=True)

    from modules import options, shared_options
    shared.options_templates = shared_options.options_templates
    shared.opts = options.Options(shared_options.options_templates, shared_options.restricted_opts)
    shared.restricted_opts = shared_options.restricted_opts
    if os.path.exists(shared.config_filename):
        shared.opts.load(shared.config_filename)

    from modules import devices
    devices.device, devices.device_interrogate, devices.device_gfpgan, devices.device_esrgan, devices.device_codeformer = \
        (devices.cpu if any(y in cmd_opts.use_cpu for y in [x, 'all']) else devices.get_optimal_device() for x in ['sd', 'interrogate', 'gfpgan', 'esrgan', 'codeformer'])

    devices.dtype = torch.float32 if cmd_opts.no_half else torch.float16
    devices.dtype_vae = torch.float32 if cmd_opts.no_half or cmd_opts.no_half_vae else torch.float16

    shared.device = devices.device
    shared.weight_load_location = None if cmd_opts.lowram else "cpu"

    from modules import shared_state
    shared.state = shared_state.State()

    from modules import styles
    shared.prompt_styles = styles.StyleDatabase(shared.styles_filename)

    from modules import interrogate
    shared.interrogator = interrogate.InterrogateModels("interrogate")

    from modules import shared_total_tqdm
    shared.total_tqdm = shared_total_tqdm.TotalTQDM()

    from modules import memmon, devices
    shared.mem_mon = memmon.MemUsageMonitor("MemMon", devices.device, shared.opts)
    shared.mem_mon.start()

