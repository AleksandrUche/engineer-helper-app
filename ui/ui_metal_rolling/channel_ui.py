from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_metal_rolling import calculate_mass_channel
from services.services_widget.services import (
    checking_values,
    CheckingError,
    check_units_measure_length,
)


class ChannelWidget(QWidget):
    """Швеллеры"""

    def __init__(self):
        super().__init__()

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
                            self.input_field_length.text())
        except CheckingError as e:
            WarningDialogWindow(information_text=str(e))
        else:
            # type_channel =
            # name =
            length = check_units_measure_length(self.input_field_length.text(),
                                                self.radio_millimeters.isChecked())
            rounding = self.selection_rounding.currentText()
            result = calculate_mass_channel()
            self.result_field.setText(f'{result} кг')
