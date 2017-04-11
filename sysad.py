#!/usr/bin/python
import psutil
import re
import time

try:
	while True:
		print "\nCurrent CPU percentage: %.2f %%" % psutil.cpu_percent()
		
		#Find free memory 
		memory_regex = re.compile('free=([0-9]*)')
		free_memory_raw = memory_regex.findall(str(psutil.virtual_memory()))
		free_memory_MB = int(free_memory_raw[0])/(1000*1000)
		
		print "Current free memory: %d MB" % free_memory_MB
		
		#Find free disk 
		disk_regex = re.compile('free=([0-9]*)')
		free_disk_raw = disk_regex.findall(str(psutil.disk_usage('/')))
		free_disk_GB = int(free_disk_raw[0])/(1000*1000*1000)
		
		print "Current free disk on \"/\": %d GB" % free_disk_GB

		print "Press Ctrl-C to stop\n"
		time.sleep(2)
except KeyboardInterrupt:
	pass
