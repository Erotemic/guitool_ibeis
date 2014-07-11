from __future__ import absolute_import, division, print_function
from PyQt4 import QtGui, QtCore  # NOQA
from PyQt4.QtCore import Qt
import utool

#BASE_CLASS = QtGui.QAbstractProxyModel
BASE_CLASS = QtGui.QSortFilterProxyModel
# BASE_CLASS = QtGui.QIdentityProxyModel


class FilterProxyModel(BASE_CLASS):
    __metaclass__ = utool.makeForwardingMetaclass(
        lambda self: self.sourceModel(),
        ['_set_context_id', '_get_context_id', '_set_changeblocked',
         '_get_changeblocked', '_about_to_change', '_change', '_update',
         '_rows_updated', 'name', 'get_header_name'],
        base_class=BASE_CLASS)

    def __init__(self, parent=None):
        assert parent is not None, "Must specify parent of filterProxyModel"
        BASE_CLASS.__init__(self, parent=parent)
        self.filter_dict = {}

    def proxy_to_source(self, row, col, parent=QtCore.QModelIndex()):
        r2, c2, p2 = row, col, parent
        return r2, c2, p2

    def source_to_proxy(self, row, col, parent=QtCore.QModelIndex()):
        r2, c2, p2 = row, col, parent
        return r2, c2, p2

    def filterAcceptsRow(self, source_row, source_parent):
        source = self.sourceModel()
        source_index = source.index(source_row, 2, parent=source_parent)
        row_type = str(source.data(source_index))
        #print('%r \'%r\'' % (source_row, row_type))
        #print(self.filter_dict)
        #print(self.filter_dict)
        rv = self.filter_dict.get(row_type, True)
        #print('return value %r' % rv)
        return rv

    def data(self, proxyIndex, role=Qt.DisplayRole):
        sourceIndex = self.mapToSource(proxyIndex)
        return self.sourceModel().data(sourceIndex, role)

    def setData(self, proxyIndex, value, role=Qt.EditRole):
        sourceIndex = self.mapToSource(proxyIndex)
        return self.sourceModel().setData(sourceIndex, value, role)

    def sort(self, column, order):
        self.sourceModel().sort(column, order)

    def get_header_data(self, colname, proxyIndex):
        if proxyIndex is None:
            return None
        elif proxyIndex.isValid():
            sourceIndex = self.mapToSource(proxyIndex)
            ret = self.sourceModel().get_header_data(colname, sourceIndex)
            return ret

    def update_filterdict(self, new_dict):
        self.filter_dict = new_dict

    def _update_rows(self):
        return self.sourceModel()._update_rows()

    def _get_row_id(self, proxyIndex):
        return self.sourceModel()._get_row_id(self.mapToSource(proxyIndex))
