from PyQt5.QtWidgets import QStackedWidget

from ui.ui_metal_rolling.corner_equal_ui import CornerEqualWidget
from ui.ui_metal_rolling.сorner_different_ui import CornerDifferentWidget
from ui.ui_metal_rolling.сircle_ui import CircleWidget
from ui.ui_metal_rolling.square_ui import SquareWidget
from ui.ui_metal_rolling.sheet_ui import SheetWidget
from ui.ui_metal_rolling.tube_ui import TubeWidget
from ui.ui_metal_rolling.profile_pipe_ui import ProfilePipeWidget
from ui.ui_vesseles.heat_treatment_ui import ThermalTreatmentWidget
from ui.ui_vesseles.pipe_thinning_ui import PipeThinningWidget
from ui.ui_vesseles.expand_shell_ui import ExpandShellWidget
from ui.ui_vesseles.arc_length_ui import ArcLengthWidget
from ui.ui_vesseles.circumference_ui import CircumferenceWidget
from ui.ui_vesseles.arc_size_ui import ArcSizeWidget
from ui.ui_vesseles.ring_weight_ui import RingWeightWidget


class MainStackWidget(QStackedWidget):
    """Конструктор виджета"""
    def __init__(self):
        super().__init__()
        self.adding_widgets()

    def adding_widgets(self):
        # Металлопрокат
        self.addWidget(CornerEqualWidget())  # 0
        self.addWidget(CornerDifferentWidget())  # 1
        self.addWidget(CircleWidget())  # 2
        self.addWidget(SquareWidget())  # 3
        self.addWidget(SheetWidget())  # 4
        self.addWidget(TubeWidget())  # 5
        self.addWidget(ProfilePipeWidget())  # 6
        # Сосуды
        self.addWidget(ThermalTreatmentWidget())  # 7
        self.addWidget(PipeThinningWidget())  # 8
        self.addWidget(ExpandShellWidget())  # 9
        self.addWidget(ArcLengthWidget())  # 10
        self.addWidget(CircumferenceWidget())  # 11
        self.addWidget(ArcSizeWidget())  # 12
        self.addWidget(RingWeightWidget())  # 13

    def select_widget(self, widget_number: int) -> None:
        """Выбор виджета"""
        self.setCurrentIndex(widget_number)
