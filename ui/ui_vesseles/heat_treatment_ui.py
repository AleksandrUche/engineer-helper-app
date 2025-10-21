from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_vesseles import heat_treatment
from services.services_widget.services import (
    checking_values,
    CheckingError,
    resource_path,
)


class ThermalTreatmentWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(595, 385)
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
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.button_calculate = QtWidgets.QPushButton(self)
        self.button_calculate.setAutoDefault(True)
        self.button_calculate.setDefault(True)
        self.button_calculate.setObjectName("button_calculate")
        self.gridLayout.addWidget(self.button_calculate, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.result_field = QtWidgets.QLabel(self)
        self.result_field.setObjectName("result_field")
        self.gridLayout.addWidget(self.result_field, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.input_field_d = QtWidgets.QLineEdit(self)
        self.input_field_d.setObjectName("input_field_d")
        self.gridLayout.addWidget(self.input_field_d, 0, 2, 1, 1)
        self.input_field_s = QtWidgets.QLineEdit(self)
        self.input_field_s.setObjectName("input_field_s")
        self.gridLayout.addWidget(self.input_field_s, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item, 6, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 1, 1, 1)
        self.Images = QtWidgets.QLabel(self)
        self.Images.setText("")
        self.Images.setPixmap(QtGui.QPixmap(resource_path("images_vesseles/shell.png")))
        self.Images.setObjectName("Images")
        self.gridLayout_2.addWidget(self.Images, 4, 0, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacer_item1, 5, 1, 1, 1)
        self.links_to_elements()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_field_d, self.input_field_s)
        self.setTabOrder(self.input_field_s, self.button_calculate)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Термообработка обечайки"))
        self.button_calculate.setText(_translate("Form", "Рассчитать"))
        self.label_5.setText(_translate("Form", "Результат:"))
        self.result_field.setText(_translate("Form", "Термообрабатывать / НЕ термообрабатывать"))
        self.label_3.setText(_translate("Form", "Толщина S, мм:"))
        self.label_2.setText(_translate("Form", "Диаметр D, мм:"))

    def links_to_elements(self):
        self.button_calculate.clicked.connect(self.calculate_mass)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.calculate_mass()
        elif event.key() == Qt.Key_Enter:
            self.calculate_mass()
        elif event.key() == Qt.Key_Down:
            self.focusNextChild()

    def calculate_mass(self):
        try:
            checking_values(self.input_field_d.text(),
                            self.input_field_s.text())
        except CheckingError as e:
            WarningDialogWindow(information_text=str(e))
        else:
            diameter = Decimal(self.input_field_d.text())
            thickness = Decimal(self.input_field_s.text())

            result = heat_treatment(diameter, thickness)
            if result:
                self.result_field.setText('Термообработать')
                self.result_field.setStyleSheet('color: rgb(255,0,0);')
            else:
                self.result_field.setText('Не термообрабатывать')
                self.result_field.setStyleSheet('color: rgb(0,0,0);')
