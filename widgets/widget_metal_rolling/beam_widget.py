from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dialogs.warning_dialog.warning import WarningDialogWindow
from services.services_widget.calculators_metal_rolling import calculate_mass_corner_equal
from services.services_widget.services import (checking_values,
                                               CheckingError,
                                               check_units_measure_length)

class BeamWidget(QWidget):
    """Швеллеры"""
    def __init__(self):
        super().__init__()

        # type_channel =
        # name =
        # length =