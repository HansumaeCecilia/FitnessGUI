# ROUTINES TO CREATE, WRITE AND READ JSON ATHLETE DATA FILE
# ====================================================

# LIBRARIES AND MODULES

import json

# CLASS DEFINITONS

class ProcessJsonFile():
    def __init__(self):
        pass

    def saveData(self, file, data):
        """Saves all athlete data to disk

        Args:
            file (str): File's name
            data (dictionary): List of dictionaries

        Returns:
            tuple: Error code, Error message, detailed Error message
        """
        with open(file, 'w') as fileToWrite:
            json.dump(data, fileToWrite, indent=4)
        status = (0, 'OK', 'All data saved successfully')
        return status
    
    def readData(self, file):
        """Reads athelete data from file

        Args:
            file (str): File's name

        Returns:
            tuple: Error code, Error message, detailed Error message, data
        """
        # Read previous athlete_data from disk
        with open(file, 'r') as fileToRead:
            athlete_data = json.load(fileToRead)
            message = 'OK'
            detailedMessage = 'Data read successfully from disk'
            data = (0, message, detailedMessage, athlete_data)
        return data

    def appendData(self, file, data):
        """Adds a new json object to the file

        Args:
            file (str): File's name
            data (dict): python dictionary containing data

        Returns:
            tuple: Error code, Error message, detailed Error message 
        """
        status = (0, 'All data saved successfully')
        return status        

# PRELIMINARY TESTS

if __name__ == "__main__":
    pass