# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements' functionality
from PyQt5.uic import loadUi
import kuntoilija
import fitness

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        self.main = loadUi('main.ui', self)

        # Define UI Controls, ie. buttons and input fields
        self.nameLE = self.nameLineEdit
        self.birthDE = self.birthDateEdit
        self.genderCB = self.genderComboBox
        self.measuringDE = self.measuringDateEdit        
        self.heightDSB = self.heightDoubleSpinBox
        self.weightDSB = self.weightDoubleSpinBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self.waistSpinBox
        self.pelvisSB = self.pelvisSpinBox

        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)        
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots, ie. methods
    # Calculates BMI, Finnish and US fat percetanges and updates corresponding labels
    def calculateAll(self):
        height = self.heightDSB.value() # Spinbox value as integer
        weight = self.weightDSB.value()                     
        age = 100
        gender = self.genderCB.currentText()
        measuring_date = str(self.measuringDE.date().getDate())      
        # athelete = kuntoilija.Kuntoilija()
        # bmi = athelete.bmi

        self.showBmiLabel.setText(measuring_date)

    # Saves data to disk
    def saveData(self):
        pass

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

  # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())