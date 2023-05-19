#!/usr/bin/env python
# mzk music theory helper - developed by acidvegas in python (https://git.acid.vegas/mzk)
# main.py

import sys

sys.dont_write_bytecode = True

import constants
import functions

if len(sys.argv) != 2:
	functions.print_help()
else:
	print(sys.argv[1])
	if sys.argv[1] == '--chords':
		functions.print_chords()
	elif sys.argv[1].startswith('--chord='):
		chord = sys.argv[1][8:]
		key   = chord.split('_')[0].upper()
		type  = chord[len(key)+1:].lower()
		if key in constants.notes and type in constants.chords:
			functions.print_scale(key, type, chord=True)
		else:
			print('error: invalid key or chord type\n\n')
			functions.print_help()
	elif sys.argv[1] == '--circle':
		functions.print_circle_of_fifths()
	elif sys.argv[1] == '--intervals':
		functions.print_intervals()
	elif sys.argv[1].startswith('--scale='):
		scale = sys.argv[1][8:]
		key   = scale.split('_')[0].upper()
		type  = scale[len(key)+1:].lower()
		if key in constants.notes and type in constants.scales:
			functions.print_scale(key, type)
		else:
			print('error: invalid key or chord type\n\n')
			functions.print_help()
	elif sys.argv[1] == '--scales':
		functions.print_scales()
	else:
		functions.print_help()