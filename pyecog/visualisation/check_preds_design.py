# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_preds_design_v3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.widget)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.setFont(font)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setColumnCount(8)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setKerning(True)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setText(1, "2")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(1, font)
        self.treeWidget.headerItem().setText(2, "3")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(2, font)
        self.treeWidget.headerItem().setText(3, "4")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(3, font)
        self.treeWidget.headerItem().setText(4, "5")
        self.treeWidget.headerItem().setText(5, "6")
        self.treeWidget.headerItem().setText(6, "7")
        self.treeWidget.headerItem().setText(7, "8")
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setMinimumSectionSize(5)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.widget, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tabWidgetPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setBaseSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout.addWidget(self.textBrowser_4)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_5 = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setContentsMargins(5, 44, 5, 5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.tid_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.tid_spinBox.setMaximumSize(QtCore.QSize(51, 16777215))
        self.tid_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tid_spinBox.setObjectName("tid_spinBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tid_spinBox)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.checkbox_hold_trace_position = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkbox_hold_trace_position.setFont(font)
        self.checkbox_hold_trace_position.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkbox_hold_trace_position.setText("")
        self.checkbox_hold_trace_position.setObjectName("checkbox_hold_trace_position")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkbox_hold_trace_position)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.hp_filter_freq = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_filter_freq.sizePolicy().hasHeightForWidth())
        self.hp_filter_freq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hp_filter_freq.setFont(font)
        self.hp_filter_freq.setWrapping(False)
        self.hp_filter_freq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hp_filter_freq.setMaximum(512.0)
        self.hp_filter_freq.setProperty("value", 1.0)
        self.hp_filter_freq.setObjectName("hp_filter_freq")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hp_filter_freq)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lp_filter_freq = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lp_filter_freq.sizePolicy().hasHeightForWidth())
        self.lp_filter_freq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lp_filter_freq.setFont(font)
        self.lp_filter_freq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lp_filter_freq.setMaximum(30000.0)
        self.lp_filter_freq.setProperty("value", 512.0)
        self.lp_filter_freq.setObjectName("lp_filter_freq")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lp_filter_freq)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.checkbox_filter_toggle = QtWidgets.QCheckBox(self.frame)
        self.checkbox_filter_toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkbox_filter_toggle.setAutoFillBackground(True)
        self.checkbox_filter_toggle.setText("")
        self.checkbox_filter_toggle.setTristate(False)
        self.checkbox_filter_toggle.setObjectName("checkbox_filter_toggle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkbox_filter_toggle)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.xrange_spinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.xrange_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.xrange_spinBox.setMaximum(3600.0)
        self.xrange_spinBox.setObjectName("xrange_spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xrange_spinBox)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.scroll_speed_box = QtWidgets.QSpinBox(self.frame_2)
        self.scroll_speed_box.setMinimum(1)
        self.scroll_speed_box.setObjectName("scroll_speed_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.scroll_speed_box)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.checkBox_scrolling = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_scrolling.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_scrolling.setText("")
        self.checkBox_scrolling.setObjectName("checkBox_scrolling")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox_scrolling)
        self.blink_box = QtWidgets.QCheckBox(self.frame_2)
        self.blink_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blink_box.setText("")
        self.blink_box.setObjectName("blink_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.blink_box)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_4.setContentsMargins(5, 5, 5, 5)
        self.formLayout_4.setHorizontalSpacing(5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.predictions_file_display = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictions_file_display.sizePolicy().hasHeightForWidth())
        self.predictions_file_display.setSizePolicy(sizePolicy)
        self.predictions_file_display.setObjectName("predictions_file_display")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.predictions_file_display)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.h5_folder_display = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h5_folder_display.sizePolicy().hasHeightForWidth())
        self.h5_folder_display.setSizePolicy(sizePolicy)
        self.h5_folder_display.setDragEnabled(True)
        self.h5_folder_display.setReadOnly(True)
        self.h5_folder_display.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.h5_folder_display.setObjectName("h5_folder_display")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.h5_folder_display)
        self.horizontalLayout.addWidget(self.frame_3)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.overview_plot = GraphicsLayoutWidget(self.splitter)
        self.overview_plot.setBaseSize(QtCore.QSize(800, 300))
        self.overview_plot.setObjectName("overview_plot")
        self.GraphicsLayoutWidget = GraphicsLayoutWidget(self.splitter)
        self.GraphicsLayoutWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphicsLayoutWidget.sizePolicy().hasHeightForWidth())
        self.GraphicsLayoutWidget.setSizePolicy(sizePolicy)
        self.GraphicsLayoutWidget.setBaseSize(QtCore.QSize(800, 300))
        self.GraphicsLayoutWidget.setObjectName("GraphicsLayoutWidget")
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalyse = QtWidgets.QMenu(self.menuBar)
        self.menuAnalyse.setObjectName("menuAnalyse")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave_annotations = QtWidgets.QAction(MainWindow)
        self.actionSave_annotations.setObjectName("actionSave_annotations")
        self.actionLoad_Library = QtWidgets.QAction(MainWindow)
        self.actionLoad_Library.setObjectName("actionLoad_Library")
        self.actionLoad_Predictions = QtWidgets.QAction(MainWindow)
        self.actionLoad_Predictions.setObjectName("actionLoad_Predictions")
        self.actionLoad_h5_folder = QtWidgets.QAction(MainWindow)
        self.actionLoad_h5_folder.setObjectName("actionLoad_h5_folder")
        self.actionConvert_dir_to_h5 = QtWidgets.QAction(MainWindow)
        self.actionConvert_dir_to_h5.setObjectName("actionConvert_dir_to_h5")
        self.actionConvert_ndf_to_h5 = QtWidgets.QAction(MainWindow)
        self.actionConvert_ndf_to_h5.setObjectName("actionConvert_ndf_to_h5")
        self.actionLibrary_logistics = QtWidgets.QAction(MainWindow)
        self.actionLibrary_logistics.setObjectName("actionLibrary_logistics")
        self.actionAdd_to_library = QtWidgets.QAction(MainWindow)
        self.actionAdd_to_library.setObjectName("actionAdd_to_library")
        self.actionAdd_labels_to_library = QtWidgets.QAction(MainWindow)
        self.actionAdd_labels_to_library.setObjectName("actionAdd_labels_to_library")
        self.actionAdd_features_to_library = QtWidgets.QAction(MainWindow)
        self.actionAdd_features_to_library.setObjectName("actionAdd_features_to_library")
        self.actionClassifier_components = QtWidgets.QAction(MainWindow)
        self.actionClassifier_components.setObjectName("actionClassifier_components")
        self.actionRun_classifer_on_h5_dir = QtWidgets.QAction(MainWindow)
        self.actionRun_classifer_on_h5_dir.setObjectName("actionRun_classifer_on_h5_dir")
        self.actionRun_classifer_on_ndf_dir = QtWidgets.QAction(MainWindow)
        self.actionRun_classifer_on_ndf_dir.setObjectName("actionRun_classifer_on_ndf_dir")
        self.actionSet_default_folder = QtWidgets.QAction(MainWindow)
        self.actionSet_default_folder.setObjectName("actionSet_default_folder")
        self.actionAdd_features_to_h5_folder = QtWidgets.QAction(MainWindow)
        self.actionAdd_features_to_h5_folder.setObjectName("actionAdd_features_to_h5_folder")
        self.actionFolder_for_substates = QtWidgets.QAction(MainWindow)
        self.actionFolder_for_substates.setObjectName("actionFolder_for_substates")
        self.actionSubstates_Window = QtWidgets.QAction(MainWindow)
        self.actionSubstates_Window.setObjectName("actionSubstates_Window")
        self.actionOpen_in_Jupyter_notebook = QtWidgets.QAction(MainWindow)
        self.actionOpen_in_Jupyter_notebook.setObjectName("actionOpen_in_Jupyter_notebook")
        self.menuFile.addAction(self.actionLoad_Library)
        self.menuFile.addAction(self.actionLoad_Predictions)
        self.menuFile.addAction(self.actionLoad_h5_folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_annotations)
        self.menuFile.addAction(self.actionSet_default_folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSubstates_Window)
        self.menuAnalyse.addAction(self.actionConvert_ndf_to_h5)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionAdd_features_to_h5_folder)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionLibrary_logistics)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionClassifier_components)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionOpen_in_Jupyter_notebook)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAnalyse.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "File list"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Mouse functionality and keyboard shortcuts</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Mouse: Scroll when hovering over either axis in the main plot to zoom that axis only. Scrolling when in the middle will zoom both axes at the same time - you probably don\'t want that.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Up arrow:         Zoom in / speed up </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Down arrow:     Zoom out / slow down </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Right arrow:     Step right / scroll forwards </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Left arrow:     Step left / scroll backwards</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Numbers:         Set plot time interval </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">B key:         Toggle blink vs scroll </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Space bar:        Start scrolling (or blinking)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Left click + Shift:    Mark start of an event in uppper window</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Left click + Alt:     Mark end of event</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Help"))
        self.label_6.setText(_translate("MainWindow", " TID: "))
        self.label_11.setText(_translate("MainWindow", "Hold position:"))
        self.label_8.setText(_translate("MainWindow", "High pass:"))
        self.label_9.setText(_translate("MainWindow", "Low pass:"))
        self.label_2.setText(_translate("MainWindow", "Filter  (Hz)"))
        self.label_7.setText(_translate("MainWindow", "Scrolling"))
        self.label_5.setText(_translate("MainWindow", "X range (s):"))
        self.label.setText(_translate("MainWindow", "Scroll speed:"))
        self.label_10.setText(_translate("MainWindow", "Blinking:"))
        self.label_4.setText(_translate("MainWindow", " h5 folder:"))
        self.label_3.setText(_translate("MainWindow", " Annotation file:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalyse.setTitle(_translate("MainWindow", "Analyse"))
        self.actionSave_annotations.setText(_translate("MainWindow", "Save annotations"))
        self.actionLoad_Library.setText(_translate("MainWindow", "Load Library"))
        self.actionLoad_Predictions.setText(_translate("MainWindow", "Load Predictions"))
        self.actionLoad_h5_folder.setText(_translate("MainWindow", "Load h5 folder"))
        self.actionConvert_dir_to_h5.setText(_translate("MainWindow", "Convert dir to h5"))
        self.actionConvert_ndf_to_h5.setText(_translate("MainWindow", "Convert ndf folder to h5"))
        self.actionLibrary_logistics.setText(_translate("MainWindow", "Library logistics"))
        self.actionAdd_to_library.setText(_translate("MainWindow", "Add to library"))
        self.actionAdd_labels_to_library.setText(_translate("MainWindow", "Add labels to library"))
        self.actionAdd_features_to_library.setText(_translate("MainWindow", "Add features to library"))
        self.actionClassifier_components.setText(_translate("MainWindow", "Classifier components"))
        self.actionRun_classifer_on_h5_dir.setText(_translate("MainWindow", "Run classifer on h5 dir"))
        self.actionRun_classifer_on_ndf_dir.setText(_translate("MainWindow", "Run classifer on ndf dir"))
        self.actionSet_default_folder.setText(_translate("MainWindow", "Set default folder"))
        self.actionAdd_features_to_h5_folder.setText(_translate("MainWindow", "Add features to h5 folder"))
        self.actionFolder_for_substates.setText(_translate("MainWindow", "Folder for substates"))
        self.actionSubstates_Window.setText(_translate("MainWindow", "Substates Window"))
        self.actionOpen_in_Jupyter_notebook.setText(_translate("MainWindow", "Open in Jupyter notebook"))

from pyqtgraph import GraphicsLayoutWidget
