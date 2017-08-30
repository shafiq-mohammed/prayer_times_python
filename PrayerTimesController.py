'''Controller will do several things
1. View will call the controller and say "Hey controller, given the date, what are the prayer timings?"
2. Controller will be like, aight coo, given today's date, find that date in the 'prayer_date' column, 
3. Endpoint will return all prayer times for the day.
'''
from flask import Flask
from datetime import datetime
import csv

app = Flask(__name__)

@app.route('/')
def main():
	#retrieves todays date in the format of excel sheet
	today = get_todays_date()
	return "Today's date: " + today

#Function to retrieve today's date in the format found in the csv's 'prayer_date' column.
#I put 2016 since the csv file was made in 2016, so it would need that to match the csv's format.
def get_todays_date():
	day = datetime.now().day
	month = datetime.now().month
	today = str(month) + "/" + str(day) + "/" + "16"
	return today

@app.route('/readcsv')
def read_csv_file():
	csvfile = open('rcm_prayer_times.csv', 'r')
	rcm = csv.reader(csvfile)
	today = get_todays_date()
	for row in rcm:
		if row[1] == today:
			return str(row)
	return "didn't find: {}".format(today)
		
app.run(debug=True, port=7864, host='0.0.0.0')
