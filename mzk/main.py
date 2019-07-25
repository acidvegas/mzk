#!/usr/bin/env python
# mzk music theory helper - developed by acidvegas in python (https://acid.vegas/mzk)
# main.py

import sys

sys.dont_write_bytecode = True

import constants
import functions

if len(sys.argv) != 2:
	functions.print_help()
else:
	sys.argv[1] = sys.argv[1].lower()
	if sys.argv[1].startswith('--chord='):
		chord = sys.argv[1][8:]
		key   = chord.split('_')[0]
		type  = chord[len(key)+1:]
		if key in constants.notes and type in constants.scales:
			functions.print_chord(key, type)
		else:
			print('error: invalid key or chord type\n\n')
			functions.print_help()
	elif sys.argv[1] == '--chords':
		functions.print_chords()
	elif sys.argv[1] == '--circle':
		functions.print_circle()
	elif sys.argv[1] == '--intervals':
		functions.print_intervals()
	elif sys.argv[1].startswith('--scale='):
		scale = sys.argv[1][8:]
		key   = scale.split('_')[0]
		type  = scale[len(key)+1:]
		if key in constants.notes and type in constants.scales:
			functions.print_scale(key, type)
		else:
			print('error: invalid key or chord type\n\n')
			functions.print_help()
	elif sys.argv[1] == '--scales':
		functions.print_scales()
	else:
		functions.print_help()