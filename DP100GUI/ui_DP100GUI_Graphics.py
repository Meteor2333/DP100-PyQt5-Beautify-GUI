# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PersonalDocument\Code\git\DP100\DP100GUI\DP100GUI_Graphics.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogGraphics(object):
    def setupUi(self, DialogGraphics):
        DialogGraphics.setObjectName("DialogGraphics")
        DialogGraphics.setWindowModality(QtCore.Qt.WindowModal)
        DialogGraphics.setEnabled(True)
        DialogGraphics.resize(160, 363)
        DialogGraphics.setMinimumSize(QtCore.QSize(160, 363))
        DialogGraphics.setMaximumSize(QtCore.QSize(160, 363))
        DialogGraphics.setSizeGripEnabled(False)
        DialogGraphics.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogGraphics)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_36 = QtWidgets.QLabel(DialogGraphics)
        self.label_36.setMinimumSize(QtCore.QSize(0, 0))
        self.label_36.setMaximumSize(QtCore.QSize(999, 16777215))
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout.addWidget(self.label_36)
        self.radioAuto = QtWidgets.QRadioButton(DialogGraphics)
        self.radioAuto.setObjectName("radioAuto")
        self.buttonGroup = QtWidgets.QButtonGroup(DialogGraphics)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioAuto)
        self.verticalLayout.addWidget(self.radioAuto)
        self.radioDark = QtWidgets.QRadioButton(DialogGraphics)
        self.radioDark.setChecked(True)
        self.radioDark.setObjectName("radioDark")
        self.buttonGroup.addButton(self.radioDark)
        self.verticalLayout.addWidget(self.radioDark)
        self.radioLight = QtWidgets.QRadioButton(DialogGraphics)
        self.radioLight.setObjectName("radioLight")
        self.buttonGroup.addButton(self.radioLight)
        self.verticalLayout.addWidget(self.radioLight)
        self.label_35 = QtWidgets.QLabel(DialogGraphics)
        self.label_35.setMinimumSize(QtCore.QSize(0, 28))
        self.label_35.setMaximumSize(QtCore.QSize(999, 16777215))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout.addWidget(self.label_35)
        self.spinMaxFps = QtWidgets.QDoubleSpinBox(DialogGraphics)
        self.spinMaxFps.setAlignment(QtCore.Qt.AlignCenter)
        self.spinMaxFps.setDecimals(1)
        self.spinMaxFps.setMinimum(1.0)
        self.spinMaxFps.setMaximum(120.0)
        self.spinMaxFps.setSingleStep(5.0)
        self.spinMaxFps.setProperty("value", 120.0)
        self.spinMaxFps.setObjectName("spinMaxFps")
        self.verticalLayout.addWidget(self.spinMaxFps)
        self.label_37 = QtWidgets.QLabel(DialogGraphics)
        self.label_37.setMinimumSize(QtCore.QSize(0, 28))
        self.label_37.setMaximumSize(QtCore.QSize(999, 16777215))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout.addWidget(self.label_37)
        self.spinDataLength = QtWidgets.QSpinBox(DialogGraphics)
        self.spinDataLength.setAlignment(QtCore.Qt.AlignCenter)
        self.spinDataLength.setMinimum(100)
        self.spinDataLength.setMaximum(10000)
        self.spinDataLength.setSingleStep(100)
        self.spinDataLength.setProperty("value", 500)
        self.spinDataLength.setObjectName("spinDataLength")
        self.verticalLayout.addWidget(self.spinDataLength)
        self.label_38 = QtWidgets.QLabel(DialogGraphics)
        self.label_38.setMinimumSize(QtCore.QSize(0, 28))
        self.label_38.setMaximumSize(QtCore.QSize(999, 16777215))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout.addWidget(self.label_38)
        self.comboFilterK = QtWidgets.QComboBox(DialogGraphics)
        self.comboFilterK.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboFilterK.setEditable(False)
        self.comboFilterK.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboFilterK.setObjectName("comboFilterK")
        self.comboFilterK.addItem("")
        self.comboFilterK.addItem("")
        self.comboFilterK.addItem("")
        self.comboFilterK.addItem("")
        self.comboFilterK.addItem("")
        self.verticalLayout.addWidget(self.comboFilterK)
        self.checkBoxOpenGL = QtWidgets.QCheckBox(DialogGraphics)
        self.checkBoxOpenGL.setChecked(True)
        self.checkBoxOpenGL.setObjectName("checkBoxOpenGL")
        self.verticalLayout.addWidget(self.checkBoxOpenGL)
        self.btnClose = QtWidgets.QPushButton(DialogGraphics)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)

        self.retranslateUi(DialogGraphics)
        self.btnClose.clicked.connect(DialogGraphics.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogGraphics)

    def retranslateUi(self, DialogGraphics):
        _translate = QtCore.QCoreApplication.translate
        DialogGraphics.setWindowTitle(_translate("DialogGraphics", "图形设置"))
        self.label_36.setText(_translate("DialogGraphics", "主题"))
        self.radioDark.setText(_translate("DialogGraphics", "Dark"))
        self.radioAuto.setText(_translate("DialogGraphics", "Auto"))
        self.radioLight.setText(_translate("DialogGraphics", "Light"))
        self.label_35.setText(_translate("DialogGraphics", "最大绘图帧率"))
        self.label_37.setText(_translate("DialogGraphics", "数据点数"))
        self.label_38.setText(_translate("DialogGraphics", "显示滤波系数"))
        self.comboFilterK.setItemText(0, _translate("DialogGraphics", "关"))
        self.comboFilterK.setItemText(1, _translate("DialogGraphics", "低"))
        self.comboFilterK.setItemText(2, _translate("DialogGraphics", "中"))
        self.comboFilterK.setItemText(3, _translate("DialogGraphics", "高"))
        self.comboFilterK.setItemText(4, _translate("DialogGraphics", "极高"))
        self.checkBoxOpenGL.setText(_translate("DialogGraphics", "OpenGL绘图"))
        self.btnClose.setText(_translate("DialogGraphics", "完成"))
