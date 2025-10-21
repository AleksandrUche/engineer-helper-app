from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_vesseles import circumference
from services.services_widget.services import (
    checking_values,
    CheckingError,
    round_the_number,
    resource_path,
)


class CircumferenceWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(607, 385)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        self.Images = QtWidgets.QLabel(self)
        self.Images.setText("")
        self.Images.setPixmap(
            QtGui.QPixmap(resource_path("images_vesseles/circumference.png")))
        self.Images.setObjectName("Images")
        self.gridLayout_2.addWidget(self.Images, 4, 0, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacer_item, 5, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.input_field_radius = QtWidgets.QLineEdit(self)
        self.input_field_radius.setObjectName("input_field_radius")
        self.gridLayout.addWidget(self.input_field_radius, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.result_field_millimeters = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.result_field_millimeters.setFont(font)
        self.result_field_millimeters.setObjectName("result_field_millimeters")
        self.gridLayout.addWidget(self.result_field_millimeters, 1, 2, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item1, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.button_calculate = QtWidgets.QPushButton(self)
        self.button_calculate.setAutoDefault(True)
        self.button_calculate.setDefault(True)
        self.button_calculate.setObjectName("button_calculate")
        self.gridLayout.addWidget(self.button_calculate, 4, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.selection_rounding = QtWidgets.QComboBox(self)
        self.selection_rounding.setObjectName("selection_rounding")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.horizontalLayout_3.addWidget(self.selection_rounding)
        spacer_item2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacer_item2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)
        self.result_field_meters = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.result_field_meters.setFont(font)
        self.result_field_meters.setObjectName("result_field_meters")
        self.gridLayout.addWidget(self.result_field_meters, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 1, 1, 1)
        self.links_to_elements()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_field_radius, self.selection_rounding)
        self.setTabOrder(self.selection_rounding, self.button_calculate)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Длина окружности"))
        self.label_2.setText(_translate("Form", "Диаметр D, мм:"))
        self.label_7.setText(_translate("Form", "метры :"))
        self.result_field_millimeters.setText(_translate("Form", "..."))
        self.label_5.setText(_translate("Form", "мм :"))
        self.button_calculate.setText(_translate("Form", "Рассчитать"))
        self.label_6.setText(_translate("Form", "Округление:"))
        self.selection_rounding.setItemText(0, _translate("Form", "1.000"))
        self.selection_rounding.setItemText(1, _translate("Form", "1.00"))
        self.selection_rounding.setItemText(2, _translate("Form", "1.0"))
        self.selection_rounding.setItemText(3, _translate("Form", "1"))
        self.result_field_meters.setText(_translate("Form", "..."))

    def links_to_elements(self):
        self.button_calculate.clicked.connect(self.calculate)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.calculate()
        elif event.key() == Qt.Key_Enter:
            self.calculate()
        elif event.key() == Qt.Key_Down:
            self.focusNextChild()

    def calculate(self):
        try:
            checking_values(self.input_field_radius.text())
        except CheckingError as e:
            WarningDialogWindow(information_text=str(e))
        else:
            diameter = Decimal(self.input_field_radius.text())
            rounding = self.selection_rounding.currentText()

            result = circumference(diameter, rounding)
            result_meters = round_the_number(result / 1000, rounding)

            self.result_field_millimeters.setText(f'{result} мм')
            self.result_field_meters.setText(f'{result_meters} м')
