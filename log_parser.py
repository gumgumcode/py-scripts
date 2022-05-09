
import re
from collections import Counter
import csv

def reader(filename):

	with open('filename') as f:

		log = f.read()

		regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

		ips_list = re.findall(regexp, log)

		return ips_list

def counter(ips_list):

	return Counter(ips_list)

def write_csv(counter):

	with open('output.csv', 'w') as csvfile:

		writer = csv.writer(csvfile)

		header = ['IP', 'Frequency'] 
		writer.writerow(header)

		for item in counter:
			writer.writerow( (item, counter[item]) )


if __name__ == '__main__':
	write_csv(count(reader('log')))

	# read a log file
	# count number of IPs in it, return a dict of {ip:frequency} values
	# write it to a csv file