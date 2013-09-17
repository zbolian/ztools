import csv
import ConfigParser

class csvIO:

    def parseConfigFile(fileName):
        parser = ConfigParser.RawConfigParser()
        parser.read(fileName)
        return parser

    def importCsvFile(filename, retType, delimitChar=',', quoteCharacter='"'):
        if retType == "listOfDicts":
            returnData = []
            dictReader = csv.DictReader(open(filename, "rU"), delimiter=delimitChar, quotechar=quoteCharacter)
            for row in dictReader:
                returnData.append(row)
        elif retType == "listOfLists":
            returnData = []
            csvReader = csv.reader(open(filename,"rU"), delimiter=delimitChar, quotechar=quoteCharacter)
            for row in csvReader:
                returnData.append(row)
        else:
            print 'foo'

        return returnData

    def exportCsvFile(data, headers, filename, objType, delimitChar=',', quoteCharacter='"', quoting = csv.QUOTE_MINIMAL):
        if objType == "listOfDicts":
            with open(filename, "wb") as f:
                w = csv.DictWriter(f, fieldnames=headers, delimiter=delimitChar, quotechar=quoteCharacter, quoting=quoting)
                w.writeheader()
                w.writerows(data)
        elif objType == "listOfLists":
            ofile = open(filename,'wb')
            w = csv.writer(ofile, delimiter=delimitChar, quotechar=quoteCharacter, quoting=quoting)
            w.writerow(headers)
            for row in data:
                w.writerow(row)
            ofile.close()
        else:
            print 'foo'

pause = 1





__author__ = 'zach.bolian'
