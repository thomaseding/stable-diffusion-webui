@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS= ^
  --no-download-sd-model^
  --data-dir=E:/models/a1111-user-data^
  --ckpt-dir=E:/models/Stable-diffusion^
  --hypernetwork-dir=E:/models/hypernetworks^
  --lora-dir=E:/models/Lora^
  --embeddings-dir=E:/models/embeddings^
  --textual-inversion-templates-dir=E:/models/ti-templates^
  --xformers^
  --port=7860

call webui.bat
