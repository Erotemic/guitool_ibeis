#!/bin/bash

#docker run -it python3 bash

IMAGE_NAME=python:3.9
docker run -v "$PWD":/io:ro -v "$HOME"/.cache/pip:/pip_cache -it $IMAGE_NAME bash


# Will need to chmod things afterwords
export PIP_CACHE_DIR=/pip_cache
echo "$PIP_CACHE_DIR"
chmod -R o+rw "$PIP_CACHE_DIR"
chmod -R o+rw "$PIP_CACHE_DIR"
chmod -R g+rw "$PIP_CACHE_DIR"
USER=$(whoami)
chown -R "$USER" "$PIP_CACHE_DIR"
cd "$HOME"
git clone /io ./repo

cd "$HOME"/repo

# Make a virtualenv
# shellcheck disable=SC2155
export PYVER=$(python -c "import sys; print('{}{}'.format(*sys.version_info[0:2]))")
pip install virtualenv
virtualenv "venv$PYVER"
source "venv${PYVER}/bin/activate"
#pip install pip -U
#pip install pip setuptools -U

# STRICT VARIANT
#pip install -e .[runtime-strict,headless-strict]
#./run_tests.py


apt update -y
apt install mlocate
apt install libgl1-mesa-glx -y


#apt-get install xvfb
#~/code/kwplot/kwplot/auto_backends.py


pip install pip -U
pip install pygments

# LOOSE VARIANT
#pip install -r requirements.txt
pip install -e .[tests,headless]


#apt-get install -y libxkbcommon-dev

apt install libxcb-xinerama0 
apt install libxcb-icccm4
apt install libxcb-image0
apt install libxcb-keysyms1
apt install libxcb-render-util0
apt install libxcb-shape0
apt install libxcb-xkb1
apt install libxkbcommon-x11-0
apt install libdbus-1-3

#libxkbcommon0
#libxcb-shape0
#libxcb-xkb1
#libxkbcommon-x110
#libxkbcommon0


ldd /root/repo/venv39/lib/python3.9/site-packages/PyQt5/Qt5/plugins/platforms/libqxcb.so
ldd /root/repo/venv39/lib/python3.9/site-packages/PyQt5/Qt5/plugins/platforms/libqxcb| grep "not found"

export QT_DEBUG_PLUGINS=1
xdoctest guitool_ibeis


./run_tests.py
