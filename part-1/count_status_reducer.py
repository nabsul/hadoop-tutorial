#!/usr/bin/env python
import sys
import json

currentStatus = ''
count = 1
for line in sys.stdin:
	status = line.rstrip()
	if ( status == currentStatus ):
		count = count + 1
	else:
		if ( currentStatus != '' ):
			sys.stdout.write( "{}\t{}\n".format(currentStatus,count))
		count = 1
		currentStatus = status

sys.stdout.write( "{}\t{}\n".format(currentStatus,count))
	