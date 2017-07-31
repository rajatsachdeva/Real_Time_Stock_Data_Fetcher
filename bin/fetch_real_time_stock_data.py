#!/bin/user/python

# Program to fetch real time data from the google finance 

from googlefinance import getQuotes
import json


# Main Function 
def main():
	# Get the number of stocks whose details are to fetched
	num = int(input("Enter number of Stocks: "))
	
	# Get the Stock names whose details are to be fetched 
	stock_list = []
	for i in range(num):
		stock_list.append(input("{}. Enter Stock: ".format(i+1)))

	print (stock_list)

	# Get the details for the stock list entered by the user
	try:
		print(json.dumps(getQuotes(stock_list), indent=2))

	except:
		print("Something's not right")

# call Main Function
if __name__ == "__main__":
	main()
