'''
	Betting Odds Analysis
'''

from modules.CSVHandler import CSVHandlerClass

resultsDict = {'0':'H', '1':'D', '2':'A'}
betAmount = 10
		

def main():
	
	statsFile = CSVHandlerClass('data/csv/S13.csv')

	results, oddsList = statsFile.returnResultsAndOdds()
	statsFile.closeCSVFile()

	netChangeOne = 0
	netChangeTwo = 0

	for result, odds in zip(results, oddsList):
		resultWithHighestOdd = odds.index(max(odds))
		resultWithLowestOdd = odds.index(min(odds))

		if result == resultsDict[str(resultWithHighestOdd)]:
			netChangeOne = netChangeOne + betAmount * float(max(odds))
			#print (max(odds), " - ", netChange)

		elif result == resultsDict[str(resultWithLowestOdd)]:
			netChangeTwo = netChangeTwo + betAmount * float(min(odds))
			#print (max(odds), " - ", netChange)

	print ("Net Change is -- ", netChangeOne)
	print ("Net Change is -- ", netChangeTwo)

if __name__ == '__main__':
	main()