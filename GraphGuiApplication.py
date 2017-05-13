import webbrowser
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
from GraphGuiClasses import GraphScene
from GraphControlPanelGui import Ui_GraphControlWindow as GraphControlPanel

''' Graph GUI 
  
    Author: Sharif Shaker
    Date: 4/29/2017
    
    Modified: 5/11/2017
    Changes made: Added functionality to change graph type between undirected graph and digraph by pressing a button on the panel.

    Description:
        This file contains various classes and functions for displaying a graphical representation of a graph.  The Graphical layout and 
        design was done using QtDesigner

'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")

        # setup central widget and main graphics area 
        self.MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphView.setObjectName("graphView")

        # using the MainWindow passed into the funtion, add a graph scene 
        self.scene=self.MainWindow.graph_scene
        self.graphView.setScene(self.scene)

        # setup layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.graphView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 40, 0, 20)
        self.verticalLayout.setObjectName("verticalLayout")

        # general label setup
        self.path_status_header = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_status_header.sizePolicy().hasHeightForWidth())
        self.path_status_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.path_status_header.setFont(font)
        self.path_status_header.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.path_status_header.setObjectName("path_status_header")
        self.verticalLayout.addWidget(self.path_status_header)
        self.path_algorithm_header_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_algorithm_header_lab.setFont(font)
        self.path_algorithm_header_lab.setObjectName("path_algorithm_header_lab")
        self.verticalLayout.addWidget(self.path_algorithm_header_lab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        # setup combo box for selecting algorithms to run on graph
        self.select_path_alg_comboBox = SceneConnectedComboBox(self.centralwidget, self.scene) # box requires reference to scene 
        self.select_path_alg_comboBox.setEditable(False)
        self.select_path_alg_comboBox.addItems(['DIJKSTRA','BELLMAN FORD', 'PRIMS']) # algorithms that can be run
        self.select_path_alg_comboBox.setMaxVisibleItems(8)
        self.select_path_alg_comboBox.setObjectName("select_path_alg_comboBox")
        self.select_path_alg_comboBox.setCurrentIndex(0)
        self.verticalLayout.addWidget(self.select_path_alg_comboBox) # add combo box to vertical layout

        # setup for algorithm information grid layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 5, -1, 5)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(55)
        self.gridLayout.setObjectName("gridLayout")
        self.dist_val_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dist_val_lab.setFont(font)
        self.dist_val_lab.setObjectName("dist_val_lab")
        self.gridLayout.addWidget(self.dist_val_lab, 5, 1, 1, 1)
        self.path_shown_yes_no = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.path_shown_yes_no.setFont(font)
        self.path_shown_yes_no.setObjectName("path_shown_yes_no")
        self.gridLayout.addWidget(self.path_shown_yes_no, 1, 1, 1, 1)
        self.path_shown_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_shown_lab.setFont(font)
        self.path_shown_lab.setObjectName("path_shown_lab")
        self.gridLayout.addWidget(self.path_shown_lab, 1, 0, 1, 1)
        self.node1_val_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.node1_val_lab.setFont(font)
        self.node1_val_lab.setObjectName("node1_val_lab")
        self.gridLayout.addWidget(self.node1_val_lab, 2, 1, 1, 1)
        self.node2__val_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.node2__val_lab.setFont(font)
        self.node2__val_lab.setObjectName("node2__val_lab")
        self.gridLayout.addWidget(self.node2__val_lab, 4, 1, 1, 1)
        self.node1_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node1_lab.setFont(font)
        self.node1_lab.setObjectName("node1_lab")
        self.gridLayout.addWidget(self.node1_lab, 2, 0, 1, 1)
        self.path_distance_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_distance_lab.setFont(font)
        self.path_distance_lab.setObjectName("path_distance_lab")
        self.gridLayout.addWidget(self.path_distance_lab, 5, 0, 1, 1)
        self.node2_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node2_lab.setFont(font)
        self.node2_lab.setObjectName("node2_lab")
        self.gridLayout.addWidget(self.node2_lab, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.graph_info_lab = QtWidgets.QLabel(self.centralwidget)
        
        # large label for graph status information
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75) 
        self.graph_info_lab.setFont(font)
        self.graph_info_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.graph_info_lab.setWordWrap(False)
        self.graph_info_lab.setObjectName("graph_info_lab")
        self.verticalLayout.addWidget(self.graph_info_lab)

        # setup internal grid layout for graph status information
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-25, -25, 25, 80)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(55)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.node_count_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node_count_lab.setFont(font)
        self.node_count_lab.setObjectName("node_count_lab")
        self.gridLayout_2.addWidget(self.node_count_lab, 0, 0, 1, 1)
        self.edge_count_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edge_count_lab.setFont(font)
        self.edge_count_lab.setObjectName("edge_count_lab")
        self.gridLayout_2.addWidget(self.edge_count_lab, 1, 0, 1, 1)
        self.num_nodes_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.num_nodes_val.setFont(font)
        self.num_nodes_val.setObjectName("num_nodes_val")
        self.gridLayout_2.addWidget(self.num_nodes_val, 0, 1, 1, 1)
        self.num_edges_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.num_edges_val.setFont(font)
        self.num_edges_val.setObjectName("num_edges_val")
        self.gridLayout_2.addWidget(self.num_edges_val, 1, 1, 1, 1)
        self.graph_status_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.graph_status_lab.setFont(font)
        self.graph_status_lab.setObjectName("graph_status_lab")
        self.gridLayout_2.addWidget(self.graph_status_lab, 2, 0, 1, 1)
        self.graph_status = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_status.sizePolicy().hasHeightForWidth())
        self.graph_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graph_status.setFont(font)
        self.graph_status.setObjectName("graph_status")
        self.gridLayout_2.addWidget(self.graph_status, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        # add button for pulling up control panel
        self.control_panel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.control_panel_btn.setObjectName("control_panel_btn")
        self.verticalLayout.addWidget(self.control_panel_btn)

        # add button for pulling up control panel
        self.switch_graph_btn = QtWidgets.QPushButton(self.centralwidget)
        self.switch_graph_btn.setObjectName("switch_graph_btn")
        self.verticalLayout.addWidget(self.switch_graph_btn)

        # add vertical layout to main horizontal layout
        self.horizontalLayout.addLayout(self.verticalLayout)

        # set as central widget
        self.MainWindow.setCentralWidget(self.centralwidget)

        # help menu setup
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1225, 31))
        self.menubar.setObjectName("menubar")
        helpAction = QtWidgets.QAction('&Open Help', self.MainWindow) # action pulling up a help menu      
        helpAction.setShortcut('Ctrl+H')
        helpAction.setStatusTip('application help')
        helpAction.triggered.connect(lambda: webbrowser.open("GraphGuiHelp.pdf")) # open help file
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.addAction(helpAction)
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(self.MainWindow) # call retranslateUi function
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
  
        self.button_setup()
        

    def button_setup(self):

        # connect edit_path_algorithm to combobox
        self.select_path_alg_comboBox.activated.connect(self.edit_path_algorithm)

        # connect the MainWindows init_control_panel function to button
        self.control_panel_btn.clicked.connect(lambda: self.MainWindow.init_control_pane())

        # connect the MainWindows init_control_panel function to button
        self.switch_graph_btn.clicked.connect(lambda: self.change_graph_type())

        # connect update_data function to signal 
        self.scene.data_updater.signal.connect(self.update_data)

    def change_graph_type(self):
        _translate = QtCore.QCoreApplication.translate
        (nodes, edges) = self.MainWindow.switch_graph_type() # switch graph type and get previously used nodes and edges from old graph
        self.setupUi(self.MainWindow) # reset the UI with the modified MainWindow 
        if self.scene.digraph: # if changed to digraph
            self.switch_graph_btn.setText(_translate("MainWindow", "TO GRAPH")) # button to change to graph
        else: 
            self.switch_graph_btn.setText(_translate("MainWindow", "TO DIGRAPH")) # button to change to digraph
        
        for node_val, node in nodes.items(): # for each node that was in the original graph
            node.selected = False 
            node.highlighted = False # remove higlights or selctions
            self.scene.addItem(node) # add the node to the windows graph scene
            self.scene.nodes[node_val] = node  # add the node to the scene's dictionary
            self.scene.graph.add_node(node_val) # add the node to the scene's underlying graph

        for (from_node, to_node), edge in edges.items(): # for each edge in the original graph
            self.scene.add_edge(from_node, to_node, edge.weight) # add it to the new graph
            if self.scene.digraph: # if changed from graph to digraph
                self.scene.add_edge(to_node, from_node, edge.weight) # add edges in both directions
        
 
    def edit_path_algorithm(self):

        # when algorithm combo box is edited reset the graph scenes current algorithm
        self.scene.current_path_algo = self.select_path_alg_comboBox.currentText()
        
 
     
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
 
        # complete setup of labels and buttons by adding text
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph"))
        self.path_status_header.setText(_translate("MainWindow", "-PATH STATUS-"))
        self.path_algorithm_header_lab.setText(_translate("MainWindow", "Path Algorithm:"))
        self.dist_val_lab.setText(_translate("MainWindow", "N/A"))
        self.path_shown_yes_no.setText(_translate("MainWindow", "NO"))
        self.path_shown_lab.setText(_translate("MainWindow", "Path Shown:"))
        self.node1_val_lab.setText(_translate("MainWindow", "N/A"))
        self.node2__val_lab.setText(_translate("MainWindow", "N/A"))
        self.node1_lab.setText(_translate("MainWindow", "From Node:"))
        self.path_distance_lab.setText(_translate("MainWindow", "Distance:"))
        self.node2_lab.setText(_translate("MainWindow", "To Node:"))
        self.graph_info_lab.setText(_translate("MainWindow", "-GRAPH INFO-"))
        self.node_count_lab.setText(_translate("MainWindow", "Node Count:"))
        self.edge_count_lab.setText(_translate("MainWindow", "Edge  Count:"))
        self.num_nodes_val.setText(_translate("MainWindow", "0"))
        self.num_edges_val.setText(_translate("MainWindow", "0"))
        self.graph_status_lab.setText(_translate("MainWindow", "Connected:"))
        self.graph_status.setText(_translate("MainWindow", "NO"))
        self.control_panel_btn.setText(_translate("MainWindow", "CONTROL PANEL"))
        self.switch_graph_btn.setText(_translate("MainWindow", "TO GRAPH"))
        
            
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

    @QtCore.pyqtSlot()
    def update_data(self):
        # function is called when signel is sent indicating the graph has been updated 
        _translate = QtCore.QCoreApplication.translate

        if self.scene.path_displayed[0]: # if a path is being displayed indicate that it is and fill in relavent data from graph 
            self.path_shown_yes_no.setText(_translate("MainWindow", "YES"))   
            self.node1_val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[1])))
            self.node2__val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[2])))
            self.dist_val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[3])))
        else: # if no path indicate that nothing is shown
            self.path_shown_yes_no.setText(_translate("MainWindow", "NO"))
            self.node1_val_lab.setText(_translate("MainWindow", "N/A"))
            self.node2__val_lab.setText(_translate("MainWindow", "N/A"))
            self.dist_val_lab.setText(_translate("MainWindow", "N/A"))

        # set label to indicate if graph is connected
        if self.scene.graph.is_connected(): self.graph_status.setText(_translate("MainWindow", "YES"))
        else: self.graph_status.setText(_translate("MainWindow", "NO"))

        #show the current number of edges and nodes in graph
        self.num_nodes_val.setText(_translate("MainWindow", str(len(self.scene.nodes))))
        self.num_edges_val.setText(_translate("MainWindow", str(len(self.scene.edges))))

class SceneConnectedComboBox(QtWidgets.QComboBox):

    def __init__(self, widget, graph_scene):
        super().__init__(widget) # initialize a combo box as part of input widget
        self.scene = graph_scene # include a graph scene reference in combobox 

    
    def keyPressEvent(self, event):
        self.scene.keyPressEvent(event) # if the combobox is selected and a key is pressed send event to graph scene
          
         

class MainGraphWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # initialize the main window of the GUI
        super().__init__()

        self.graph_scene = GraphScene(True) # initialize it with a graph scene
        
        self.app = QtWidgets.QApplication([])
        self.screen_resolution = app.desktop().screenGeometry()
        self.width = self.screen_resolution.width()
        self.height = self.screen_resolution.height()  

        self.init_control_pane() # also intitialize with a control panel
        

    def init_control_pane(self):
        self.setGeometry(self.width/4+5, 40, 3*self.width/4, self.height-100) # main window take up 3/4 of the total width of the screen
        self.GraphControlWindow = QtWidgets.QWidget() # create an new control panel window
        ui = GraphControlPanel()
        ui.setupUi(self.GraphControlWindow, self.graph_scene)
        self.GraphControlWindow.setGeometry(0,40,self.width/4,self.height-100) # control panel takes 1/4 of the total width of the screen
        self.GraphControlWindow.show() # display control panel

    def switch_graph_type(self):
        
        edges = self.graph_scene.edges
        nodes = self.graph_scene.nodes
        digraph = not self.graph_scene.digraph
        
        self.graph_scene = GraphScene(digraph)

        self.init_control_pane() # also intitialize with a control panel
        
        return ((nodes, edges)) 
        
                
    def closeEvent(self, event):
        self.GraphControlWindow.close() # when the main window is closed the control panel must also close


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainGraphWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
