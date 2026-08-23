# -*- coding: utf-8 -*-
# flake8:noqa
# Wrapper around PyQt4/5
from __future__ import absolute_import, division, print_function
from . import _internal

if _internal.GUITOOL_PYQT_VERSION == 4:
     # just a clone of QtGui in PyQt4
    from PyQt4.QtGui import *
else:
    from PyQt5.QtWidgets import *
