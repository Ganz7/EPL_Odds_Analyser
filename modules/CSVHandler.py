
import csv

class CSVHandlerClass(object):
	def __init__(self, filename):
		self.seasonStatsFile = open(filename,'r')


	def returnResultsAndOdds(self):

		reader = csv.reader(self.seasonStatsFile)

		resultsList = []
		oddsList = []

		firstLine = True
		for row in reader:
			if firstLine:
				firstLine =  False
				continue

			resultsList.append(row[6])
			
			odds = [row[23], row[24], row[25]]
			oddsList.append(odds)

		return resultsList, oddsList


	def closeCSVFile(self):
		self.seasonStatsFile.close()