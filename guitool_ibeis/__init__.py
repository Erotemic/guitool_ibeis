# flake8: noqa
from __future__ import absolute_import, division, print_function

__version__ = '2.0.0'

import utool as ut
ut.noinject(__name__, '[guitool_ibeis.__init__]')


#try:
#    # try seeing if importing plottool before any guitool_ibeis things helps
#    import plottool
#except Exception as ex:
#    import utool as ut
#    ut.printex(ex, 'tried to import plottool to solve win crash')
#    raise
#    #pass

#print('__guitool__1')
from guitool_ibeis import __PYQT__
#print('__guitool__2')

from guitool_ibeis import api_item_model
from guitool_ibeis import api_table_view
from guitool_ibeis import api_tree_view
from guitool_ibeis import api_item_widget
from guitool_ibeis import stripe_proxy_model

from guitool_ibeis import guitool_tables
from guitool_ibeis import guitool_dialogs
from guitool_ibeis import guitool_decorators
from guitool_ibeis import guitool_delegates
from guitool_ibeis import guitool_components
from guitool_ibeis import guitool_main
from guitool_ibeis import guitool_misc
from guitool_ibeis import qtype

import utool

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
__DYNAMIC__ = not ut.get_argflag('--nodyn')
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
from guitool_ibeis.guitool_tables import *
from guitool_ibeis.guitool_dialogs import *
from guitool_ibeis.guitool_decorators import *
from guitool_ibeis.guitool_delegates import *
from guitool_ibeis.guitool_components import *
from guitool_ibeis.guitool_main import *
from guitool_ibeis.guitool_misc import *
from guitool_ibeis.api_item_model import *
from guitool_ibeis.api_table_view import *
from guitool_ibeis.api_tree_view import *
from guitool_ibeis.api_item_widget import *
from guitool_ibeis.stripe_proxy_model import *
from guitool_ibeis.filter_proxy_model import *
from guitool_ibeis.qtype import *

if DOELSE:
    pass
    # <AUTOGEN_INIT>

    from guitool_ibeis import guitool_main
    from guitool_ibeis import guitool_components
    from guitool_ibeis import guitool_dialogs
    from guitool_ibeis import guitool_decorators
    from guitool_ibeis import guitool_misc
    from guitool_ibeis import api_item_model
    from guitool_ibeis import api_tree_view
    from guitool_ibeis import api_table_view
    from guitool_ibeis import qtype
    from guitool_ibeis import stripe_proxy_model
    from guitool_ibeis import filter_proxy_model
    from guitool_ibeis.guitool_main import (GUITOOL_PYQT_VERSION, GuitoolApplication,
                                      IS_ROOT_WINDOW, QAPP, QUIET, VERBOSE,
                                      activate_qwindow, ensure_qapp,
                                      ensure_qtapp, exit_application,
                                      get_qtapp, ping_python_interpreter,
                                      qtapp_loop, qtapp_loop_nonblocking,
                                      remove_pyqt_input_hook,)
    from guitool_ibeis.guitool_components import (ALIGN_DICT, BlockSignals,
                                            ConfigConfirmWidget, DEBUG_WIDGET,
                                            GuiProgContext, GuitoolWidget,
                                            PROG_TEXT, ProgHook,
                                            ResizableTextEdit, SimpleTree,
                                            Spoiler, WIDGET_BASE, adjust_font,
                                            fix_child_attr_heirarchy,
                                            fix_child_size_heirarchy,
                                            getAvailableFonts, get_nested_attr,
                                            get_widget_text_width,
                                            layoutSplitter, make_style_sheet,
                                            msg_event, newButton, newCheckBox,
                                            newComboBox, newFont, newFrame,
                                            newLabel, newLineEdit, newMenu,
                                            newMenuAction, newMenubar,
                                            newOutputLog, newProgressBar,
                                            newQPoint, newScrollArea,
                                            newSizePolicy, newSplitter,
                                            newTabWidget, newTextEdit,
                                            newToolbar, newWidget,
                                            print_widget_heirarchy,
                                            prop_text_map, rectify_qt_const,
                                            walk_widget_heirarchy,)
    from guitool_ibeis.guitool_dialogs import (ResizableMessageBox, SELDIR_CACHEID,
                                         are_you_sure, build_nested_qmenu,
                                         connect_context_menu, msgbox,
                                         newDirectoryDialog, newFileDialog,
                                         popup_menu, select_directory,
                                         select_files, select_images,
                                         user_info, user_input, user_option,
                                         user_question,)
    from guitool_ibeis.guitool_decorators import (DEBUG, checks_qt_error, signal_,
                                            slot_,)
    from guitool_ibeis.guitool_misc import (ALT_KEY, BlockContext, GUILoggingHandler,
                                      GUILoggingSender, QLoggedOutput,
                                      find_used_chars, get_cplat_tab_height,
                                      get_view_selection_as_str,
                                      make_option_dict, make_word_hotlinks,)
    from guitool_ibeis.api_item_model import (APIItemModel, API_MODEL_BASE,
                                        ChangeLayoutContext, QVariantHack,
                                        VERBOSE_MODEL,
                                        default_method_decorator,
                                        simple_thumbnail_widget, updater,)
    from guitool_ibeis.api_tree_view import (APITreeView, API_VIEW_BASE,
                                       testdata_tree_view,)
    from guitool_ibeis.api_table_view import (APITableView,)
    from guitool_ibeis.qtype import (ItemDataRoles, LOCALE, QLocale, QString,
                               QT_BUTTON_TYPES, QT_COMBO_TYPES,
                               QT_DELEGATE_TYPES, QT_ICON_TYPES,
                               QT_IMAGE_TYPES, QT_PIXMAP_TYPES, QVariant,
                               SIMPLE_CASTING, cast_from_qt, cast_into_qt,
                               infer_coltype, locale_float, numpy_to_qicon,
                               numpy_to_qpixmap, qindexinfo, to_qcolor,)
    from guitool_ibeis.stripe_proxy_model import (STRIPE_PROXY_BASE,
                                            STRIP_PROXY_META_CLASS,
                                            STRIP_PROXY_SIX_BASE,
                                            StripeProxyModel,)
    from guitool_ibeis.filter_proxy_model import (BASE_CLASS, FilterProxyModel,)
    import utool
    print, rrr, profile = utool.inject2(__name__, '[guitool_ibeis]')


    def reassign_submodule_attributes(verbose=1):
        """
        Updates attributes in the __init__ modules with updated attributes
        in the submodules.
        """
        import sys
        if verbose and '--quiet' not in sys.argv:
            print('dev reimport')
        # Self import
        import guitool_ibeis
        # Implicit reassignment.
        seen_ = set([])
        for tup in IMPORT_TUPLES:
            if len(tup) > 2 and tup[2]:
                continue  # dont import package names
            submodname, fromimports = tup[0:2]
            submod = getattr(guitool_ibeis, submodname)
            for attr in dir(submod):
                if attr.startswith('_'):
                    continue
                if attr in seen_:
                    # This just holds off bad behavior
                    # but it does mimic normal util_import behavior
                    # which is good
                    continue
                seen_.add(attr)
                setattr(guitool_ibeis, attr, getattr(submod, attr))


    def reload_subs(verbose=1):
        """ Reloads guitool_ibeis and submodules """
        if verbose:
            print('Reloading guitool_ibeis submodules')
        rrr(verbose > 1)
        def wrap_fbrrr(mod):
            def fbrrr(*args, **kwargs):
                """ fallback reload """
                if verbose > 0:
                    print('Auto-reload (using rrr) not setup for mod=%r' % (mod,))
            return fbrrr
        def get_rrr(mod):
            if hasattr(mod, 'rrr'):
                return mod.rrr
            else:
                return wrap_fbrrr(mod)
        def get_reload_subs(mod):
            return getattr(mod, 'reload_subs', wrap_fbrrr(mod))
        get_rrr(guitool_main)(verbose > 1)
        get_rrr(guitool_components)(verbose > 1)
        get_rrr(guitool_dialogs)(verbose > 1)
        get_rrr(guitool_decorators)(verbose > 1)
        get_rrr(guitool_misc)(verbose > 1)
        get_rrr(api_item_model)(verbose > 1)
        get_rrr(api_tree_view)(verbose > 1)
        get_rrr(api_table_view)(verbose > 1)
        get_rrr(qtype)(verbose > 1)
        get_rrr(stripe_proxy_model)(verbose > 1)
        get_rrr(filter_proxy_model)(verbose > 1)
        rrr(verbose > 1)
        try:
            # hackish way of propogating up the new reloaded submodule attributes
            reassign_submodule_attributes(verbose=verbose)
        except Exception as ex:
            print(ex)
    rrrr = reload_subs
    # </AUTOGEN_INIT>