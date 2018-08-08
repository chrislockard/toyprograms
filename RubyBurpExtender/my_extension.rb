=begin 

Include instructions with extension:
  0. Start burp/extension
  1. Spider site as Admin user
  2. Activate extension to repeat all requests taken as admin user
Add function for replaying admin spider session as unprivileged user

=end
require 'java'
java_import 'burp.IBurpExtender'
java_import 'burp.ITab'
java_import 'burp.IHttpListener'
java_import 'burp.IMessageEditorController'
java_import 'burp.IProxyListener'
java_import 'burp.IExtensionStateListener'

class BurpExtender
  include IBurpExtender, ITab, IHttpListener, IMessageEditorController, IProxyListener, IExtensionStateListener

  #
  # Implement IBurpExtender
  #
  def registerExtenderCallbacks(callbacks)
    
    # Keep a reference to this callback object
    @callbacks = callbacks

    # Obtain an extension to the helpers object
    @helpers = callbacks.getHelpers()

    # Set Extension Name
    callbacks.setExtensionName("Admin Replay")

    # Obtain output stream
    @stdout = java.io.PrintWriter.new(callbacks.getStdout(), true)

    # create log
    @log = java.util.ArrayList.new()
    @mutex = Mutex.new()
    
    # Create split pane
    @splitpane = javax.swing.JSplitPane.new(0)

    # Create text entry box for entering admin username
    @adminenter = javax.swing.JTextField.new(0)

    # Table of log entries
    @tableModel = LogTableModel.new(self, @log)
    logTable = Table.new(self, @tableModel)
    scrollPane = javax.swing.JScrollPane.new(logTable)
    @splitpane.setLeftComponent(scrollPane)  

    # Tabs with request/reqsponse viewers
    tabs = javax.swing.JTabbedPane.new()
    @requestViewer = callbacks.createMessageEditor(self, false)
    @responseViewer = callbacks.createMessageEditor(self, false)
    tabs.addTab("Request", @requestViewer.getComponent())
    tabs.addTab("Response", @responseViewer.getComponent())
    @splitpane.setRightComponent(tabs)

    # Customize UI Elements
    callbacks.customizeUiComponent(@splitpane)
    callbacks.customizeUiComponent(@adminenter)
    callbacks.customizeUiComponent(logTable)
    callbacks.customizeUiComponent(scrollPane)
    callbacks.customizeUiComponent(tabs)

    # Add custom tab to Burp's UI
    callbacks.addSuiteTab(self)

    # Register Listeners
    callbacks.registerHttpListener(self)
    callbacks.registerProxyListener(self)
    callbacks.registerExtensionStateListener(self)

  end

  def getTabCaption()
    return "Admin Replay"
  end

  def getUiComponent()
    return @splitpane
  end

  # Implement IHttpListener
  # This function captures all request/responses generated from all BurpSuite tools
  def processHttpMessage(toolFlag, messageIsRequest, messageInfo)
    
    # Process requests
    #if (!messageIsRequest)

    # Process POST requests
    if (@helpers.analyzeRequest(messageInfo).getMethod() == "POST")
      # Create log entry
      @mutex.synchronize do
        row = @log.size()
        @log.add(LogEntry.new(toolFlag, @callbacks.saveBuffersToTempFiles(messageInfo), @helpers.analyzeRequest(messageInfo).getUrl()))
        @tableModel.fireTableRowsInserted(row, row)
      end
    end
  
    # Is the request a POST? If so, log to stdOut
    if (@helpers.analyzeRequest(messageInfo).getMethod() == "POST")
      @stdout.println("POST: " + @helpers.analyzeRequest(messageInfo).getUrl().toString())
    end
    # Print to stdout
    #@stdout.println(
    #        (messageIsRequest ? "HTTP request to " : "HTTP response from ") +
    #        messageInfo.getHttpService().toString() + " [" + @callbacks.getToolName(toolFlag) + "]")
  end
  
  # Implement IProxyListener
  def processProxyMessage(messageIsRequest, message)
    @stdout.println(
            (messageIsRequest ? "Proxy request to " : "Proxy response from ") +
            message.getMessageInfo().getHttpService().toString())
  end

  # Implement IExtensionStateListener
  def extensionUnloaded()
    @stdout.println("Extension was unloaded successfully")
  end

  # Implement IMessageEditorController
  def getHttpService()
    return @currentlyDisplayedItem.getHttpService()
  end

  def getRequest()
    return @currentlyDisplayedItem.getRequest()
  end

  def getResponse()
    return @currentlyDisplayedItem.getResponse()
  end

  # Getters/Setters
  def callbacks
    @callbacks
  end

  def log
    @log
  end

  def requestViewer
    @requestViewer
  end

  def responseViewer
    @responseViewer
  end

  def currentlyDisplayedItem=(currentlyDisplayedItem)
    @currentlyDisplayedItem = currentlyDisplayedItem
  end

end

#
# Extend Java DefaultTableModel
#
class LogTableModel < javax.swing.table.DefaultTableModel
  
  def initialize(extender, log)
    super 0, 0
    @extender = extender
    @log = log
  end

  def getRowCount()
    begin
      return @log.size()
    rescue
      return 0
    end
  end

  def getColumnCount()
    return 2
  end

  def getColumnName(columnIndex)
    if (columnIndex == 0)
      return "Tool"
    end
    if (columnIndex == 1)
      return "URL"
    end
    return ""
  end

  def getValueAt(rowIndex, columnIndex)
    logEntry = @log.get(rowIndex)
    if (columnIndex == 0)
      return @extender.callbacks.getToolName(logEntry.tool)
    end
    if (columnIndex == 1)
      return logEntry.url.toString()
    end
    return ""
  end

end

#
# Extend Java Table Model
#
class Table < javax.swing.JTable

  def initialize(extender, tableModel)
    super tableModel
    @extender = extender
  end

  def changeSelection(row, col, toggle, extend)

    # Show the log entry for the selected row
    logEntry = @extender.log.get(row)
    @extender.requestViewer.setMessage(logEntry.requestResponse.getRequest(), true)
    @extender.responseViewer.setMessage(logEntry.requestResponse.getResponse(), false)
    @extender.currentlyDisplayedItem = logEntry.requestResponse

    super(row, col, toggle, extend)
  end

end

class LogEntry

  def initialize(tool, requestResponse, url)
    @tool = tool
    @requestResponse = requestResponse
    @url = url
  end

  #
  # getters/setters
  #
  def tool
    @tool
  end

  def requestResponse
    @requestResponse
  end

  def url
    @url
  end

end

