from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from services.services_widget.services import resource_path


class WarningDialogWindow(QMessageBox):
    """Диалоговое окно вызываемое при вводе невалидных данных"""
    def __init__(self,
                 error_text='Попробуйте еще раз. Если ошибка не исчезает, пожалуйста, \n '
                            'сообщите об этом в службу поддержки.',
                 information_text='',
                 detail_text=''):
        super().__init__()
        self.setWindowIcon(QIcon(resource_path('icon/icon.ico')))
        self.setWindowTitle('Ошибка')
        self.setText(error_text)  # Текст ошибки
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)
        self.setInformativeText(information_text)  # Информационный текст
        self.setDetailedText(detail_text)  # Детальный текст
        self.exec_()