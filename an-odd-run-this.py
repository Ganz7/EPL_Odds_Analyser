'''
	Betting Odds Analysis
'''

import csv

from modules.CSVHandler import CSVHandlerClass


def main():
	

	statsFile = CSVHandlerClass('data/csv/S13.csv')

	results, odds = statsFile.returnResultsAndOdds()

	statsFile.closeCSVFile()


if __name__ == '__main__':
	main()