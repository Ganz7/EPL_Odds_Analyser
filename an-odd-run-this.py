'''
	Betting Odds Analysis
'''

import csv


def main():
	
	seasonStatsFile = open('data/csv/S13.csv','r')
	reader = csv.reader(seasonStatsFile)

	for row in reader:
		print (row)


if __name__ == '__main__':
	main()