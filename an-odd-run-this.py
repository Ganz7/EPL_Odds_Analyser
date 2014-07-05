'''
	Betting Odds Analysis
'''

from modules.CSVHandler import CSVHandlerClass

resultsDict = {'0':'H', '1':'D', '2':'A'}
betAmount = 10


def secondLargest(oddsList):
    n1, n2 = '0', '0'
    for x in oddsList:
        if float(x) >= float(n1):
            n1, n2 = x, n1
        elif float(x) > float(n2):
            n2 = x
    return n2		

def main():
	
	filename = ''
	season = 13

	while (season > 2):
		if season > 9 :
			filename = 'data/csv/S' + str(season) + '.csv'
		else:
			filename = 'data/csv/S0' + str(season) + '.csv'

		season = season - 1

		statsFile = CSVHandlerClass(filename)

		results, oddsList = statsFile.returnResultsAndOdds()
		statsFile.closeCSVFile()

		netChangeOne = 0
		netChangeTwo = 0
		netChangeThree = 0

		for result, odds in zip(results, oddsList):
			resultWithHighestOdd = odds.index(max(odds))
			resultWithLowestOdd = odds.index(min(odds))
			resultWithSecondHighestOdd = odds.index(secondLargest(odds))

			if result == resultsDict[str(resultWithHighestOdd)]:
				netChangeOne = netChangeOne + betAmount * float(max(odds))
				#print (max(odds), " - ", netChange)

			elif result == resultsDict[str(resultWithLowestOdd)]:
				netChangeTwo = netChangeTwo + betAmount * float(min(odds))
				#print (max(odds), " - ", netChange)

			else:
				netChangeThree = netChangeThree + betAmount * float(secondLargest(odds))

		print ("\n\nSeason ", season+1)
		print ("If you bet on the highest odds, Gross revenue -- ", netChangeOne)
		print ("If you bet on the lowest odds, Gross revenue -- ", netChangeTwo)
		print ("If you bet on the second largest odds, Gross revenue -- ", netChangeThree)

if __name__ == '__main__':
	main()