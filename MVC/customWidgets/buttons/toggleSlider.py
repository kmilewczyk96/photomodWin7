from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox


class ToggleSlider(QCheckBox):
    """Custom QCheckBox."""
    def __init__(self, label: str, parent=None):
        super().__init__(label, parent=parent)
        self.setProperty('class', 'toggle-slider')
        self.setCursor(Qt.CursorShape.PointingHandCursor)
