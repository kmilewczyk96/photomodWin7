from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class TipBox(QFrame):
    """
    Custom widget containing two lines of text. Purposed to serve information to the user.
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 38)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        self.info = QLabel()
        self.info.setFixedHeight(18)

        self.details = QLabel()
        self.details.setFixedHeight(18)

        layout.addWidget(self.info)
        layout.addWidget(self.details)
        self.setLayout(layout)

    def clear(self):
        """Clear tip box."""
        self.info.setText('')
        self.details.setText('')
