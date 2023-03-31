# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements' functionality
from PyQt5.uic import loadUi
import kuntoilija
import fitness
import timetools

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
        self.measuringDE.setDate(QtCore.QDate.currentDate())        
        self.heightDSB = self.heightDoubleSpinBox
        self.weightDSB = self.weightDoubleSpinBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self.waistSpinBox
        self.pelvisSB = self.pelvisSpinBox

        # Set the measuring date to current date
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)        
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots, ie. methods
    # Calculates BMI, Finnish and US fat percetanges and updates corresponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightDSB.value() # Spinbox value as integer
        weight = self.weightDSB.value()

        # Convert birthday to ISO string using QtCore's methods
        birthday = self.birthDE.date().toString(format=QtCore.Qt.ISODate)        
        
        # Set gender value according to ComboBox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1
        else:
            gender = 0
        
        # Convert measuring data to ISO string
        measuringDate = self.measuringDE.date().toString(format=QtCore.Qt.ISODate)
        
        # Calculate time difference with out homemade tools
        age = timetools.datediff2(birthday, measuringDate, 'year')

        # Create an athelete from Kuntoilija class
        athelete = kuntoilija.Kuntoilija(name, height, weight, age, gender, measuringDate)
        bmi = athelete.bmi

        self.showBmiLabel.setText(str(bmi))

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