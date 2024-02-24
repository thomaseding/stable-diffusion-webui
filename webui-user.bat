@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS= ^
  --no-download-sd-model^
  ^
  --data-dir=E:/models/a1111-user-data^
  ^
  --ckpt-dir=E:/models/Stable-diffusion^
  --ckpt-dir=E:/civitai/v1.5/checkpoint^
  --ckpt-dir=E:/civitai/sdxl/checkpoint^
  ^
  --vae-dir=E:/civitai/v1.5/vae^
  ^
  --hypernetwork-dir=E:/models/hypernetworks^
  --hypernetwork-dir=E:/civitai/v1.5/hypernetwork^
  ^
  --lora-dir=E:/models/lora^
  --lora-dir=E:/civitai/v1.5/lora^
  --lora-dir=E:/civitai/sdxl/lora^
  ^
  --lyco-dir=E:/models/lycoris^
  --lyco-dir=E:/civitai/v1.5/lycoris^
  --lyco-dir=E:/civitai/sdxl/lycoris^
  ^
  --embeddings-dir=E:/models/textual-inversion^
  --embeddings-dir=E:/civitai/v1.5/textual-inversion^
  --embeddings-dir=E:/civitai/sdxl/textual-inversion^
  ^
  --textual-inversion-templates-dir=E:/models/ti-templates^
  ^
  --xformers^
  --port=7860^
  ^
  %*

call webui.bat
