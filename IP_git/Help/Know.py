# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Know.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 609)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgba(0, 52, 48, 250);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_2:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_5:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_8:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_11.setStyleSheet("#pushButton_11{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_11:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(230, 231, 197);")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(230, 231, 197);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(230, 231, 197);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_4.addWidget(self.textBrowser_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(230, 231, 197);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_5.addWidget(self.textBrowser_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(230, 231, 197);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_6.addWidget(self.textBrowser_5)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "了解IP核"))
        self.pushButton.setText(_translate("MainWindow", "了解哈希函数算子"))
        self.pushButton_5.setText(_translate("MainWindow", "了解随机数生成"))
        self.pushButton_8.setText(_translate("MainWindow", "了解大数运算单元"))
        self.pushButton_11.setText(_translate("MainWindow", "了解椭圆曲线算子"))
        self.label.setText(_translate("MainWindow", "了解IP核"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.IP核概述</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核，全称知识产权核（英语：</span><span style=\" font-size:12pt;\">Semiconductor intellectual property core</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">），是在集成电路的可重用设计方法学中，指某一方提供的、形式为逻辑单元、芯片设计的可重用模组。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核可以授权给另一方，也可以由一方拥有和使用。</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">该术语来自设计中存在的专利或源代码版权的许可。</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">专用集成电路和现场可编程门阵列逻辑系统的设计人员可以使用</span><span style=\" font-size:12pt;\"> IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核作为构建块。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">随着芯片复杂度提升，不同芯片模块形成不同组合应用于不同的终端应用场景，又将形成新的</span><span style=\" font-size:12pt;\"> IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核。计算机基于冯诺依曼架构，由运算、控制、存储、输入、输出五大功能模块组成。芯片内部底层功能按照上述模块化划分包括数学运算</span><span style=\" font-size:12pt;\"> IP(</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">浮点、整数、逻辑运算等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、存储器</span><span style=\" font-size:12pt;\"> IP(LPM</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">ROM</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">RAM</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">FIFO</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">FLASH </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、数字信号处理</span><span style=\" font-size:12pt;\"> IP(FIR</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">CIC</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">NCO</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、</span><span style=\" font-size:12pt;\">FFT </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、数字通信</span><span style=\" font-size:12pt;\"> IP(</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">编译器、编码器等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、视频和图像处理</span><span style=\" font-size:12pt;\"> IP(</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">接口、滤波器、混合器、采样器等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、输入</span><span style=\" font-size:12pt;\">/</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">输出</span><span style=\" font-size:12pt;\"> IP(</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">时钟控制、锁相环、收发器等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，接口</span><span style=\" font-size:12pt;\"> IP(ASI</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，以太网</span><span style=\" font-size:12pt;\"> IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，</span><span style=\" font-size:12pt;\">PCI </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">编译器等</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，调试</span><span style=\" font-size:12pt;\"> IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核等等。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">内核产品的广度令人震惊。它包括处理器、</span><span style=\" font-size:12pt;\">DSP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、通信、接口、内存、音频、视频、控制和安全</span><span style=\" font-size:12pt;\"> IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，范围广泛，从简单的设备（如计数器）一直到复杂的设备（如</span><span style=\" font-size:12pt;\"> 32 </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">位定制软处理器）。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.IP核背景 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">的由来要从早期的芯片设计过程讲起。早期芯片的集成规模有限，设计复杂度不高，芯片上所有的电路都是由芯片设计者自主完成。设计水平不高、能力有限的芯片公司只能设计规模小的简单的芯片。设计水平高、能力强的芯片公司才可以设计规模大、功能复杂的芯片。这个时期，不论芯片规模大还是小，芯片从“头”到“脚”都是由芯片公司自己设计的。早期的高端芯片基本上都是由为数不多的大型国际芯片公司把持。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">随着现代信息社会对芯片要求提升，芯片的规模呈指数性增加，复杂性急剧增大。中小型芯片公司要独立完成一款复杂芯片设计几乎变得不太可能。特别是</span><span style=\" font-size:12pt;\">20</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">世纪</span><span style=\" font-size:12pt;\">80</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">年代末，芯片行业出现了晶圆代工</span><span style=\" font-size:12pt;\">(Foundry)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">商业模式，大批的中小微芯片设计公司</span><span style=\" font-size:12pt;\">(Fabless)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">应运而生。这个时期，芯片设计行业急需解决小芯片公司无法设计大芯片的难题。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">解决这一难题的启发思路很多。例如：搭积木和拼图画玩具；由标准件设计大型机器；由软件子程序</span><span style=\" font-size:12pt;\">(</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">或者中间件</span><span style=\" font-size:12pt;\">)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">调用设计大型软件；用芯片搭建大型电子系统等。思路都是重复使用预先设计好的成熟的构件来搭建更复杂的系统，省掉对构件内部问题的考虑，化繁为简；重复使用构件，减少重复劳动，节省时间；重复使用构件，提高整个复杂系统搭建的成功率。</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">芯片设计行业中的</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核开发和</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">复用，就是在这些思路启发下形成的。</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核就类似于上述的构件。</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核是预先设计好的具有独立功能的电路模块设计。有了</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核这种构件，大的复杂的芯片设计就变得较容易、周期短、易成功。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.IP核分类</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核模块分为软核（</span><span style=\" font-size:12pt;\">Soft IP Core</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）、完成结构描述的固核（</span><span style=\" font-size:12pt;\">Firm IP Core</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）和基于物理</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">描述并经过工艺验证的硬核（</span><span style=\" font-size:12pt;\">Hard IP Core</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">三种类型的</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核各有优缺点，用户会根据自己的实际需要来选择。以下是三种</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核的优缺点简要总结。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">软核：它以综合源代码的形式交付给用户，其优点是源代码灵活，在功能一级可以重新配置，可以灵活选择目标制造工艺。灵活性高、可移植性强，允许用户自配置。其缺点是对电路功能模块的预测性较差，在后续设计中存在发生错误的可能性，有一定的设计风险。并且</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">软核的知识产权保护难度较大。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">固核：它的灵活性和成功率介于</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">软核和</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">硬核之间，是一种折中的类型。和</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">软核相比，</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">固核的设计灵活性稍差，但在可靠性上有较大提高。目前，</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">固核是</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核的主流形式之一。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">硬核：它的最大优点是确保性能，如速度、功耗等达到预期效果。然而，</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">硬核与制造工艺相关，难以转移到新的工艺或者集成到新的结构中去，是不可以重新配置的。</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">硬核不许修改的特点使其复用有一定的困难，因此只能用于某些特定应用，使用范围较窄。但</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">硬核的知识产权保护最为方便。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核的举例，最典型有</span><span style=\" font-size:12pt;\"> ARM </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">公司的各种类型的</span><span style=\" font-size:12pt;\">CPU IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核。许多</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">供应商提供的</span><span style=\" font-size:12pt;\">DSP IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核、</span><span style=\" font-size:12pt;\">USB IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核、</span><span style=\" font-size:12pt;\">PCI-X IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核、</span><span style=\" font-size:12pt;\">WiFi IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核、以太网</span><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核、嵌入式存储器</span><span style=\" font-size:12pt;\">IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核等，五花八门，品种十分繁多。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">如果按大类分，大体上可分为处理器和微控制器类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、存储器类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、外设及接口类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、模拟和混合电路类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、通信类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、图像和媒体类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">等。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">全球大的</span><span style=\" font-size:12pt;\"> EDA </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">供应商中，有些也是</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">供应商。例如美国新思科技</span><span style=\" font-size:12pt;\">(Synopsys)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">可提供上千种各类</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">。涵盖逻辑电路</span><span style=\" font-size:12pt;\">(Logic Libraries)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、嵌入式存储器</span><span style=\" font-size:12pt;\">(Embedded Memories)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、模拟电路</span><span style=\" font-size:12pt;\">(Analog Libraries)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、有线和无线通信接口</span><span style=\" font-size:12pt;\">(Wired and Wireless Interface)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、安全</span><span style=\" font-size:12pt;\">(Security)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">、嵌入式处理器</span><span style=\" font-size:12pt;\">(Embedded Processors) </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">和子系统</span><span style=\" font-size:12pt;\">(Subsystems)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">等方面的</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">芯片设计公司可以根据自身需求，向</span><span style=\" font-size:12pt;\"> IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">供应商采购不同的</span><span style=\" font-size:12pt;\"> IP </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核，如可采购软核进行自定义整合设计，也可以直接采购具备电</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">路布局的硬核实现更快速的芯片设计定型与量产。</span><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "了解IP核"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">哈希函数是把任意长度的输入（又叫做预映射</span><span style=\" font-size:12pt;\">pre-image</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）通过散列算法变换成固定长度的输出，该输出就是散列值或哈希值（</span><span style=\" font-size:12pt;\">hash value</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）。这种转换是一种压缩映射，也就是，散列值的空间通常远小于输入的空间，不同的输入可能会散列成相同的输出，所以不可能从散列值来确定唯一的输入值。简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">在密码学领域，哈希函数又被称为单向散列函数，哈希函数输出的哈希值很难找到逆向规律，所以在安全加速引擎</span><span style=\" font-size:12pt;\">IP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">核中，哈希函数可以用来：消息认证码（</span><span style=\" font-size:12pt;\">MAC</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）生成、数字签名、密码存储和验证、安全摘要生成。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">对于密码安全的哈希函数，要求其具有以下六个附加属性：</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">（1）</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">抗第二原像攻击（弱抗碰撞性）：给定一个任意的输入</span><span style=\" font-size:12pt;\">M</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，很难找到另一个输入</span><span style=\" font-size:12pt;\">M\'</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">（</span><span style=\" font-size:12pt;\">M </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">≠</span><span style=\" font-size:12pt;\"> M</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">），使得</span><span style=\" font-size:12pt;\">H(M) =  H(M’)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">（2）</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">强抗碰撞性：当两个不同的输入产生相同的输出时，会发生碰撞。如果没有人可以发现碰撞，哈希函数</span><span style=\" font-size:12pt;\">H</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">（</span><span style=\" font-size:12pt;\">x</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）则具有抗碰撞性，即：找到两个不同的输入M和M\'(M≠M’)，使得H(M)=H(M’)是计算不可行的，这里的“计算不可行(困难)”是在计算的复杂性角度所给出的概念。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">（3）</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">隐匿性（单向性）：隐匿属性声明如果我们给出</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">hash</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">函数</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">y= H</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">（</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">x</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）的输出，则没有可行的方法来确定输入</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">x</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">是什么。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">（4）</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">谜题友好性：对于每个可能的</span><span style=\" font-size:12pt;\">n</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">位输出值</span><span style=\" font-size:12pt;\">y</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，如果从具有高最小熵的分布中选择</span><span style=\" font-size:12pt;\">k</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，则不可能找到</span><span style=\" font-size:12pt;\">x</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">使得</span><span style=\" font-size:12pt;\">H</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">（</span><span style=\" font-size:12pt;\">k||x</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">） </span><span style=\" font-size:12pt;\">= y</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，即几乎不可能通过随机的方式找到另一个值</span><span style=\" font-size:12pt;\">x</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，使之与给定</span><span style=\" font-size:12pt;\">k</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">的哈希值一样。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">（</span><span style=\" font-size:12pt;\">5</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）压缩性：哈希函数的输入是任意长度的，输出是固定长度的。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">（</span><span style=\" font-size:12pt;\">6</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）容易计算：通过任意给定的</span><span style=\" font-size:12pt;\">M</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，计算出</span><span style=\" font-size:12pt;\">H(M)</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">是容易的。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "了解哈希函数算子"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">解决信息安全的关键技术是密码学中的加密技术和解密技术。加密技术和解密技术的核心是密钥，密钥有安全等级比较高的，也有安全等级比较低的，随机数的随机性决定了密钥的可靠性。随机数的随机性越好，密钥越不容易被破解，反之，容易被破解；随机数发生器有真随机和伪随机之分。对于一些对安全性要求不太高的信息，可以使用伪随机数发生器产生的随机数作为密钥；而对于安全级别要求高的信息，就需要真随机数发生器生成随机数了，以这样的随机数作为密钥，信息就会更加安全。原因在于真随机数发生器不能预测下一次的输出，所以生成的随机数的随机性比较高；伪随机数发生器能预测下一次的输出，故生成的随机数的随机性比较低，仅适用于一些对于安全等级要求不高的场景。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.真随机数生成</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">真随机数发生器是利用物理过程的随机噪声作为熵源，如热力学噪声、闪烁噪声等。这些物理过程具有统计学随机特性；然后用比较器，</span><span style=\" font-size:12pt;\">D</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">触发器等进行随机数提取；最后将提取的随机数进行后处理再输出；所以生成的随机数的随机性要比伪随机数发生器生成的随机数的随机性好，这样的数据是不能预测的，并且真随机数发生器还可以添加后处理模块来提高生成随机数的随机性。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.伪随机数生成</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">伪随机数发生器是以数学算法为基础，然后根据算法，通过一系列种子值计算出来的随机数，想要生成一个真正的随机数，对于计算机来说基本不可能。伪随机数发生器生成的随机数只能说近似随机，只要知道了初始值，然后根据公式，就可以推算出接下来生成的数据，这是可以预测的。</span><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "了解随机数生成"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">针对不同的数据类型，计算机会分配大小不同的存储空间，但是计算机中存储空间的大小是固定的，数据位数少的数据可以正常存储和计算，数据位数较多时，计算机进行存储和计算就会出现差错．</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">例如两个二十位的数据做乘法，乘积位数较多，任何数据类型都无法处理。本系统主要通过加、减、乘三种运算，来实现大数运算的算法。大体来说，计算机对数据的处理主要是存储和计算两个部分，计算机在对位数较多的数据进行处理时，首先要解决存储的问题，数据存储是运算的前提。数据存储的基本思想是将数据以字符类型输入，并存储到数组中，同时按照先低位后高位的运算习惯，将其逆序存放，达到低位在前，高位在后的效果，为后面的逐位运算做好基础。</span><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "了解大数运算单元"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">椭圆曲线算子（</span><span style=\" font-size:12pt;\">Elliptic Curve Operator</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）是在椭圆曲线密码学中使用的一种操作，用于实现基于椭圆曲线的加密和数字签名算法，是基于椭圆曲线数学理论实现的一种非对称加密算法。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">椭圆曲线密码学是一种现代的公钥密码学体系，其安全性基于椭圆曲线上的离散对数问题。在该密码学中，椭圆曲线算子涉及两个主要操作：点加法和点乘法。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">（1） </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">点加法（</span><span style=\" font-size:12pt;\">Point Addition</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">在椭圆曲线上，可以定义两个点的相加操作。点加法中的主要运算是通过利用椭圆曲线的几何性质，将两点的切线与椭圆曲线的交点进行计算，然后将结果反射得到相加后的点。点加法操作使得椭圆曲线上的点集成为一个阿贝尔群。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">（2） </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">点乘法（</span><span style=\" font-size:12pt;\">Point Multiplication</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">）</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">点乘法是对一个椭圆曲线上的点进行重复相加操作的运算。具体而言，对于给定的点</span><span style=\" font-size:12pt;\">P</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">和一个整数</span><span style=\" font-size:12pt;\">n</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，点乘法通过将</span><span style=\" font-size:12pt;\">P</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">与自身相加</span><span style=\" font-size:12pt;\">n</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">次来计算</span><span style=\" font-size:12pt;\">nP</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">。这个操作可以用于生成公钥和私钥之间的关联，以及进行数字签名和密钥交换等密码学操作。</span><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "了解椭圆曲线算子"))
