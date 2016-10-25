#!/usr/bin/env python
import sys
import json

for line in sys.stdin:
	try:
		data = json.loads(line)
		if ( 'status' in data ):
			sys.stdout.write( data['status'] + "\n" )
	except:
		continue
