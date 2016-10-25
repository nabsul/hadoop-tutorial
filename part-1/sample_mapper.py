#!/usr/bin/env python
import sys
import random

for line in sys.stdin:
	if random.random() < 0.01:
		sys.stdout.write( line )
