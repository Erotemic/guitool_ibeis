import ast
from pathlib import Path


ROOT = Path(__file__).parents[1]
PACKAGE = ROOT / 'guitool_ibeis'


def _tree(path):
    return ast.parse(path.read_text(), filename=str(path))


def _active_noinject_sites():
    sites = []
    for path in PACKAGE.rglob('*.py'):
        tree = _tree(path)
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == 'noinject'
            ):
                sites.append(path.relative_to(ROOT).as_posix())
    return sorted(sites)


def _imports_utool(path):
    for node in ast.walk(_tree(path)):
        if isinstance(node, ast.Import):
            if any(alias.name == 'utool' for alias in node.names):
                return True
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module == 'utool' or node.module.startswith('utool.'):
                return True
    return False


def test_noinject_is_limited_to_gui_log_bridge_holdout():
    # guitool_misc is kept unchanged because the current Loguru sink adapter
    # was just refactored there; avoid mixing that behavioral surface into this
    # bookkeeping-only cleanup.
    assert set(_active_noinject_sites()) <= {'guitool_ibeis/guitool_misc.py'}


def test_pyqt_shims_and_simple_delegates_are_utool_free():
    relpaths = [
        'guitool_ibeis/__PYQT__/QtCore.py',
        'guitool_ibeis/__PYQT__/QtGui.py',
        'guitool_ibeis/__PYQT__/QtTest.py',
        'guitool_ibeis/__PYQT__/QtWidgets.py',
        'guitool_ibeis/__PYQT__/__init__.py',
        'guitool_ibeis/__PYQT__/_internal.py',
        'guitool_ibeis/api_timestamp_delegate.py',
        'guitool_ibeis/guitool_delegates.py',
    ]
    assert not [rel for rel in relpaths if _imports_utool(ROOT / rel)]


def test_strict_locks_use_a_windows_compatible_qt_runtime():
    lock_relpaths = [
        'requirements/locks/tests-headless.txt',
        'requirements/locks/tests-optional-headless.txt',
    ]
    for relpath in lock_relpaths:
        text = (ROOT / relpath).read_text()
        qt_lines = [
            line for line in text.splitlines()
            if line.startswith('pyqt5-qt5==')
        ]
        assert any(
            line.startswith('pyqt5-qt5==5.15.2 ;')
            and "sys_platform == 'win32'" in line
            for line in qt_lines
        ), relpath
        assert all(
            "sys_platform != 'win32'" in line
            for line in qt_lines
            if not line.startswith('pyqt5-qt5==5.15.2 ;')
        ), relpath
