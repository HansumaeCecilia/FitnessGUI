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
import instructions
import BGPictures # Compiled resources for background images
from PyQt5.QtGui import QPixmap # For converting picture files to pixmaps

# TODO: Make another resource file for the help window, build and import it
# TODO: Import some library able to plot trends and make it a widget in the UI

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
        self.hipsL = self.hipsLabel

        # Set measuring date to current date
        self.measuringDE.setDate(QtCore.QDate.currentDate())

        # TODO: Change spin boxes to sliders and add labels to show values
        self.heightVS = self.heightVerticalSlider
        self.heightVS.valueChanged.connect(self.activateCalculatePB)
        self.dialWeight = self.weightDial
        self.dialWeight.valueChanged.connect(self.activateCalculatePB)
        self.neckHS = self.neckHorizontalSlider
        self.neckHS.valueChanged.connect(self.activateCalculatePB)
        self.waistHS = self.neckHorizontalSlider
        self.waistHS.valueChanged.connect(self.activateCalculatePB)
        self.hipsHS = self.hipsHorizontalSlider
        self.hipsHS.valueChanged.connect(self.activateCalculatePB)

        self.dimensionBox = self.dimensionFrame        

        # Create a status bar for showing informational messages
        self.statusBar = QW.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.show()

        # self.calculatePB = self.calculatePushButton
        self.calculatePB = self.findChild(QW.QPushButton, 'calculatePushButton')
        self.calculatePB.clicked.connect(self.calculateAll)
        self.calculatePB.setEnabled(False)           

        # Temporary push button for inserting test values into controls
        # self.testPB = self.testUiPushButton
        # self.testPB.clicked.connect(self.insertTestValues)
        
        # A push button for saving user data
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

        # MENU ACTIONS
        self.actionRestoreDefaults.triggered.connect(self.restoreDefaults)  
        self.actionInstructions.triggered.connect(self.openHelpDialog)
    
    # Create an alerting method
    def alert(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Critical)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    # Create a warning method
    def warn(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Warning)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    # Create an information method  
    def inform(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Information)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def showMessageBox(self, windowTitle, message, detailedMessage, icon='Information'):
        """Shows icon depending on error message

        Args:
            windowTitle (str): Header for the message window 
            message (str): Message to be shown
            detailedMessage (str): A message that can be viewed by pressing the 'details' button
            icon (str, optional): Allowed values: NoIcon, Information, Question, Warning and Critical
        """
        iconTypes = {'Information': QW.QMessageBox.Information, 'NoIcon': QW.QMessageBox.NoIcon, 
         'Question': QW.QMessageBox.Question, 'Warning': QW.QMessageBox.Warning, 'Critical': QW.QMessageBox.Critical}
        msgBox = QW.QMessageBox()
        msgBox.setIcon(iconTypes[icon])
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    # Define slots, ie. methods
    def activateCalculatePB(self):
        self.calculatePB.setEnabled(True)
        if self.nameLE.text() == '':
            self.calculatePB.setEnabled(False)
        
        if self.birthDE.date() == QtCore.QDate(1900, 1, 1):
            self.calculatePB.setEnabled(False)
    
        if self.genderCB.currentText() == '':
            self.calculatePB.setEnabled(False)

        if self.heightVS.value() == 100:
            self.calculatePB.setEnabled(False)
        
        if self.dialWeight.value() == 20:
            self.calculatePB.setEnabled(False)
        
        if self.neckHS.value() == 10:
            self.calculatePB.setEnabled(False)
        
        if self.waistHS.value() == 30:
            self.calculatePB.setEnabled(False)       

        if self.genderCB.currentText() == 'Nainen' or self.genderCB.currentText() == '':
            self.hipsHS.show()
            self.dimensionBox.setStyleSheet("background-image : url(images/NaisSlice.png)")

            if self.hipsHS.value() == 50:
                self.calculatePB.setEnabled(False)
        
        else:
            self.hipsHS.hide()
            self.hipsL.hide()
            self.dimensionBox.setStyleSheet("background-image : url(images/MiesSlice.png)")
        
    def insertTestValues(self):
        # Set test values to all controls
        self.nameLE.setText('Teppo Testi')
        testBirthDay = QtCore.QDate(1999, 12, 31)
        self.birthDE.setDate(testBirthDay)
        self.genderCB.setCurrentText('Mies')
        self.heightVS.setValue(171)
        self.dialWeight.setValue(75)
        self.neckHS.setValue(27)
        self.waistHS.setValue(90)

    # Calculates BMI, Finnish and US fat percetanges and updates corresponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightVS.value() # Spinbox value as integer
        weight = self.dialWeight.value()
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
        
        # Calculate time difference with our homemade tools
        age = timetools.datediff2(birthday, measuringDate, 'year')        
        neck = self.neckHS.value()
        if neck < 21:
            # self.alert('Tarkista kaulan ympärysmitta', 'Kaulan ympärysmitta liian pieni',
            #             'Kaulan koko voi olla välillä 21 - 60 cm')
            self.showMessageBox('Tarkista kaulan ympärysmitta', 'Kaulan ympärysmitta virheellinen',
                                'Sallitut arvot 21 - 60 cm', 'Warning')
        waist = self.waistHS.value()
        hip = self.hipsHS.value()

        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, neck, waist, hip, measuringDate)
        
        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi))      
        
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

        # Save list to a json file
        jsonfile2 = athlete_file.ProcessJsonFile()
        status = jsonfile2.saveData('athleteData.json', self.dataList)

        # Show message about status of saving on statbar
        self.statusBar.showMessage(status[1], 4000)

        # Call error message box if error code is not 0
        if status[0] != 0:
            self.alert(status[1], status[2])
        else:
            self.restoreDefaults()

        # TODO: Reset fat percentage values in UI after saving   

    def restoreDefaults(self):
        # Set all inputs to their default values after saving data
        zeroDate = QtCore.QDate(1900, 1, 1)
        self.birthDE.setDate(zeroDate)
        zeroDate2 = (QtCore.QDate.currentDate())
        self.measuringDE.setDate(zeroDate2)
        self.nameLE.clear()
        self.genderCB.clear()       
        self.heightVS.setValue(100)
        self.dialWeight.setValue(20)
        self.neckHS.setValue(10)
        self.waistHS.setValue(30)
        self.hipsHS.setValue(50)
        self.savePB.setEnabled(False)        
        self.bmiLE.setText('0')
        self.fatFiLE.setText('0')
        self.fatUsLE.setText('0')
    
    def openHelpDialog(self):
        openHelp = instructions.OpenHelp()
        openHelp.exec()

if __name__ == "__main__":

    # Create the application
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion') # Use fusion style in form

  # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())