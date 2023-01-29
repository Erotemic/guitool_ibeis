__version__ = '2.1.2'

import utool as ut
ut.noinject(__name__, '[guitool_ibeis.__init__]')

from guitool_ibeis import __PYQT__  # NOQA

from guitool_ibeis import api_item_model  # NOQA
from guitool_ibeis import api_table_view  # NOQA
from guitool_ibeis import api_tree_view  # NOQA
from guitool_ibeis import api_item_widget  # NOQA
from guitool_ibeis import stripe_proxy_model  # NOQA

from guitool_ibeis import guitool_tables  # NOQA
from guitool_ibeis import guitool_dialogs  # NOQA
from guitool_ibeis import guitool_decorators  # NOQA
from guitool_ibeis import guitool_delegates  # NOQA
from guitool_ibeis import guitool_components  # NOQA
from guitool_ibeis import guitool_main  # NOQA
from guitool_ibeis import guitool_misc  # NOQA
from guitool_ibeis import qtype  # NOQA

import utool  # NOQA

print, rrr, profile = utool.inject2(__name__, '[guitool_ibeis]')


def reload_subs():
    """Reloads utool and submodules """
    rrr()
    if hasattr(guitool_tables, 'rrr'):
        guitool_tables.rrr()
    if hasattr(guitool_dialogs, 'rrr'):
        guitool_dialogs.rrr()
    if hasattr(guitool_decorators, 'rrr'):
        guitool_decorators.rrr()
    if hasattr(guitool_main, 'rrr'):
        guitool_main.rrr()
    if hasattr(guitool_misc, 'rrr'):
        guitool_misc.rrr()
    if hasattr(api_item_model, 'rrr'):
        api_item_model.rrr()
    if hasattr(qtype, 'rrr'):
        qtype.rrr()
    if hasattr(guitool_components, 'rrr'):
        guitool_components.rrr()

rrrr = reload_subs


IMPORT_TUPLES = [
    ('guitool_main', None),
    ('guitool_components', None),
    ('guitool_dialogs', None),
    ('guitool_decorators', None),
    ('guitool_misc', None),
    ('api_item_model', None),
    ('api_tree_view', None),
    ('api_table_view', None),
    ('qtype', None),
    ('stripe_proxy_model', None),
    ('filter_proxy_model', None),
]
"""
python -c "import guitool_ibeis" --dump-guitool_ibeis-init
python -c "import guitool_ibeis" --update-guitool_ibeis-init
"""
__DYNAMIC__ = True
DOELSE = False
if __DYNAMIC__:
    # TODO: import all utool external prereqs. Then the imports will not import
    # anything that has already in a toplevel namespace
    # COMMENTED OUT FOR FROZEN __INIT__
    # Dynamically import listed util libraries and their members.
    from utool._internal import util_importer
    # FIXME: this might actually work with rrrr, but things arent being
    # reimported because they are already in the modules list
    ignore_endswith = ['_cyth']
    ignore_list = ['Qt']
    import_execstr = util_importer.dynamic_import(__name__, IMPORT_TUPLES,
                                                  ignore_endswith=ignore_endswith,
                                                  ignore_list=ignore_list,
                                                  verbose=False)
    exec(import_execstr)
    DOELSE = False
else:
    # Do the nonexec import (can force it to happen no matter what if alwyas set
    # to True)
    DOELSE = True

# This screws up dynamic_import if it is placed before
from guitool_ibeis.guitool_tables import *  # NOQA
from guitool_ibeis.guitool_dialogs import *  # NOQA
from guitool_ibeis.guitool_decorators import *  # NOQA
from guitool_ibeis.guitool_delegates import *  # NOQA
from guitool_ibeis.guitool_components import *  # NOQA
from guitool_ibeis.guitool_main import *  # NOQA
from guitool_ibeis.guitool_misc import *  # NOQA
from guitool_ibeis.api_item_model import *  # NOQA
from guitool_ibeis.api_table_view import *  # NOQA
from guitool_ibeis.api_tree_view import *  # NOQA
from guitool_ibeis.api_item_widget import *  # NOQA
from guitool_ibeis.stripe_proxy_model import *  # NOQA
from guitool_ibeis.filter_proxy_model import *  # NOQA
from guitool_ibeis.qtype import *  # NOQA
