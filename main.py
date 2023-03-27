# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt6 import QtCore # Core functionality of Qt
from PyQt6 import QtWidgets # UI elements' functionality
from PyQt6.uic.load_ui import loadUi

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        self.main = loadUi('main.ui', self)

        # Define UI Controls, ie. buttons and input fields
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)

    # Define slots, ie. methods
    def calculateAll(self):
        self.showBmiLabel.setValue('100')

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

  # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())