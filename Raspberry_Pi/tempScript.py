# tempScript - Outputs DS18B20 Sensor Data in Fahrenheit and Celcius to CLI
# Output bit stream found on page 6 here: 
#   https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf

import os
import glob
import time

os.system('modproble w1-gpio')
os.system('modproble w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.25)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		raw_temp = lines[1][equals_pos+2:]
		temp_c = float(raw_temp) / 1000
		temp_f = temp_c * 9 / 5 + 32
		return temp_f, temp_c

while True:
	print(read_temp())
	time.sleep(.5)
