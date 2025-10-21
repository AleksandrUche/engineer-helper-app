from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_metal_rolling import calculate_mass_square
from services.services_widget.services import (
    checking_values,
    CheckingError,
    check_units_measure_length,
    resource_path,
)


class SquareWidget(QWidget):
    """Квадрат"""

    def __init__(self):
        super().__init__()

        self.resize(590, 385)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.Images = QtWidgets.QLabel(self)
        self.Images.setText("")
        self.Images.setPixmap(QtGui.QPixmap(resource_path("images_metal_rolling/square.png")))
        self.Images.setObjectName("Images")
        self.gridLayout.addWidget(self.Images, 2, 1, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item, 4, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_millimeters = QtWidgets.QRadioButton(self)
        self.radio_millimeters.setTabletTracking(False)
        self.radio_millimeters.setCheckable(True)
        self.radio_millimeters.setChecked(True)
        self.radio_millimeters.setAutoRepeat(False)
        self.radio_millimeters.setObjectName("radio_millimeters")
        self.horizontalLayout.addWidget(self.radio_millimeters)
        self.radio_meters = QtWidgets.QRadioButton(self)
        self.radio_meters.setObjectName("radio_meters")
        self.horizontalLayout.addWidget(self.radio_meters)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.selection_rounding = QtWidgets.QComboBox(self)
        self.selection_rounding.setObjectName("selection_rounding")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.horizontalLayout_2.addWidget(self.selection_rounding)
        spacer_item2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.result_field = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.result_field.setFont(font)
        self.result_field.setTextFormat(QtCore.Qt.AutoText)
        self.result_field.setObjectName("result_field")
        self.gridLayout_2.addWidget(self.result_field, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.button_calculate = QtWidgets.QPushButton(self)
        self.button_calculate.setAutoDefault(True)
        self.button_calculate.setDefault(True)
        self.button_calculate.setObjectName("button_calculate")
        self.gridLayout_2.addWidget(self.button_calculate, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.input_field_length = QtWidgets.QLineEdit(self)
        self.input_field_length.setObjectName("input_field_length")
        self.gridLayout_2.addWidget(self.input_field_length, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.input_field_a = QtWidgets.QLineEdit(self)
        self.input_field_a.setTabletTracking(True)
        self.input_field_a.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_field_a.setObjectName("input_field_a")
        self.gridLayout_2.addWidget(self.input_field_a, 0, 1, 1, 1)
        spacer_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacer_item3, 8, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 2, 1)
        spacer_item4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item4, 2, 0, 1, 1)
        spacer_item5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item5, 2, 2, 1, 1)
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
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.links_to_elements()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_field_a, self.input_field_length)
        self.setTabOrder(self.input_field_length, self.radio_millimeters)
        self.setTabOrder(self.radio_millimeters, self.radio_meters)
        self.setTabOrder(self.radio_meters, self.selection_rounding)
        self.setTabOrder(self.selection_rounding, self.button_calculate)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.radio_millimeters.setText(_translate("Form", "мм"))
        self.radio_meters.setText(_translate("Form", "метры"))
        self.label_6.setText(_translate("Form", "Округление:"))
        self.selection_rounding.setItemText(0, _translate("Form", "1.000"))
        self.selection_rounding.setItemText(1, _translate("Form", "1.00"))
        self.selection_rounding.setItemText(2, _translate("Form", "1.0"))
        self.selection_rounding.setItemText(3, _translate("Form", "1"))
        self.result_field.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "a, мм:"))
        self.button_calculate.setText(_translate("Form", "Рассчитать"))
        self.label_5.setText(_translate("Form", "Масса:"))
        self.label_4.setText(_translate("Form", "Длина:"))
        self.label.setText(_translate("Form", "Расчет массы квадрата"))

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
            checking_values(self.input_field_a.text(),
                            self.input_field_length.text())
        except CheckingError as e:
            WarningDialogWindow(information_text=str(e))
        else:
            size = Decimal(self.input_field_a.text())
            length = check_units_measure_length(self.input_field_length.text(),
                                                self.radio_millimeters.isChecked())
            rounding = self.selection_rounding.currentText()

            result = calculate_mass_square(size, length, rounding)
            self.result_field.setText(f'{result} кг')
