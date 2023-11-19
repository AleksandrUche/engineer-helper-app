from PyQt5.QtWidgets import QStackedWidget

from widgets.widget_metal_rolling.corner_equal_widget import CornerEqualWidget
from widgets.widget_metal_rolling.сorner_different_widget import CornerDifferentWidget
from widgets.widget_metal_rolling.сircle_widget import CircleWidget
from widgets.widget_metal_rolling.square_widget import SquareWidget
from widgets.widget_metal_rolling.sheet_widget import SheetWidget
from widgets.widget_metal_rolling.tube_widget import TubeWidget
from widgets.widget_metal_rolling.profile_pipe_widget import ProfilePipeWidget
from widgets.widget_vesseles.heat_treatment_widget import ThermalTreatmentWidget
from widgets.widget_vesseles.pipe_thinning_widget import PipeThinningWidget
from widgets.widget_vesseles.expand_shell_widget import ExpandShellWidget
from widgets.widget_vesseles.arc_length_widget import ArcLengthWidget
from widgets.widget_vesseles.circumference_widget import CircumferenceWidget
from widgets.widget_vesseles.arc_size_widget import ArcSizeWidget
from widgets.widget_vesseles.ring_weight_widget import RingWeightWidget


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
