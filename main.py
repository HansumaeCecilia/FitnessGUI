# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets as QW # UI elements' functionality
from PyQt5.uic import loadUi
import kuntoilija
import timetools
import athlete_file # Home made module for processing data files

# TODO: Import some library able to plot trends and make it as widget in the UI

# Class for the main window
class MainWindow(QW.QMainWindow):
    
    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        self.main = loadUi('main.ui', self)

        # Define UI Controls, ie. buttons and input fields
        self.nameLE = self.findChild(QW.QLineEdit, 'nameLineEdit')        
        self.nameLE.textEdited.connect(self.activateCalculatePB)

        self.birthDE = self.birthDateEdit
        self.birthDE.dateChanged.connect(self.activateCalculatePB)
        self.genderCB = self.genderComboBox
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB)

        self.measuringDE = self.measuringDateEdit

        # Set measuring date to current date
        self.measuringDE.setDate(QtCore.QDate.currentDate())

        self.heightDSB = self.heightDoubleSpinBox  
        self.heightDSB.valueChanged.connect(self.activateCalculatePB)      
        self.weightDSB = self.weightDoubleSpinBox  
        self.weightDSB.valueChanged.connect(self.activateCalculatePB)      
        self.neckSB = self.neckSpinBox
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self.waistSpinBox
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipSB = self.hipSpinBox
        self.hipSB.setEnabled(False)
        self.hipSB.valueChanged.connect(self.activateCalculatePB)
        
        '''
        self.minHeightLE = self.minHeightLabel   
        self.minHeightLE.setVisible(False)        
        '''                   

        # TODO: Disable Calculate button until values have been edited
        self.calculatePB = self.findChild(QW.QPushButton, 'calculatePushButton')
        self.calculatePB.clicked.connect(self.calculateAll)
        self.calculatePB.setEnabled(False)           

        # TODO: Disable Save button until values have been calculated     
        #self.savePB = self.savePushButton
        self.savePB = self.findChild(QW.QPushButton, 'savePushButton')
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)

        # Read data from file and save it to a list
        self.dataList = []
        jsonFile = athlete_file.ProcessJsonFile()
        try:
            data = jsonFile.readData('athleteData.json')
            self.dataList = data[3]
        except Exception as e:
            data = (1, 'Error', str(e), self.dataList)              
        
    # Define slots, ie. methods
    def activateCalculatePB(self):
        self.calculatePB.setEnabled(True)
        if self.nameLE.text() == '':
            self.calculatePB.setEnabled(False)
        
        if self.birthDE.date() == QtCore.QDate(1900, 1, 1):
            self.calculatePB.setEnabled(False)
    
        if self.genderCB.currentText() == '':
            self.calculatePB.setEnabled(False)

        if self.heightDSB.value() == 100:            
            self.calculatePB.setEnabled(False)       

        if self.weightDSB.value() == 20:
            self.calculatePB.setEnabled(False)

        if self.neckSB.value() == 10:
            self.calculatePB.setEnabled(False)

        if self.waistSB.value() == 30:
            self.calculatePB.setEnabled(False)

        if self.genderCB.currentText() == 'Nainen':
            self.hipSB.setEnabled(True)
            if self.genderCB.currentText() == 50:
                self.calculatePB.setEnabled(False)
        
        else:
            self.hipSB.setEnabled(False)

    '''
    def showMinHeight(self):        
        if self.heightDSB.value == 150:
            self.minHeightLE.setVisible(True)    
    '''    
        
    # Calculates BMI, Finnish and US fat percetanges and updates corresponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightDSB.value() # Spinbox value as integer
        weight = self.weightDSB.value()
        self.calculatePB.setEnabled(False)
        self.savePB.setEnabled(True)

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

        neck = self.neckSB.value()
        waist = self.waistSB.value()
        hip = self.hipSB.value()

        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, neck, waist, hip, measuringDate)
        
        bmi = athlete.bmi
        self.showBmiLabel.setText(str(bmi))      
        
        fiFatPercentage = athlete.fi_rasva
        usaFatPercentage = athlete.usa_rasva

        self.fatFiLabel.setText(str(fiFatPercentage))
        self.fatUsLabel.setText(str(usaFatPercentage))                 

        self.dataRow = self.constructData(athlete)
        print(self.dataRow)        

    def constructData(self, athlete):
        athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino,
                            'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'pvm': athlete.punnitus_paiva,
                            'bmi': athlete.bmi, 'rasvaprosenttiFi': athlete.fi_rasva, 'rasvaprosenttiUs': athlete.usa_rasva}
        return athlete_data_row

    # Saves data to disk
    def saveData(self):
        self.dataList.append(self.dataRow)
        jsonfile2 = athlete_file.ProcessJsonFile()
        status = jsonfile2.saveData('athleteData.json', self.dataList)
        print(status)

if __name__ == "__main__":

    # Create the application
    app = QW.QApplication(sys.argv)

  # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())