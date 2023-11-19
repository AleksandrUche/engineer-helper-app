import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout

# Локальные
from menu.menu_bar import MainMenuBar
from services.services_widget.services import resource_path
from widgets.main_widget import MainStackWidget


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self):
        super().__init__()
        # Базовые настройки
        self.setWindowIcon(QIcon(resource_path('icon/icon.ico')))
        self.setWindowTitle('Engineer helper 1.0.1')
        self.resize(600, 400)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.menu_bar = MainMenuBar()  # Меню бар
        self.setMenuBar(self.menu_bar)

        self.widget = MainStackWidget()  # Виджеты
        hbox = QHBoxLayout(self.centralWidget)
        hbox.addWidget(self.widget)
        self.trigger_menu_metal_rolling()  # Триггеры
        self.trigger_menu_vesseles()

    def trigger_menu_metal_rolling(self):
        self.menu_bar.corner_equal_shelves_item.triggered.connect(lambda: self.widget.select_widget(0))
        self.menu_bar.corner_different_shelves_item.triggered.connect(lambda: self.widget.select_widget(1))
        self.menu_bar.circle_item.triggered.connect(lambda: self.widget.select_widget(2))
        self.menu_bar.square_item.triggered.connect(lambda: self.widget.select_widget(3))
        self.menu_bar.sheet_item.triggered.connect(lambda: self.widget.select_widget(4))
        self.menu_bar.tube_item.triggered.connect(lambda: self.widget.select_widget(5))
        self.menu_bar.profile_pipe_item.triggered.connect(lambda: self.widget.select_widget(6))

    def trigger_menu_vesseles(self):
        self.menu_bar.thermal_treatment.triggered.connect(lambda: self.widget.select_widget(7))
        self.menu_bar.pipe_thinning_item.triggered.connect(lambda: self.widget.select_widget(8))
        self.menu_bar.shell_reamers_item.triggered.connect(lambda: self.widget.select_widget(9))
        self.menu_bar.arc_length_item.triggered.connect(lambda: self.widget.select_widget(10))
        self.menu_bar.circumference_item.triggered.connect(lambda: self.widget.select_widget(11))
        self.menu_bar.arc_size_item.triggered.connect(lambda: self.widget.select_widget(12))
        self.menu_bar.ring_weight.triggered.connect(lambda: self.widget.select_widget(13))


def application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
