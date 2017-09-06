'''Controller will do several things
1. View will call the controller and say "Hey controller, given the date, what are the prayer timings?"
2. Controller will be like, aight coo, given today's date, find that date in the 'prayer_date' column, 
3. Endpoint will return all prayer times for the day.
'''
from flask import Flask, url_for
from flask import render_template
from datetime import datetime
import csv
import time

app = Flask(__name__)

@app.route('/')
def main():
	#Gets todays date, and then retrieves the row with the respective prayer timings for today in list format
	today = get_todays_date()
	times = read_csv_file(today)
	context = {
	'fajr_athan': times[3],
	'fajr_iqamah': times[4],

	'dhour_athan': times[5],
	'dhour_iqamah': times[6], 

	'asr_athan': times[7],
	'asr_iqamah': times[8],

	'maghrib_athan': times[9], 
	'maghrib_iqamah': times[10],

	'isha_athan': times[11], 
	'isha_iqamah': times[12], 

	'first_jummah_khutbah': times[13],
	'first_jummah_iqamah': times[14],

	'second_jummah_khutbah': times[16],
	'second_jummah_iqamah': times[17],
	'todays_date': (time.strftime("%A") + ", " + time.strftime("%B") + " " + time.strftime("%d") + ", " + time.strftime("%Y"))
	}
	return render_template("index.html", **context)#"Welcome to the app! + {}".format(str(todays_timings_list))

#Function to retrieve today's date in the format found in the csv's 'prayer_date' column.
#I put 2016 since the csv file was made in 2016, so it would need that to match the csv's format.
def get_todays_date():
	day = datetime.now().day
	month = datetime.now().month
	today = str(month) + "/" + str(day)
	return today

#Returns row
#@app.route('/readcsv')
def read_csv_file(today):
	csvfile = open('rcm_prayer_times.csv', 'r')
	rcm = csv.reader(csvfile)
	print("**************Start***********: " + str(today))
	for row in rcm:
		if row[1][0:-3] == today:
			print("**************SUCCESS***********")
			return row
	return "**************************************"
'''
@app.route('/parse')
def parse_row():
	todays_timings_list = read_csv_file()
	fajr_athan = todays_timings_list[3] 
	fajr_iqamah = todays_timings_list[4]
	return fajr_athan, fajr_iqamah
'''

		
app.run(debug=True, host='0.0.0.0', port=80)
