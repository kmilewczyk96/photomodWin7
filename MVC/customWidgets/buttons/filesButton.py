from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton


class FilesPushButton(QPushButton):
    """
    Customized QPushButton simulating QRadio button 'Checked' state.
    Its purpose is to be checked once and never change the state afterwards.
    """
    def __init__(self, label: str, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(26)
        self.setText(label)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty('class', 'fileBtn')
        self._setInitialStyle()
        self.altered = False

    def pseudoCheck(self):
        """Create effect of button being checked/enabled."""
        if not self.altered:
            self.setStyleSheet(
                """
                .fileBtn {
                    color: #087f5b;
                    background-color: #63e6be;
                    border: 1px solid #087f5b;
                    border-radius: 3;
                    padding: 0 12;
                }
                .fileBtn:hover {
                    color: #087f5b;
                    background-color: #38d9a9;
                }
                """
            )

            self.altered = True

    def _setInitialStyle(self):
        self.setStyleSheet(
            """
            .fileBtn {
                color: #495057;
                background-color: #dee2e6;
                border: 1px solid #343a40;
                border-radius: 3;
            }
            .fileBtn:hover {
                color: #212529;
                background-color: #adb5bd;
            }
            """
        )
