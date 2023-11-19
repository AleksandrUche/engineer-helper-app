from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_vesseles import refine_the_pipe
from services.services_widget.services import (checking_values,
                                               CheckingError,
                                               resource_path)


class PipeThinningWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(659, 420)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(size_policy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(size_policy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(size_policy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout_2.addWidget(self.groupBox, 5, 0, 1, 3)
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
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.button_calculate = QtWidgets.QPushButton(self)
        self.button_calculate.setAutoDefault(True)
        self.button_calculate.setDefault(True)
        self.button_calculate.setObjectName("button_calculate")
        self.gridLayout.addWidget(self.button_calculate, 3, 2, 1, 1)
        self.input_field_s_one = QtWidgets.QLineEdit(self)
        self.input_field_s_one.setObjectName("input_field_s_one")
        self.gridLayout.addWidget(self.input_field_s_one, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.result_field = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.result_field.setFont(font)
        self.result_field.setObjectName("result_field")
        self.gridLayout.addWidget(self.result_field, 2, 2, 1, 1)
        self.input_field_s_two = QtWidgets.QLineEdit(self)
        self.input_field_s_two.setObjectName("input_field_s_two")
        self.gridLayout.addWidget(self.input_field_s_two, 1, 2, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 3, 1, 1)
        self.Images = QtWidgets.QLabel(self)
        self.Images.setText("")
        self.Images.setPixmap(QtGui.QPixmap(resource_path("images_vesseles/refine_the_pipe.png")))
        self.Images.setObjectName("Images")
        self.gridLayout_2.addWidget(self.Images, 4, 1, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacer_item1, 4, 0, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacer_item2, 6, 1, 1, 1)
        self.links_to_elements()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_field_s_one, self.input_field_s_two)
        self.setTabOrder(self.input_field_s_two, self.button_calculate)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Информаия"))
        self.label_4.setText(_translate("Form", "S1 - Толщина  патрубка меньшей толщины"))
        self.label_6.setText(_translate("Form", "S2 - Толщина толстого патрубка"))
        self.label.setText(_translate("Form", "Утонение патрубка ГОСТ 34347-2017"))
        self.button_calculate.setText(_translate("Form", "Рассчитать"))
        self.label_2.setText(_translate("Form", "S1, мм:"))
        self.label_3.setText(_translate("Form", "S2, мм:"))
        self.label_5.setText(_translate("Form", "Результат:"))
        self.result_field.setText(_translate("Form", "утонять / не утонять "))

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
            checking_values(self.input_field_s_one.text(),
                            self.input_field_s_two.text())
        except CheckingError as e:
            WarningDialogWindow(information_text=str(e))
        else:
            thin_pipe = Decimal(self.input_field_s_one.text())
            thick_pipe = Decimal(self.input_field_s_two.text())

            result = refine_the_pipe(thin_pipe, thick_pipe)
            if result:
                self.result_field.setText('Утонить')
                self.result_field.setStyleSheet('color: rgb(255,0,0);')
            else:
                self.result_field.setText('Не утонять')
                self.result_field.setStyleSheet('color: rgb(0,0,0);')
