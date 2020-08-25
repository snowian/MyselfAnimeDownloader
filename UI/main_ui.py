# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Anime(object):
    def setupUi(self, Anime):
        Anime.setObjectName("Anime")
        Anime.setWindowModality(QtCore.Qt.NonModal)
        Anime.resize(1021, 460)
        Anime.setStyleSheet("QScrollBar::vertical {\n"
                            "       border:0px solid grey;\n"
                            "       width: 15px;\n"
                            "       }\n"
                            "\n"
                            "       QScrollBar::handle:vertical {\n"
                            "       background:#dfdfdf;\n"
                            "       border-radius:6px;\n"
                            "       }\n"
                            "\n"
                            "       QMessageBox::QPushButton{\n"
                            "       background-color:#dedede;\n"
                            "       border-radius:6px;\n"
                            "       width: 71px;\n"
                            "       height: 31px;\n"
                            "       }\n"
                            "   ")
        Anime.setIconSize(QtCore.QSize(24, 24))
        Anime.setDocumentMode(False)
        Anime.setDockNestingEnabled(False)
        Anime.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Anime)
        self.centralwidget.setObjectName("centralwidget")
        self.anime_info_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.anime_info_tabWidget.setGeometry(QtCore.QRect(10, 20, 1001, 405))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.anime_info_tabWidget.setFont(font)
        self.anime_info_tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.anime_info_tabWidget.setStyleSheet("QTabWidget:pane {border-top:0px solid #e8f3f9;background: transparent; }")
        self.anime_info_tabWidget.setObjectName("anime_info_tabWidget")
        self.week_page = QtWidgets.QWidget()
        self.week_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.week_page.setObjectName("week_page")
        self.week_page_gridLayout = QtWidgets.QGridLayout(self.week_page)
        self.week_page_gridLayout.setObjectName("week_page_gridLayout")
        self.week_tabWidget = QtWidgets.QTabWidget(self.week_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.week_tabWidget.setFont(font)
        self.week_tabWidget.setObjectName("week_tabWidget")
        self.Monday = QtWidgets.QWidget()
        self.Monday.setObjectName("Monday")
        self.monday_gridLayout = QtWidgets.QGridLayout(self.Monday)
        self.monday_gridLayout.setObjectName("monday_gridLayout")
        self.Monday_scrollArea = QtWidgets.QScrollArea(self.Monday)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Monday_scrollArea.setFont(font)
        self.Monday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Monday_scrollArea.setWidgetResizable(True)
        self.Monday_scrollArea.setObjectName("Monday_scrollArea")
        self.Monday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Monday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Monday_scrollAreaWidgetContents.setObjectName("Monday_scrollAreaWidgetContents")
        self.Monday_scrollArea.setWidget(self.Monday_scrollAreaWidgetContents)
        self.monday_gridLayout.addWidget(self.Monday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Monday, "")
        self.Tuesday = QtWidgets.QWidget()
        self.Tuesday.setObjectName("Tuesday")
        self.tuesday_gridLayout = QtWidgets.QGridLayout(self.Tuesday)
        self.tuesday_gridLayout.setObjectName("tuesday_gridLayout")
        self.Tuesday_scrollArea = QtWidgets.QScrollArea(self.Tuesday)
        self.Tuesday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Tuesday_scrollArea.setWidgetResizable(True)
        self.Tuesday_scrollArea.setObjectName("Tuesday_scrollArea")
        self.Tuesday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Tuesday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Tuesday_scrollAreaWidgetContents.setObjectName("Tuesday_scrollAreaWidgetContents")
        self.Tuesday_scrollArea.setWidget(self.Tuesday_scrollAreaWidgetContents)
        self.tuesday_gridLayout.addWidget(self.Tuesday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Tuesday, "")
        self.Wednesday = QtWidgets.QWidget()
        self.Wednesday.setObjectName("Wednesday")
        self.wednesday_gridLayout = QtWidgets.QGridLayout(self.Wednesday)
        self.wednesday_gridLayout.setObjectName("wednesday_gridLayout")
        self.Wednesday_scrollArea = QtWidgets.QScrollArea(self.Wednesday)
        self.Wednesday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Wednesday_scrollArea.setWidgetResizable(True)
        self.Wednesday_scrollArea.setObjectName("Wednesday_scrollArea")
        self.Wednesday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Wednesday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Wednesday_scrollAreaWidgetContents.setObjectName("Wednesday_scrollAreaWidgetContents")
        self.Wednesday_scrollArea.setWidget(self.Wednesday_scrollAreaWidgetContents)
        self.wednesday_gridLayout.addWidget(self.Wednesday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Wednesday, "")
        self.Thursday = QtWidgets.QWidget()
        self.Thursday.setObjectName("Thursday")
        self.thursday_gridLayout = QtWidgets.QGridLayout(self.Thursday)
        self.thursday_gridLayout.setObjectName("thursday_gridLayout")
        self.Thursday_scrollArea = QtWidgets.QScrollArea(self.Thursday)
        self.Thursday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Thursday_scrollArea.setWidgetResizable(True)
        self.Thursday_scrollArea.setObjectName("Thursday_scrollArea")
        self.Thursday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Thursday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Thursday_scrollAreaWidgetContents.setObjectName("Thursday_scrollAreaWidgetContents")
        self.Thursday_scrollArea.setWidget(self.Thursday_scrollAreaWidgetContents)
        self.thursday_gridLayout.addWidget(self.Thursday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Thursday, "")
        self.Friday = QtWidgets.QWidget()
        self.Friday.setObjectName("Friday")
        self.friday_gridLayout = QtWidgets.QGridLayout(self.Friday)
        self.friday_gridLayout.setObjectName("friday_gridLayout")
        self.Friday_scrollArea = QtWidgets.QScrollArea(self.Friday)
        self.Friday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Friday_scrollArea.setWidgetResizable(True)
        self.Friday_scrollArea.setObjectName("Friday_scrollArea")
        self.Friday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Friday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Friday_scrollAreaWidgetContents.setObjectName("Friday_scrollAreaWidgetContents")
        self.Friday_scrollArea.setWidget(self.Friday_scrollAreaWidgetContents)
        self.friday_gridLayout.addWidget(self.Friday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Friday, "")
        self.Staurday = QtWidgets.QWidget()
        self.Staurday.setObjectName("Staurday")
        self.staurday_gridLayout = QtWidgets.QGridLayout(self.Staurday)
        self.staurday_gridLayout.setObjectName("staurday_gridLayout")
        self.Staurday_scrollArea = QtWidgets.QScrollArea(self.Staurday)
        self.Staurday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Staurday_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Staurday_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Staurday_scrollArea.setWidgetResizable(True)
        self.Staurday_scrollArea.setObjectName("Staurday_scrollArea")
        self.Staurday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Staurday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Staurday_scrollAreaWidgetContents.setObjectName("Staurday_scrollAreaWidgetContents")
        self.Staurday_scrollArea.setWidget(self.Staurday_scrollAreaWidgetContents)
        self.staurday_gridLayout.addWidget(self.Staurday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Staurday, "")
        self.Sunday = QtWidgets.QWidget()
        self.Sunday.setObjectName("Sunday")
        self.sunday_gridLayout = QtWidgets.QGridLayout(self.Sunday)
        self.sunday_gridLayout.setObjectName("sunday_gridLayout")
        self.Sunday_scrollArea = QtWidgets.QScrollArea(self.Sunday)
        self.Sunday_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Sunday_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Sunday_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Sunday_scrollArea.setWidgetResizable(True)
        self.Sunday_scrollArea.setObjectName("Sunday_scrollArea")
        self.Sunday_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Sunday_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 965, 313))
        self.Sunday_scrollAreaWidgetContents.setObjectName("Sunday_scrollAreaWidgetContents")
        self.Sunday_scrollArea.setWidget(self.Sunday_scrollAreaWidgetContents)
        self.sunday_gridLayout.addWidget(self.Sunday_scrollArea, 0, 0, 1, 1)
        self.week_tabWidget.addTab(self.Sunday, "")
        self.week_page_gridLayout.addWidget(self.week_tabWidget, 0, 0, 1, 1)
        self.anime_info_tabWidget.addTab(self.week_page, "")
        self.end_page = QtWidgets.QWidget()
        self.end_page.setObjectName("end_page")
        self.end_gridLayout = QtWidgets.QGridLayout(self.end_page)
        self.end_gridLayout.setObjectName("end_gridLayout")
        self.end_scrollArea = QtWidgets.QScrollArea(self.end_page)
        self.end_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.end_scrollArea.setWidgetResizable(True)
        self.end_scrollArea.setObjectName("end_scrollArea")
        self.end_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.end_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 983, 363))
        self.end_scrollAreaWidgetContents.setObjectName("end_scrollAreaWidgetContents")
        self.end_scrollAreaWidgetContents_Layout = QtWidgets.QVBoxLayout(self.end_scrollAreaWidgetContents)
        self.end_scrollAreaWidgetContents_Layout.setObjectName("end_scrollAreaWidgetContents_Layout")
        self.end_scrollArea.setWidget(self.end_scrollAreaWidgetContents)
        self.end_gridLayout.addWidget(self.end_scrollArea, 0, 0, 1, 1)
        self.anime_info_tabWidget.addTab(self.end_page, "")
        self.anime_page = QtWidgets.QWidget()
        self.anime_page.setStyleSheet("QGridLayout {background: transparent; }")
        self.anime_page.setObjectName("anime_page")
        self.anime_page_gridLayout = QtWidgets.QGridLayout(self.anime_page)
        self.anime_page_gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.anime_page_gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.anime_page_gridLayout.setVerticalSpacing(25)
        self.anime_page_gridLayout.setObjectName("anime_page_gridLayout")
        self.image_label = QtWidgets.QLabel(self.anime_page)
        self.image_label.setMinimumSize(QtCore.QSize(250, 0))
        self.image_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image_label.setObjectName("image_label")
        self.anime_page_gridLayout.addWidget(self.image_label, 0, 0, 4, 1)
        self.type_label = QtWidgets.QLabel(self.anime_page)
        self.type_label.setMinimumSize(QtCore.QSize(0, 30))
        self.type_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.type_label.setObjectName("type_label")
        self.anime_page_gridLayout.addWidget(self.type_label, 0, 1, 1, 1)
        self.total_set_label = QtWidgets.QLabel(self.anime_page)
        self.total_set_label.setMinimumSize(QtCore.QSize(0, 30))
        self.total_set_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.total_set_label.setObjectName("total_set_label")
        self.anime_page_gridLayout.addWidget(self.total_set_label, 1, 1, 1, 1)
        self.web_label = QtWidgets.QLabel(self.anime_page)
        self.web_label.setMinimumSize(QtCore.QSize(0, 30))
        self.web_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.web_label.setObjectName("web_label")
        self.anime_page_gridLayout.addWidget(self.web_label, 2, 1, 1, 1)
        self.premiere_label = QtWidgets.QLabel(self.anime_page)
        self.premiere_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.premiere_label.setObjectName("premiere_label")
        self.anime_page_gridLayout.addWidget(self.premiere_label, 0, 2, 1, 1)
        self.remarks_label = QtWidgets.QLabel(self.anime_page)
        self.remarks_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.remarks_label.setObjectName("remarks_label")
        self.anime_page_gridLayout.addWidget(self.remarks_label, 2, 2, 1, 1)
        self.author_label = QtWidgets.QLabel(self.anime_page)
        self.author_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.author_label.setObjectName("author_label")
        self.anime_page_gridLayout.addWidget(self.author_label, 1, 2, 1, 1)
        self.story_list_widget = QtWidgets.QWidget(self.anime_page)
        self.story_list_widget.setObjectName("story_list_widget")
        self.story_list_label = QtWidgets.QLabel(self.story_list_widget)
        self.story_list_label.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.story_list_label.setMinimumSize(QtCore.QSize(0, 0))
        self.story_list_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.story_list_label.setFont(font)
        self.story_list_label.setStyleSheet("QLabel{\n"
"background-color:#dedede;\n"
"border-radius:6px\n"
"}")
        self.story_list_label.setObjectName("story_list_label")
        self.story_list_all_pushButton = QtWidgets.QPushButton(self.story_list_widget)
        self.story_list_all_pushButton.setGeometry(QtCore.QRect(10, 320, 91, 30))
        self.story_list_all_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.story_list_all_pushButton.setFont(font)
        self.story_list_all_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.story_list_all_pushButton.setStyleSheet("")
        self.story_list_all_pushButton.setObjectName("story_list_all_pushButton")
        self.story_list_scrollArea = QtWidgets.QScrollArea(self.story_list_widget)
        self.story_list_scrollArea.setGeometry(QtCore.QRect(10, 60, 211, 251))
        self.story_list_scrollArea.setStyleSheet("")
        self.story_list_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story_list_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.story_list_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.story_list_scrollArea.setWidgetResizable(True)
        self.story_list_scrollArea.setObjectName("story_list_scrollArea")
        self.story_list_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.story_list_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 211, 251))
        self.story_list_scrollAreaWidgetContents.setObjectName("story_list_scrollAreaWidgetContents")
        self.story_list_scrollAreaWidgetContents_Layout = QtWidgets.QVBoxLayout(self.story_list_scrollAreaWidgetContents)
        self.story_list_scrollAreaWidgetContents_Layout.setObjectName("story_list_scrollAreaWidgetContents_Layout")
        self.story_list_scrollArea.setWidget(self.story_list_scrollAreaWidgetContents)
        self.download_pushbutton = QtWidgets.QPushButton(self.story_list_widget)
        self.download_pushbutton.setGeometry(QtCore.QRect(120, 320, 101, 30))
        self.download_pushbutton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.download_pushbutton.setFont(font)
        self.download_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_pushbutton.setStyleSheet("")
        self.download_pushbutton.setObjectName("download_pushbutton")
        self.anime_page_gridLayout.addWidget(self.story_list_widget, 0, 3, 4, 1)
        self.introduction_textBrowser = QtWidgets.QTextBrowser(self.anime_page)
        self.introduction_textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.introduction_textBrowser.setStyleSheet("QTextBrowser {border-top:0px solid #e8f3f9;background: transparent; }")
        self.introduction_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.introduction_textBrowser.setObjectName("introduction_textBrowser")
        self.anime_page_gridLayout.addWidget(self.introduction_textBrowser, 3, 1, 1, 2)
        self.anime_info_tabWidget.addTab(self.anime_page, "")
        self.download_page = QtWidgets.QWidget()
        self.download_page.setObjectName("download_page")
        self.down_list_gridLayout = QtWidgets.QGridLayout(self.download_page)
        self.down_list_gridLayout.setObjectName("down_list_gridLayout")
        self.download_tableWidget = QtWidgets.QTableWidget(self.download_page)
        self.download_tableWidget.setStyleSheet("QTableView::item{\n"
"gridline-color:#000000\n"
"}")
        self.download_tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.download_tableWidget.setObjectName("download_tableWidget")
        self.download_tableWidget.setColumnCount(3)
        self.download_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.download_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.download_tableWidget.setHorizontalHeaderItem(2, item)
        self.download_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.down_list_gridLayout.addWidget(self.download_tableWidget, 0, 0, 1, 1)
        self.anime_info_tabWidget.addTab(self.download_page, "")
        self.history_page = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(9)
        self.history_page.setFont(font)
        self.history_page.setObjectName("history_page")
        self.history_layout = QtWidgets.QVBoxLayout(self.history_page)
        self.history_layout.setObjectName("history_layout")
        self.history_tableWidget = QtWidgets.QTableWidget(self.history_page)
        self.history_tableWidget.setObjectName("history_tableWidget")
        self.history_tableWidget.setColumnCount(2)
        self.history_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.history_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_tableWidget.setHorizontalHeaderItem(1, item)
        self.history_layout.addWidget(self.history_tableWidget)
        self.anime_info_tabWidget.addTab(self.history_page, "")
        self.customize_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.customize_groupBox.setGeometry(QtCore.QRect(590, 0, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customize_groupBox.setFont(font)
        self.customize_groupBox.setStyleSheet("QGroupBox{\n"
                                              "border:none}")
        self.customize_groupBox.setObjectName("customize_groupBox")
        self.customize_label = QtWidgets.QLabel(self.customize_groupBox)
        self.customize_label.setGeometry(QtCore.QRect(10, 25, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customize_label.setFont(font)
        self.customize_label.setObjectName("customize_label")
        self.customize_lineEdit = QtWidgets.QLineEdit(self.customize_groupBox)
        self.customize_lineEdit.setGeometry(QtCore.QRect(60, 23, 291, 21))
        self.customize_lineEdit.setObjectName("customize_lineEdit")
        self.customize_pushButton = QtWidgets.QPushButton(self.customize_groupBox)
        self.customize_pushButton.setGeometry(QtCore.QRect(360, 21, 51, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customize_pushButton.setFont(font)
        self.customize_pushButton.setStyleSheet("")
        self.customize_pushButton.setObjectName("customize_pushButton")
        self.load_week_label = QtWidgets.QLabel(self.centralwidget)
        self.load_week_label.setGeometry(QtCore.QRect(370, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_week_label.setFont(font)
        self.load_week_label.setAlignment(QtCore.Qt.AlignCenter)
        self.load_week_label.setObjectName("load_week_label")
        self.load_anime_label = QtWidgets.QLabel(self.centralwidget)
        self.load_anime_label.setEnabled(True)
        self.load_anime_label.setGeometry(QtCore.QRect(350, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_anime_label.setFont(font)
        self.load_anime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.load_anime_label.setObjectName("load_anime_label")
        self.status_widget = QtWidgets.QWidget(self.centralwidget)
        self.status_widget.setGeometry(QtCore.QRect(0, 415, 1011, 21))
        self.status_widget.setStyleSheet("QWidget{\n"
                                         "background-color: rgba(255, 255, 240, 100)\n"
                                         "}")
        self.status_widget.setObjectName("status_widget")
        self.left_status_label = QtWidgets.QLabel(self.status_widget)
        self.left_status_label.setGeometry(QtCore.QRect(20, 0, 211, 20))
        self.left_status_label.setObjectName("left_status_label")
        self.right_ststus_label = QtWidgets.QLabel(self.status_widget)
        self.right_ststus_label.setGeometry(QtCore.QRect(780, 0, 211, 20))
        self.right_ststus_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.right_ststus_label.setObjectName("right_ststus_label")
        self.load_end_anime_label = QtWidgets.QLabel(self.centralwidget)
        self.load_end_anime_label.setGeometry(QtCore.QRect(400, 155, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_end_anime_label.setFont(font)
        self.load_end_anime_label.setObjectName("load_end_anime_label")
        Anime.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Anime)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        Anime.setMenuBar(self.menubar)
        self.menu_config = QtWidgets.QAction(Anime)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../image/config.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_config.setIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu_config.setFont(font)
        self.menu_config.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.menu_config.setPriority(QtWidgets.QAction.NormalPriority)
        self.menu_config.setObjectName("menu_config")
        self.menu_exit = QtWidgets.QAction(Anime)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\UI\\../image/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_exit.setIcon(icon1)
        self.menu_exit.setObjectName("menu_exit")
        self.menu_about = QtWidgets.QAction(Anime)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\UI\\../image/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_about.setIcon(icon2)
        self.menu_about.setObjectName("menu_about")
        self.menu.addAction(self.menu_config)
        self.menu.addAction(self.menu_about)
        self.menu.addAction(self.menu_exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Anime)
        self.anime_info_tabWidget.setCurrentIndex(0)
        self.week_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Anime)

    def retranslateUi(self, Anime):
        _translate = QtCore.QCoreApplication.translate
        Anime.setWindowTitle(_translate("Anime", "Anime Download"))
        self.anime_info_tabWidget.setWhatsThis(_translate("Anime", "<html><head/><body><p><br/></p></body></html>"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Monday), _translate("Anime", "一"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Tuesday), _translate("Anime", "二"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Wednesday), _translate("Anime", "三"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Thursday), _translate("Anime", "四"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Friday), _translate("Anime", "五"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Staurday), _translate("Anime", "六"))
        self.week_tabWidget.setTabText(self.week_tabWidget.indexOf(self.Sunday), _translate("Anime", "日"))
        self.anime_info_tabWidget.setTabText(self.anime_info_tabWidget.indexOf(self.week_page),
                                             _translate("Anime", "每周更新"))
        self.anime_info_tabWidget.setTabText(self.anime_info_tabWidget.indexOf(self.end_page),
                                             _translate("Anime", "完結列表"))
        self.image_label.setText(_translate("Anime", "anime_image"))
        self.type_label.setText(_translate("Anime", "TextLabel"))
        self.total_set_label.setText(_translate("Anime", "TextLabel"))
        self.web_label.setText(_translate("Anime", "TextLabel"))
        self.premiere_label.setText(_translate("Anime", "TextLabel"))
        self.remarks_label.setText(_translate("Anime", "TextLabel"))
        self.author_label.setText(_translate("Anime", "TextLabel"))
        self.story_list_label.setText(_translate("Anime", " 劇情列表"))
        self.story_list_all_pushButton.setText(_translate("Anime", "全選"))
        self.download_pushbutton.setText(_translate("Anime", "開始下載"))
        self.introduction_textBrowser.setHtml(_translate("Anime",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.anime_info_tabWidget.setTabText(self.anime_info_tabWidget.indexOf(self.anime_page),
                                             _translate("Anime", "動漫資訊"))
        self.download_page.setWhatsThis(_translate("Anime", "<html><head/><body><p>123</p></body></html>"))
        self.download_tableWidget.setSortingEnabled(False)
        item = self.download_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Anime", "名稱"))
        item = self.download_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Anime", "狀態"))
        item = self.download_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Anime", "進度"))
        self.anime_info_tabWidget.setTabText(self.anime_info_tabWidget.indexOf(self.download_page),
                                             _translate("Anime", "下載清單"))
        item = self.history_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Anime", "名稱"))
        item = self.history_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Anime", "下載時間"))
        self.anime_info_tabWidget.setTabText(self.anime_info_tabWidget.indexOf(self.history_page),
                                             _translate("Anime", "歷史紀錄"))
        self.customize_groupBox.setTitle(_translate("Anime", "每周更新以外的動漫"))
        self.customize_label.setText(_translate("Anime", "網址:"))
        self.customize_pushButton.setText(_translate("Anime", "確定"))
        self.load_week_label.setText(_translate("Anime", "每周動漫更新讀取中"))
        self.load_anime_label.setText(_translate("Anime", "動漫資訊讀取中"))
        self.left_status_label.setText(_translate("Anime", "狀態: 0 個下載中　　連接設定: 0/20"))
        self.right_ststus_label.setText(_translate("Anime", "記憶體用量: 10.10MB / 程序: 3.50%"))
        self.load_end_anime_label.setText(_translate("Anime", "完結動漫讀取中"))
        self.menu.setTitle(_translate("Anime", "設定"))
        self.menu_config.setText(_translate("Anime", "設定"))
        self.menu_config.setStatusTip(_translate("Anime", "設定"))
        self.menu_exit.setText(_translate("Anime", "離開"))
        self.menu_exit.setStatusTip(_translate("Anime", "離開"))
        self.menu_about.setText(_translate("Anime", "關於"))
        self.menu_about.setStatusTip(_translate("Anime", "關於"))
