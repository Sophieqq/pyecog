# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_preds_design_v2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt
class PecogQTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self,*args, **kwargs):
        super(PecogQTreeWidget, self).__init__(*args, **kwargs)
        self.substate_child_selected = False

    def pyecog_save(self):
        print('!s')
        pass

    def keyPressEvent(self, QKeyEvent):
        key_id = QKeyEvent.key()

        key_id_to_numbers = {eval('Qt.Key_'+str(i)):i for i in range(0,10)}
        if key_id in list(key_id_to_numbers.keys()):

            if self.substate_child_selected:
                key_val = key_id_to_numbers[key_id]
                self.currentItem().setText(2, str(key_val))
                # make down press command
                fake_down_press =QtGui.QKeyEvent(QtCore.QEvent.KeyPress, QtCore.Qt.Key_Down, QtCore.Qt.NoModifier)
                super(PecogQTreeWidget,self).keyPressEvent(fake_down_press)

        elif key_id == Qt.Key_S:
            self.pyecog_save()

        else:
            super(PecogQTreeWidget,self).keyPressEvent(QKeyEvent)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.full_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.full_splitter.setOrientation(QtCore.Qt.Vertical)
        self.full_splitter.setObjectName("full_splitter")
        self.top_splitter = QtWidgets.QSplitter(self.full_splitter)
        self.top_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.top_splitter.setObjectName("top_splitter")
        #self.treeWidget = QtWidgets.QTreeWidget(self.top_splitter)
        self.treeWidget = PecogQTreeWidget(self.top_splitter)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setBaseSize(QtCore.QSize(200, 300))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.setFont(font)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setColumnCount(8)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
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
        self.GraphicsLayoutWidget = GraphicsLayoutWidget(self.top_splitter)
        self.GraphicsLayoutWidget.setEnabled(True)
        self.GraphicsLayoutWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.GraphicsLayoutWidget.setBaseSize(QtCore.QSize(700, 300))
        self.GraphicsLayoutWidget.setObjectName("GraphicsLayoutWidget")
        self.overview_plot = GraphicsLayoutWidget(self.full_splitter)
        self.overview_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.overview_plot.setBaseSize(QtCore.QSize(912, 200))
        self.overview_plot.setObjectName("overview_plot")
        self.bottom_splitter = QtWidgets.QSplitter(self.full_splitter)
        self.bottom_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.bottom_splitter.setObjectName("bottom_splitter")
        self.layoutWidget = QtWidgets.QWidget(self.bottom_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.h5_folder_display = QtWidgets.QLineEdit(self.layoutWidget)
        self.h5_folder_display.setMinimumSize(QtCore.QSize(0, 0))
        self.h5_folder_display.setMaximumSize(QtCore.QSize(16777215, 100))
        self.h5_folder_display.setDragEnabled(True)
        self.h5_folder_display.setReadOnly(True)
        self.h5_folder_display.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.h5_folder_display.setObjectName("h5_folder_display")
        self.gridLayout_3.addWidget(self.h5_folder_display, 1, 1, 1, 1)
        self.scroll_speed_box = QtWidgets.QSpinBox(self.layoutWidget)
        self.scroll_speed_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.scroll_speed_box.setMinimum(1)
        self.scroll_speed_box.setObjectName("scroll_speed_box")
        self.gridLayout_3.addWidget(self.scroll_speed_box, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.predictions_file_display = QtWidgets.QLineEdit(self.layoutWidget)
        self.predictions_file_display.setMinimumSize(QtCore.QSize(0, 0))
        self.predictions_file_display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.predictions_file_display.setObjectName("predictions_file_display")
        self.gridLayout_3.addWidget(self.predictions_file_display, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)
        self.blink_box = QtWidgets.QCheckBox(self.layoutWidget)
        self.blink_box.setObjectName("blink_box")
        self.gridLayout_3.addWidget(self.blink_box, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 2, 1, 1)
        self.xrange_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.xrange_spinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.xrange_spinBox.setMinimum(1)
        self.xrange_spinBox.setProperty("value", 5)
        self.xrange_spinBox.setObjectName("xrange_spinBox")
        self.gridLayout_3.addWidget(self.xrange_spinBox, 2, 3, 1, 1)
        self.tid_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.tid_spinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.tid_spinBox.setObjectName("tid_spinBox")
        self.gridLayout_3.addWidget(self.tid_spinBox, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.bottom_splitter)
        self.textBrowser.setMaximumSize(QtCore.QSize(400, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.full_splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1005, 22))
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
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAnalyse.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Scroll type"))
        self.label_4.setText(_translate("MainWindow", "h5 Folder:"))
        self.label_3.setText(_translate("MainWindow", "Prediction File:"))
        self.label.setText(_translate("MainWindow", "Scroll speed"))
        self.blink_box.setText(_translate("MainWindow", "Blinking"))
        self.label_5.setText(_translate("MainWindow", "Xrange (sec)"))
        self.label_6.setText(_translate("MainWindow", "Tid for h5 folder "))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt; font-weight:600;\">Mouse Functionality</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">Scroll when hovering over either axis in the main plot to zoom that axis only. Scrolling when in the middle will zoom both axes at the same time - you probably don\'t want that.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt; font-weight:600;\">Keyboard Shortcuts</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">Number key:   Set plot time interval </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">B key:              Toggle blink vs scroll</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">SPACE:           Start scrolling (or blinking)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">Up:        Zoom in   / speed up              </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">Down:        Zoom out / slow down              </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">Right arrow:    Step right / scroll forwards      </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\">Left arrow:        Step left   / scroll backwards</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt;\"><br /></p></body></html>"))
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

from pyqtgraph import GraphicsLayoutWidget
