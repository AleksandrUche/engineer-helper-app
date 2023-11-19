from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_metal_rolling import calculate_mass_sheet
from services.services_widget.services import checking_values, CheckingError, resource_path


class SheetWidget(QWidget):
    """Лист"""

    def __init__(self):
        super().__init__()

        self.resize(590, 385)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.result_field = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.result_field.setFont(font)
        self.result_field.setTextFormat(QtCore.Qt.AutoText)
        self.result_field.setObjectName("result_field")
        self.gridLayout_2.addWidget(self.result_field, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selection_rounding = QtWidgets.QComboBox(self)
        self.selection_rounding.setObjectName("selection_rounding")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.selection_rounding.addItem("")
        self.horizontalLayout_2.addWidget(self.selection_rounding)
        spacer_item = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.button_calculate = QtWidgets.QPushButton(self)
        self.button_calculate.setAutoDefault(True)
        self.button_calculate.setDefault(True)
        self.button_calculate.setObjectName("button_calculate")
        self.gridLayout_2.addWidget(self.button_calculate, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.input_field_s = QtWidgets.QLineEdit(self)
        self.input_field_s.setObjectName("input_field_s")
        self.gridLayout_2.addWidget(self.input_field_s, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.input_field_b = QtWidgets.QLineEdit(self)
        self.input_field_b.setObjectName("input_field_b")
        self.gridLayout_2.addWidget(self.input_field_b, 1, 1, 1, 1)
        self.input_field_a = QtWidgets.QLineEdit(self)
        self.input_field_a.setTabletTracking(True)
        self.input_field_a.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_field_a.setObjectName("input_field_a")
        self.gridLayout_2.addWidget(self.input_field_a, 0, 1, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacer_item1, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 1, 1)
        self.Images = QtWidgets.QLabel(self)
        self.Images.setText("")
        self.Images.setPixmap(QtGui.QPixmap(resource_path("images_metal_rolling/sheet.png")))
        self.Images.setObjectName("Images")
        self.gridLayout.addWidget(self.Images, 2, 1, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item2, 2, 2, 1, 1)
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
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item3, 2, 0, 1, 1)
        spacer_item4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item4, 3, 2, 1, 1)
        self.links_to_elements()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_field_a, self.input_field_b)
        self.setTabOrder(self.input_field_b, self.input_field_s)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.result_field.setText(_translate("Form", "..."))
        self.selection_rounding.setItemText(0, _translate("Form", "1.000"))
        self.selection_rounding.setItemText(1, _translate("Form", "1.00"))
        self.selection_rounding.setItemText(2, _translate("Form", "1.0"))
        self.selection_rounding.setItemText(3, _translate("Form", "1"))
        self.label_6.setText(_translate("Form", "Округление:"))
        self.label_5.setText(_translate("Form", "Масса:"))
        self.button_calculate.setText(_translate("Form", "Рассчитать"))
        self.label_2.setText(_translate("Form", "а, мм:"))
        self.label_3.setText(_translate("Form", "Толщина, мм:"))
        self.label_12.setText(_translate("Form", "b, мм:"))
        self.label.setText(_translate("Form", "Расчет массы листа"))

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
                            self.input_field_b.text(),
                            self.input_field_s.text())
        except CheckingError as e:
            WarningDialogWindow(information_text=str(e))
        else:
            input_field_a = Decimal(self.input_field_a.text())
            input_field_b = Decimal(self.input_field_b.text())
            thickness = Decimal(self.input_field_s.text())

            rounding = self.selection_rounding.currentText()
            result = calculate_mass_sheet(input_field_a, input_field_b, thickness, rounding)
            self.result_field.setText(f'{result} кг')
