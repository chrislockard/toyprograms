from burp import IBurpExtender
from burp import IContextMenuFactory
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IMessageEditorController
from burp import ITab
from java.awt import Color
from java.awt import Dimension
from java.awt import Font
from java.awt import Toolkit
from java.awt.datatransfer import Clipboard
from java.awt.datatransfer import StringSelection
from java.awt.event import ActionListener
from java.awt.event import AdjustmentListener
from java.awt.event import ItemListener
from java.awt.event import MouseAdapter
from java.io import File
from java.lang import Integer
from java.lang import Math
from java.lang import String
from java.net import URL
from java.util import ArrayList
from java.util import LinkedList
from javax.swing import DefaultListModel
from javax.swing import JButton
from javax.swing import JCheckBox
from javax.swing import JCheckBoxMenuItem
from javax.swing import JComboBox
from javax.swing import JFileChooser
from javax.swing import JFrame
from javax.swing import JLabel
from javax.swing import JList
from javax.swing import JMenuItem
from javax.swing import JPanel
from javax.swing import JPopupMenu
from javax.swing import JScrollPane
from javax.swing import JScrollPane
from javax.swing import JSplitPane
from javax.swing import JTabbedPane
from javax.swing import JTable
from javax.swing import JTextArea
from javax.swing import RowFilter
from javax.swing.border import LineBorder
from javax.swing.table import AbstractTableModel
from javax.swing.table import TableRowSorter
from thread import start_new_thread
from threading import Lock
import base64
import csv
import re
import sys


class BurpExtender(IBurpExtender, ITab, IHttpListener, IMessageEditorController, AbstractTableModel, IContextMenuFactory):

    #
    # implement IBurpExtender
    #

    def registerExtenderCallbacks(self, callbacks):
        # PDB debugging: connect sys.stdout and sys.stderr to Burp
        # sys.stdout = callbacks.getStdout()
        # sys.stderr = callbacks.getStderr()
        
        # keep a reference to our callbacks object
        self._callbacks = callbacks

        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()

        # set extension name
        callbacks.setExtensionName("To Do")

        # create the log and a lock on which to synchronize when adding
        # log entries
        self._log = ArrayList()
        self._lock = Lock()

        # main split pane
        self._splitpane = JSplitPane(JSplitPane.HORIZONTAL_SPLIT)

        # Configuration Tab
        self.initConfigTab()

        # table of to do entries
        logTable = Table(self)
        scrollPane = JScrollPane(logTable)
        self._splitpane.setLeftComponent(scrollPane)

        # Config tab
        self.tabs = JTabbedPane()
        self._configuration = self._callbacks.createMessageEditor(self, False)
        self.tabs.addTab("Configuration", self._configuration.getComponent())
        self._splitpane.setRightComponent(self.panel)

        # customize our UI components
        callbacks.customizeUiComponent(self._splitpane)
        callbacks.customizeUiComponent(logTable)
        callbacks.customizeUiComponent(scrollPane)

        # add the custom tab to Burp's UI
        callbacks.addSuiteTab(self)

        # register ourselves as an HTTP listener
        callbacks.registerHttpListener(self)

        # initialize tabs
        self.initTabs()

        # Print thank you, contact info, etc
        print("Thank you for installing Burp To Do List")
        print("created by Chris Lockard")
        print("https://github.com/chrislockard/BurpToDoList")
        return

    #
    # implement ITab
    #

    def getTabCaption(self):
        return "To Do"

    def getUiComponent(self):
        return self._splitpane

    def initConfigTab(self):
        # Init configuration tab
        self.test = JLabel("Configuration")
        self.test.setBounds(10,10,140,30)

        self.panel = JPanel()
        self.panel.setBounds(0,0,1000,1000)
        self.panel.setLayout(None)
        self.panel.add(self.test)

    def initTabs(self):
        # Init ToDo List Tabs
        self.logTable = Table(self)

        tableWidth = self.logTable.getPreferredSize().width
        self.logTable.getColumn("Complete?").setPreferredWidth(Math.round(tableWidth / 10 * 1))
        self.logTable.getColumn("Section").setPreferredWidth(Math.round(tableWidth / 10 * 3))
        self.logTable.getColumn("Task").setPreferredWidth(Math.round(tableWidth / 10 * 3))
        self.logTable.getColumn("Notes").setPreferredWidth(Math.round(tableWidth / 10 * 3))

        self.tableSorter = TableRowSorter(self)
        self.logTable.setRowSorter(self.tableSorter)

        self._splitpane = JSplitPane(JSplitPane.HORIZONTAL_SPLIT)
        self._splitpane.setResizeWeight(1)
        self.scrollPane = JScrollPane(self.logTable)
        self._splitpane.setLeftComponent(self.scrollPane)
        self.scrollPane.getVerticalScrollBar().addAdjustmentListener(autoScrollListener(self))

    def getRowCount(self):
        try:
            return self._log.size()
        except:
            return 0

    def getColumnCount(self):
        return 4

    def getColumnName(self, columnIndex):
        if columnIndex == 0:
            return "Complete?"
        if columnIndex == 1:
            return "Section"
        if columnIndex == 2:
            return "Task"
        if columnIndex == 3:
            return "Notes"
        return ""

    def getColumnClass(self, columnIndex):
        if columnIndex == 0:
            return checkbox
        if columnIndex == 1:
            return String
        if columnIndex == 2:
            return String
        if columnIndex == 3:
            return String
        return ""

    def getValueAt(self, rowIndex, columnIndex):
        logEntry = self._log.get(rowIndex)
        if columnIndex == 0:
            return self._callbacks.getToolName(logEntry._tool)
        if columnIndex == 1:
            return logEntry._url.toString()
        if columnIndex == 2:
            pass
        if columnIndex == 3:
            pass
        return ""

    #
    # implement IMessageEditorController
    # this allows our request/response viewers to obtain details about the
    # messages being displayed
    # def getHttpService(self):
    #    return self._currentlyDisplayedItem.getHttpService()

    # def getRequest(self):
    #    return self._currentlyDisplayedItem.getRequest()

    # def getResponse(self):
    #    return self._currentlyDisplayedItem.getResponse()

#
# extend JTable to handle cell selection
#


class Table(JTable):

    def __init__(self, extender):
        self._extender = extender
        self.setModel(extender)
        self.addMouseListener(mouseclick(self._extender))
        self.getColumnModel().getColumn(0).setPreferredWidth(Math.round(10 / 10 * 1))
        self.getColumnModel().getColumn(1).setPreferredWidth(250)
        self.getColumnModel().getColumn(2).setPreferredWidth(250)
        self.getColumnModel().getColumn(3).setPreferredWidth(250)
        self.setRowSelectionAllowed(True)
        return

    def changeSelection(self, row, col, toggle, extend):

        # show the log entry for the selected row
        logEntry = self._extender._log.get(row)
        self._extender._requestViewer.setMessage(logEntry._requestResponse.getRequest(), True)
        self._extender._responseViewer.setMessage(logEntry._requestResponse.getResponse(), False)
        self._extender._currentlyDisplayedItem = logEntry._requestResponse

        JTable.changeSelection(self, row, col, toggle, extend)
        return

#
# class to hold details of each log entry
#


class LogEntry:

    def __init__(self, tool, requestResponse, url):
        self._tool = tool
        self._requestResponse = requestResponse
        self._url = url
        return


class mouseclick(MouseAdapter):

    def __init__(self, extender):
        self._extender = extender
        # import pdb; pdb.set_trace()

    def mouseReleased(self, evt):
        if evt.button == 3:
            self._extender.menu.show(evt.getComponent(), evt.getX(), evt.getY())


class autoScrollListener(AdjustmentListener):
    def __init__(self, extender):
        self._extender = extender

    def adjustmentValueChanged(self, e):
        if (self._extender.autoScroll.isSelected() is True):
            e.getAdjustable().setValue(e.getAdjustable().getMaximum())
