# -*- coding: utf-8 -*-
"""
http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import time
from guitool_ibeis.__PYQT__ import QtCore, QtWidgets
from guitool_ibeis import __PYQT__
if __PYQT__.GUITOOL_PYQT_VERSION == 5:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
elif __PYQT__.GUITOOL_PYQT_VERSION == 4:
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
else:
    raise NotImplementedError
from matplotlib.figure import Figure
#from matplotlib.backends import qt_compat


BASE = FigureCanvas


class QtAbstractMplInteraction(BASE):
    """
    Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.).

    Args:
        self (?):
        parent (None): (default = None)
        width (int): (default = 5)
        height (int): (default = 4)
        dpi (int): (default = 100)

    CommandLine:
        python -m guitool_ibeis.mpl_embed QtAbstractMplInteraction --show

    Example:
        >>> # DISABLE_DOCTEST
        >>> # xdoctest: +REQUIRES(env:DISPLAY)
        >>> from guitool_ibeis.mpl_embed import *  # NOQA
        >>> import plottool_ibeis as pt
        >>> import guitool_ibeis
        >>> guitool_ibeis.ensure_qapp()  # must be ensured before any embeding
        >>> self = QtAbstractMplInteraction()
        >>> parent = None
        >>> width = 5
        >>> height = 4
        >>> dpi = 100
        >>> self = QtAbstractMplInteraction(parent)
        >>> self.show()
        >>> print('Blocking')
        >>> self.start_blocking()
        >>> print('Done')
        >>> # xdoctest: +REQUIRES(--show)
        >>> #import utool as ut
        >>> #ut.quit_if_noshow()
        >>> #import plottool_ibeis as pt
        >>> #ut.show_if_requested()
        >>> guitool_ibeis.qtapp_loop(self, frequency=100, init_signals=True)

    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self._running = None
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        has_hold = False
        try:
            import matplotlib as mpl
            from distutils.version import LooseVersion
            has_hold = LooseVersion(mpl.__version__) < '3.0.0'
        except Exception:
            pass

        if has_hold:
            self.axes.hold(False)

        self.compute_initial_figure()
        #
        BASE.__init__(self, fig)
        self.setParent(parent)

        BASE.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Expanding)
        BASE.updateGeometry(self)
        self.fig = fig

    def compute_initial_figure(self):
        pass

    def closeEvent(self, event):
        self.stop_blocking()
        event.accept()
        #BASE.closeEvent(self, event)

    @QtCore.pyqtSlot()
    def start_blocking(self):
        #self.buttonStart.setDisabled(True)
        self._running = True
        while self._running:
            QtWidgets.qApp.processEvents()
            time.sleep(0.05)
        #self.buttonStart.setDisabled(False)

    @QtCore.pyqtSlot()
    def stop_blocking(self):
        self._running = False


if __name__ == '__main__':
    r"""
    CommandLine:
        python -m guitool_ibeis.mpl_embed
        python -m guitool_ibeis.mpl_embed --allexamples
    """
    import xdoctest
    xdoctest.doctest_module(__file__)
