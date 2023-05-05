# HELP DIALOG WINDOW
# ===================

# LIBRARIES AND MODULES
from PyQt5 import QtWidgets as QW # UI elements' functionality
from PyQt5.uic import loadUi # Read the UI file

# CLASS DEFINITION
class OpenHelp(QW.QDialog):
    def __init__(self):
        super().__init__()

        loadUi('instructions.ui', self)
        self.setWindowTitle('Kuntoilusovelluksen ohje')
        self.closePB = self.closePushButton
        self.closePB.clicked.connect(self.closeHelp)

    # Methods ie. slots
    def closeHelp(self):
        self.close()