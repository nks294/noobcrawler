from PyQt5 import QtCore, QtGui, QtWidgets
import res.res


class Ui_MainWindow(object):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(900, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowTitle("자동차 사진 크롤러 ver.GUI")
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("""
            QWidget#win_main { background-color: rgb(22,22,22); }
            QListWidget { background-color:rgb(66,68,74); color: #ecf0f1; border:none; }
            QTextBrowser { background-color: rgb(54,55,61); color: #ecf0f1; border: none; padding-left: 10px; padding-right: 10px; }


            QLabel { color: #ecf0f1; padding-bottom: 3px; }
            QLabel#lab_list { background-color: rgb(81,82,91); }
            QLabel#lab_path { background-color: rgb(54,54,101); padding-left: 6px;}
            QLabel#lab_paths { padding-left: 10px; background-color: rgb(94,95,106);}
            QLabel#lab_view { background-color: #4f6978; }
            QLabel#lab_log { background-color: rgb(65,65,73); }
            QLabel#lab_model, QLabel#lab_brand, QLabel#lab_grade { background-color: rgb(102,103,115); color: #ecf0f1; border: none; padding-left: 5px; }
            QLabel#lab_info1 { background-color: #5f686d; color: #ecf0f1; border: none; }
            QLabel#lab_info2, QLabel#lab_info3 { background-color: rgb(65,65,73); color: #ecf0f1; padding-left: 10px;}
            QLabel#lab_title { background-color: #2980b9; color: #ecf0f1; padding-left: 20px; padding-bottom: 1px; }

            QLabel#ico_setting { image:url(:/images/setting.png); background-color: rgb(102,103,115); padding-top: 0.2em;}
            QLabel#ico_log { image:url(:/images/console.png); background-color: rgb(65,65,73); padding-top: 0.2em;}
            QLabel#ico_images { image:url(:/images/doc.png); background-color: rgb(81,82,91); padding-top: 0.2em;}

            QLabel#win_pic { background-color: rgb(54,55,61); }


            QPushButton { border:none; background-color: #3d4f5a; color: #ecf0f1; }
            QPushButton#btn_close { image:url(:/res/resources/icons-09.png); background-color:transparent; }
            QPushButton#btn_dir { image:url(:/images/folder.png); background-color:rgb(94,95,106); border:none; }
            QPushButton#btn_download { image:url(:/images/download.png); background-color:rgb(102,103,115); border:none; }
            QPushButton#btn_view_func_1, QPushButton#btn_view_func_2, QPushButton#btn_view_func_3 { background-color: rgb(61,62,69);} 


            QComboBox { background-color: rgb(102,103,115); color: #ecf0f1; border: none; padding-left: 10px; }
            QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; border:none; }
            QComboBox::down-arrow { image:url(:/images/down_arrow.png); }
            QComboBox#com_count { background-color: rgb(89,90,102); border: none; }
			QComboBox QAbstractItemView { border: none; background-color: transparent; selection-background-color: rgba(0,0,0,0.1); color: white; }


            QScrollBar:vertical { border: none; background: transparent; width: 10px; margin-top: 10px; margin-bottom: 10px; }
            QScrollBar::handle:vertical { background: rgba(255,255,255,0.15); }
            QScrollBar::add-line:vertical { border: none; background: none; }
            QScrollBar::sub-line:vertical { border: none; background: none; }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { border: none; background: none; }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }
            QScrollBar:horizontal { border: none; background: transparent; margin-left: 10px; margin-right: 10px; height: 10px; }
            QScrollBar::handle:horizontal { background: rgba(255,255,255,0.15); }
            QScrollBar::add-line:horizontal { border: none; background: none; }
            QScrollBar::sub-line:horizontal { border: none; background: none; }
            QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal { border: none; background: none; }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; }
            """)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.win_main = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.win_main.sizePolicy().hasHeightForWidth())
        self.win_main.setSizePolicy(sizePolicy)
        self.win_main.setMinimumSize(QtCore.QSize(900, 700))
        self.win_main.setMaximumSize(QtCore.QSize(1920, 1080))
        self.win_main.setStyleSheet("")
        self.win_main.setInputMethodHints(QtCore.Qt.ImhNone)
        self.win_main.setObjectName("win_main")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.win_main)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(0)
        self.layout_main.setObjectName("layout_main")
        self.layout_img_func = QtWidgets.QHBoxLayout()
        self.layout_img_func.setContentsMargins(0, 0, 0, 0)
        self.layout_img_func.setSpacing(0)
        self.layout_img_func.setObjectName("layout_img_func")
        self.btn_dir = QtWidgets.QPushButton(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dir.sizePolicy().hasHeightForWidth())
        self.btn_dir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.btn_dir.setFont(font)
        self.btn_dir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dir.setText("")
        self.btn_dir.setObjectName("btn_dir")
        self.layout_img_func.addWidget(self.btn_dir)
        self.layout_img_func_set = QtWidgets.QVBoxLayout()
        self.layout_img_func_set.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_img_func_set.setContentsMargins(0, 0, 0, -1)
        self.layout_img_func_set.setSpacing(0)
        self.layout_img_func_set.setObjectName("layout_img_func_set")
        self.layout_img_func_set_dir = QtWidgets.QHBoxLayout()
        self.layout_img_func_set_dir.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_img_func_set_dir.setContentsMargins(-1, -1, 5, -1)
        self.layout_img_func_set_dir.setSpacing(0)
        self.layout_img_func_set_dir.setObjectName("layout_img_func_set_dir")
        self.lab_paths = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_paths.sizePolicy().hasHeightForWidth())
        self.lab_paths.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_paths.setFont(font)
        self.lab_paths.setStyleSheet("")
        self.lab_paths.setText("")
        self.lab_paths.setObjectName("lab_paths")
        self.layout_img_func_set_dir.addWidget(self.lab_paths)
        self.com_count = QtWidgets.QComboBox(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_count.sizePolicy().hasHeightForWidth())
        self.com_count.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.com_count.setFont(font)
        self.com_count.setObjectName("com_count")
        self.com_count.addItem("")
        self.com_count.setItemText(0, "COUNT")
        for i in range(1, 301):
            self.com_count.addItem("")
            self.com_count.setItemText(i, str(i))
        self.layout_img_func_set_dir.addWidget(self.com_count)
        self.layout_img_func_set_dir.setStretch(0, 600)
        self.layout_img_func_set_dir.setStretch(1, 80)
        self.layout_img_func_set.addLayout(self.layout_img_func_set_dir)
        self.layout_img_func_set_grade = QtWidgets.QHBoxLayout()
        self.layout_img_func_set_grade.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_img_func_set_grade.setContentsMargins(5, 5, 0, -1)
        self.layout_img_func_set_grade.setSpacing(0)
        self.layout_img_func_set_grade.setObjectName("layout_img_func_set_grade")
        self.ico_setting = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico_setting.sizePolicy().hasHeightForWidth())
        self.ico_setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.ico_setting.setFont(font)
        self.ico_setting.setText("")
        self.ico_setting.setObjectName("ico_setting")
        self.layout_img_func_set_grade.addWidget(self.ico_setting)
        self.lab_brand = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_brand.sizePolicy().hasHeightForWidth())
        self.lab_brand.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_brand.setFont(font)
        self.lab_brand.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lab_brand.setObjectName("lab_brand")
        self.layout_img_func_set_grade.addWidget(self.lab_brand)
        self.com_brand = QtWidgets.QComboBox(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_brand.sizePolicy().hasHeightForWidth())
        self.com_brand.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.com_brand.setFont(font)
        self.com_brand.setObjectName("com_brand")
        self.layout_img_func_set_grade.addWidget(self.com_brand)
        self.com_brand.addItem("")
        self.com_brand.setItemText(0, "현대")
        self.com_brand.addItem("")
        self.com_brand.setItemText(1, "제네시스")
        self.com_brand.addItem("")
        self.com_brand.setItemText(2, "기아")
        self.com_brand.addItem("")
        self.com_brand.setItemText(3, "쉐보레(GM대우)")
        self.com_brand.addItem("")
        self.com_brand.setItemText(4, "르노삼성")
        self.com_brand.addItem("")
        self.com_brand.setItemText(5, "쌍용")
        self.lab_model = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_model.sizePolicy().hasHeightForWidth())
        self.lab_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_model.setFont(font)
        self.lab_model.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lab_model.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lab_model.setMidLineWidth(0)
        self.lab_model.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lab_model.setObjectName("lab_model")
        self.layout_img_func_set_grade.addWidget(self.lab_model)
        self.com_model = QtWidgets.QComboBox(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_model.sizePolicy().hasHeightForWidth())
        self.com_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.com_model.setFont(font)
        self.com_model.setObjectName("com_model")
        self.layout_img_func_set_grade.addWidget(self.com_model)
        self.lab_grade = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_grade.sizePolicy().hasHeightForWidth())
        self.lab_grade.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_grade.setFont(font)
        self.lab_grade.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lab_grade.setObjectName("lab_grade")
        self.layout_img_func_set_grade.addWidget(self.lab_grade)
        self.com_grade = QtWidgets.QComboBox(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_grade.sizePolicy().hasHeightForWidth())
        self.com_grade.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.com_grade.setFont(font)
        self.com_grade.setObjectName("com_grade")
        self.layout_img_func_set_grade.addWidget(self.com_grade)
        self.layout_img_func_set_grade.setStretch(0, 20)
        self.layout_img_func_set_grade.setStretch(1, 70)
        self.layout_img_func_set_grade.setStretch(2, 160)
        self.layout_img_func_set_grade.setStretch(3, 70)
        self.layout_img_func_set_grade.setStretch(4, 165)
        self.layout_img_func_set_grade.setStretch(5, 70)
        self.layout_img_func_set_grade.setStretch(6, 165)
        self.layout_img_func_set.addLayout(self.layout_img_func_set_grade)
        self.layout_img_func.addLayout(self.layout_img_func_set)
        self.btn_download = QtWidgets.QPushButton(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.btn_download.setFont(font)
        self.btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_download.setText("")
        self.btn_download.setObjectName("btn_download")
        self.layout_img_func.addWidget(self.btn_download)
        self.layout_img_func.setStretch(0, 60)
        self.layout_img_func.setStretch(1, 800)
        self.layout_img_func.setStretch(2, 60)
        self.layout_main.addLayout(self.layout_img_func)
        self.layout_img = QtWidgets.QHBoxLayout()
        self.layout_img.setContentsMargins(-1, 5, -1, 5)
        self.layout_img.setSpacing(0)
        self.layout_img.setObjectName("layout_img")
        self.layout_img_list = QtWidgets.QVBoxLayout()
        self.layout_img_list.setContentsMargins(-1, -1, 5, -1)
        self.layout_img_list.setSpacing(0)
        self.layout_img_list.setObjectName("layout_img_list")
        self.layout_img_lab = QtWidgets.QHBoxLayout()
        self.layout_img_lab.setSpacing(0)
        self.layout_img_lab.setObjectName("layout_img_lab")
        self.ico_images = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico_images.sizePolicy().hasHeightForWidth())
        self.ico_images.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.ico_images.setFont(font)
        self.ico_images.setText("")
        self.ico_images.setObjectName("ico_images")
        self.layout_img_lab.addWidget(self.ico_images)
        self.lab_list = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_list.sizePolicy().hasHeightForWidth())
        self.lab_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_list.setFont(font)
        self.lab_list.setStyleSheet("")
        self.lab_list.setObjectName("lab_list")
        self.layout_img_lab.addWidget(self.lab_list)
        self.layout_img_lab.setStretch(0, 1)
        self.layout_img_lab.setStretch(1, 8)
        self.layout_img_list.addLayout(self.layout_img_lab)
        self.listWidget = QtWidgets.QListWidget(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.layout_img_list.addWidget(self.listWidget)
        self.layout_img_list.setStretch(1, 1)
        self.layout_img.addLayout(self.layout_img_list)
        self.layout_pic_tool = QtWidgets.QVBoxLayout()
        self.layout_pic_tool.setSpacing(0)
        self.layout_pic_tool.setObjectName("layout_pic_tool")
        self.win_pic = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.win_pic.sizePolicy().hasHeightForWidth())
        self.win_pic.setSizePolicy(sizePolicy)
        self.win_pic.setScaledContents(True)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.win_pic.setFont(font)
        self.win_pic.setText("")
        self.win_pic.setObjectName("win_pic")
        self.layout_pic_tool.addWidget(self.win_pic)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_view_func_3 = QtWidgets.QPushButton(self.win_main)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.btn_view_func_3.setFont(font)
        self.btn_view_func_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_func_3.setObjectName("btn_view_func_3")
        self.horizontalLayout_6.addWidget(self.btn_view_func_3)
        self.btn_view_func_1 = QtWidgets.QPushButton(self.win_main)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_view_func_1.setFont(font)
        self.btn_view_func_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_func_1.setFlat(False)
        self.btn_view_func_1.setObjectName("btn_view_func_1")
        self.horizontalLayout_6.addWidget(self.btn_view_func_1)
        self.btn_view_func_2 = QtWidgets.QPushButton(self.win_main)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.btn_view_func_2.setFont(font)
        self.btn_view_func_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_func_2.setObjectName("btn_view_func_2")
        self.horizontalLayout_6.addWidget(self.btn_view_func_2)
        self.layout_pic_tool.addLayout(self.horizontalLayout_6)
        self.layout_pic_tool.setStretch(0, 1)
        self.layout_img.addLayout(self.layout_pic_tool)
        self.layout_img.setStretch(0, 2)
        self.layout_img.setStretch(1, 7)
        self.layout_main.addLayout(self.layout_img)
        self.layout_log = QtWidgets.QHBoxLayout()
        self.layout_log.setSpacing(0)
        self.layout_log.setObjectName("layout_log")
        self.ico_log = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico_log.sizePolicy().hasHeightForWidth())
        self.ico_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.ico_log.setFont(font)
        self.ico_log.setText("")
        self.ico_log.setObjectName("ico_log")
        self.layout_log.addWidget(self.ico_log)
        self.lab_log = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_log.sizePolicy().hasHeightForWidth())
        self.lab_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_log.setFont(font)
        self.lab_log.setStyleSheet("")
        self.lab_log.setObjectName("lab_log")
        self.layout_log.addWidget(self.lab_log)
        self.lab_info2 = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_info2.sizePolicy().hasHeightForWidth())
        self.lab_info2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_info2.setFont(font)
        self.lab_info2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lab_info2.setObjectName("lab_info2")
        self.layout_log.addWidget(self.lab_info2)
        self.lab_info3 = QtWidgets.QLabel(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_info3.sizePolicy().hasHeightForWidth())
        self.lab_info3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lab_info3.setFont(font)
        self.lab_info3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lab_info3.setObjectName("lab_info3")
        self.layout_log.addWidget(self.lab_info3)
        self.layout_log.setStretch(0, 10)
        self.layout_log.setStretch(1, 300)
        self.layout_log.setStretch(2, 50)
        self.layout_log.setStretch(3, 50)
        self.layout_main.addLayout(self.layout_log)
        self.win_log = QtWidgets.QTextBrowser(self.win_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.win_log.sizePolicy().hasHeightForWidth())
        self.win_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.win_log.setFont(font)
        self.win_log.setObjectName("win_log")
        self.layout_main.addWidget(self.win_log)
        self.layout_main.setStretch(1, 7)
        self.layout_main.setStretch(3, 4)
        self.horizontalLayout_3.addLayout(self.layout_main)
        MainWindow.setCentralWidget(self.win_main)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.com_brand.activated.connect(self.brand_combobox_manager)
        self.com_model.activated.connect(self.model_combobox_manager)
        self.win_log.textChanged.connect(self.update_log)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lab_list.setText(_translate("MainWindow", "LIST"))
        self.lab_paths.setText(_translate("MainWindow", "PATH"))
        self.lab_log.setText(_translate("MainWindow", "LOG"))
        self.lab_brand.setText(_translate("MainWindow", "BRAND"))
        self.lab_model.setText(_translate("MainWindow", "MODEL"))
        self.lab_grade.setText(_translate("MainWindow", "GRADE"))
        self.lab_info2.setText(_translate("MainWindow", "TOTAL : "))
        self.lab_info3.setText(_translate("MainWindow", "LEFT : "))
        self.btn_view_func_1.setText(_translate("MainWindow", "GRAY"))
        self.btn_view_func_2.setText(_translate("MainWindow", "INVERSE"))
        self.btn_view_func_3.setText(_translate("MainWindow", "DETECT"))

    def add_item(self, item):
        self.listWidget.addItem(item)

    def update_log(self):
        self.win_log.moveCursor(QtGui.QTextCursor.End)

    def brand_combobox_manager(self):
        self.com_grade.clear()
        hyundae_list = ['그랜저', '쏘나타', '싼타페', '아반떼', '스타렉스', '제네시스']
        genesis_list = ['G70', 'G80', 'G90', 'EQ900']
        kia_list = ['카니발', 'K5', '쏘렌토', '모닝', '스포티지', 'K7']
        gmdeawoo_list = ['스파크', '말리부', '크루즈', '올란도', '마티즈', '트렉스']
        runosamsung_list = ['SM3', 'SM5', 'SM6', 'SM7', 'QM3']
        ssangyoung_list = ['렉스턴', '로디우스', '무쏘', '액티언', '이스타나', '체어맨', '카이런', '코란도']

        if self.com_brand.currentText() == '현대':
            self.com_model.clear()
            for r in hyundae_list:
                self.com_model.addItem(r)

        elif self.com_brand.currentText() == '제네시스':
            self.com_model.clear()
            for r in genesis_list:
                self.com_model.addItem(r)

        elif self.com_brand.currentText() == '기아':
            self.com_model.clear()
            for r in kia_list:
                self.com_model.addItem(r)

        elif self.com_brand.currentText() == '쉐보레(GM대우)':
            self.com_model.clear()
            for r in gmdeawoo_list:
                self.com_model.addItem(r)

        elif self.com_brand.currentText() == '르노삼성':
            self.com_model.clear()
            for r in runosamsung_list:
                self.com_model.addItem(r)

        elif self.com_brand.currentText() == '쌍용':
            self.com_model.clear()
            for r in ssangyoung_list:
                self.com_model.addItem(r)

        else:
            self.com_model.clear()

    def model_combobox_manager(self):
        granzer_list = ['그랜저 IG', '그랜저 IG 하이브리드', '그랜저 HG', '그랜저 HG 하이브리드', '더 럭셔리 그랜저', '그랜저 뉴 럭셔리', '그랜저 TG',
                        '뉴 그랜저 XG', '그랜저 XG', '뉴 그랜저', '그랜저']
        sonata_list = ['쏘나타 (DN8)', '쏘나타 뉴 라이즈', '쏘나타 뉴 라이즈 하이브리드', 'LF 쏘나타 하이브리드', 'LF 쏘나타', '쏘나타 더 브릴리언트',
                       'YF 쏘나타', '쏘나타 하이브리드', 'NF 쏘나타 트랜스폼', 'NF 쏘나타', '뉴 EF 쏘나타', 'EF 쏘나타', '쏘나타 III', '쏘나타 II', '쏘나타']
        ssantape_list = ['싼타페 TM', '싼타페 더 프라임', '싼타페 DM', '싼타페 CM', '싼타페']
        abantte_list = ['더 뉴 아반떼 AD', '아반때 AD', '더 뉴 아반떼', '아반떼 쿠페', '아반떼 MD', '아반떼 HD', '아반떼 하이브리드',
                        '뉴 아반떼 XD', '아반떼 XD', '올 뉴 아반떼', '아반떼']
        staraks_list = ['더 뉴 그랜드 스타렉스', '그랜드 스타렉스', '스타렉스 점보', '스타렉스']
        genesis_list = ['제네시스 DH', '제네시스', '더 뉴 제네시스 쿠페', '제네시스 쿠페']

        if self.com_model.currentText() == "그랜저":
            self.com_grade.clear()
            for r in granzer_list:
                self.com_grade.addItem(r)

        elif self.com_model.currentText() == "쏘나타":
            self.com_grade.clear()
            for r in sonata_list:
                self.com_grade.addItem(r)

        elif self.com_model.currentText() == "싼타페":
            self.com_grade.clear()
            for r in ssantape_list:
                self.com_grade.addItem(r)

        elif self.com_model.currentText() == "스타렉스":
            self.com_grade.clear()
            for r in staraks_list:
                self.com_grade.addItem(r)

        elif self.com_model.currentText() == "아반떼":
            self.com_grade.clear()
            for r in abantte_list:
                self.com_grade.addItem(r)

        elif self.com_model.currentText() == "제네시스":
            self.com_grade.clear()
            for r in genesis_list:
                self.com_grade.addItem(r)

        else:
            self.com_grade.clear()
