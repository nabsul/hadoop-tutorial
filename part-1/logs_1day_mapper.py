#!/usr/bin/env python
import sys
import json

for line in sys.stdin:
	try:
		data = json.loads(line)
		if ( 'date' in data and data['date'].startswith( '2016-10-03' ) ):
			sys.stdout.write( line )
	except:
		continue
