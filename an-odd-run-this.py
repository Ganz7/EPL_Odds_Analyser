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

	netChange = 0
	for result, odds in zip(results, oddsList):
		resultWithHighestOdd = odds.index(max(odds))

		if result == resultsDict[str(resultWithHighestOdd)]:
			netChange = netChange + betAmount * float(max(odds))
			#print (netChange)



	print ("Net Change is -- ", netChange)

if __name__ == '__main__':
	main()