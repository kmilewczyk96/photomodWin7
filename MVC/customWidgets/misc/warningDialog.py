from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class WarningDialog(QDialog):
    def __init__(self, parent, warningList, labelText: str):
        super().__init__(parent=parent)
        self.warningList = warningList
        self.labelText = labelText
        self.setMinimumWidth(350)
        self._setWindowPersonalization()
        self.setWindowIcon(QIcon('resources/icons/warning.ico'))
        self.setWindowTitle('Operacja nie może zostać wykonana!')
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self._createContent()

    def _setWindowPersonalization(self):
        self.setProperty('class', 'warningDialog')
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, False)

    def show(self) -> None:
        self.exec()

    def _createContent(self):
        labelTip = QLabel(self.labelText)
        labelTip.setProperty('class', 'warningMessage')
        self.layout().addWidget(labelTip)
        if self.warningList:
            self.layout().addWidget(self.warningList)
        self.errorBtn = QPushButton('ZAMKNIJ')
        self.errorBtn.setProperty('class', 'warningBtn')
        self.errorBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout().addWidget(self.errorBtn)