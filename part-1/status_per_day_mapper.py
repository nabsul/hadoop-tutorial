#!/usr/bin/env python
import sys
import json
import re

regex = re.compile( '^(.+)T' )

for line in sys.stdin:
	try:
		data = json.loads( line )
		if ( 'status' in data and 'date' in data ):
			match = regex.match( data[ 'date' ] )
			if ( match ):
				date = match.group( 1 )
				sys.stdout.write( "{}\t{}\n".format( date, data[ 'status' ] ) )
				
	except:
		continue
