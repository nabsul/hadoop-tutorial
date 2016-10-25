#!/usr/bin/env python
import sys

for line in sys.stdin:
	if random.random() < 0.01:
		sys.stdout.write( line )
