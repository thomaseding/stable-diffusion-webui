@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS= --no-download-sd-model --port=7860 --xformers

call webui.bat
