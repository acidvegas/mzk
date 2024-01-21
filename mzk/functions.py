#!/usr/bin/env python
# mzk music theory helper - developed by acidvegas in python (https://git.acid.vegas/mzk)
# functions.py

import constants

def chromatic_scale(key):
	notes = list(constants.notes)
	while notes[0] != key:
		notes.append(notes.pop(0))
	return notes

def generate_scale_string(string, scale_notes, full=False):
	notes = chromatic_scale(string.upper())*2 if full else chromatic_scale(string.upper())
	notes.append(notes[0])
	for index,note in enumerate(notes):
		if note in scale_notes:
			notes[index] = notes[index].center(5, '-')
		else:
			notes[index] = '-'*5
	return notes

def get_pattern(pattern):
	new_pattern = list()
	for step in pattern:
		if   step == '1' : new_pattern.append('H')
		elif step == '2' : new_pattern.append('W')
		elif step == '3' : new_pattern.append('WH')
	return ' '.join(new_pattern)

def chord_notes(type, key):
	notes = scale_notes(type, key)
	pattern = constants.chords[type]['pattern']
	_notes = [key,]
	for step in pattern.split()[1:]: #1 b3 5
		if len(step) == 2:
			if step[:1] == 'b':
				_notes.append(notes[int(step)-2])
			elif step[:1] == '#':
				_notes.append(notes[int(step)])
		else:
			_notes.append(notes[int(step)-1])
	return _notes

def print_scale(root, type, full=False, chord=False):
	frets = (24,147) if full else (12,75)
	print(f'{root.upper()} {type.upper()} SCALE'.center(frets[1]))
	print('  ┌' + '┬'.join('─'*5 for x in range(frets[0])) + '┐')
	print('0 │' + '│'.join(str(x).center(5) for x in range(1,frets[0]+1)) + '│')
	print('  ├' + '┼'.join('─'*5 for x in range(frets[0])) + '┤')
	notes = chord_notes(type, root) if chord else scale_notes(type, root)
	for string in ('eBGDAE'):
		string_notes = generate_scale_string(string, notes, full)
		print(string + ' │' + '│'.join(note.center(5, '-') for note in string_notes[1:]) + '│')
	print('  └' + '┴'.join('─'*5 for x in range(frets[0])) + '┘')
	print((', '.join(notes) + ' / ' + get_pattern(constants.scales[type])).rjust(frets[1]))

def scale_notes(type, key):
	last = 0
	all_notes = chromatic_scale(key)*2
	scale_notes = [all_notes[0],]
	for step in constants.scales[type]:
		last += int(step)
		scale_notes.append(all_notes[last])
	return scale_notes

def print_chord(root, type):
	# todo: finish this
	print('◯  ⬤ ')
	print('''╳   ╳   ╳   ╳   ╳   ╳
┌───┬───┬───┬───┬───┐
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
└───┴───┴───┴───┴───┘
E   A   D   G   B   e''')
	print('''╳           ◯       ◯
┌───┬───┬───┬───┬───┐
│   │   │   │   │   │
├───┼───┼───┼───⬤───┤
│   │   │   │   │   │
├───┼───⬤───┼───┼───┤
│   │   │   │   │   │
├───⬤───┼───┼───┼───┤
│   │   │   │   │   │
├───┼───┼───┼───┼───┤
│   │   │   │   │   │
└───┴───┴───┴───┴───┘
E   A   D   G   B   e''')


def print_circle_of_fifths():
	'''definition:
			the relationship among the 12 tones of the chromatic scale, their corresponding key signatures, & the associated major/minor keys

		accidentals:
			sharps - F, C, G, D, A, E, B
			flats  - B, E, A, D, G, C, F

		intervals:
			unison
			perfect   fifth
			major     sencond
			major     sixth
			major     third
			major     seventh
			augmented fourth
			minor     second
			minor     sixth
			minor     third
			minor     seventh
			perfect   fourth'''
	circle = constants.circle.replace('\n',' \n') + ' ' # todo: fix this
	for note in ('major','C','F','B♭','E♭','A♭','D♭','C♯','G♭/F♯','B','C♭','E','A','D','G'): # todo: reverse
		circle = circle.replace(f' {note} ', f' \033[91m{note}\033[0m ')
	for item in ('♮','1♭','2♭','3♭','4♭','5♭/7♯','6♭/6♯','7♭/5♯','4','3♯','2♯','1♯'):
		circle = circle.replace(f' {item} ', f' \033[90m{item}\033[0m ')
	for note in ('minor','a','d','g','c','f','b♭','e♭/d♯','g♯','c♯','f♯','b','c'):
		circle = circle.replace(f' {note} ', f' \033[92m{note}\033[0m ')
	print(circle)
	print(print_circle_of_fifths.__doc__)

def print_help():
	print('usage: python mzk.py [OPTIONS]')
	print('\noptions:')
	print('--chord=KEY_TYPE │ print a TYPE chord in the key of KEY')
	print('--circle         │ print the circle of fifths')
	print('--intervals      │ print list of intervals')
	print('--scale=KEY_TYPE │ print a TYPE scale in the key of KEY')
	print('--scales         │ print list of scale types & patterns')
	print('\nnote: KEY_TYPE must be formatted as such: c_major, f#_mixolydian, etc.')

def print_intervals():
	'''definition:
		the distance between two notes or pitches

	note:
		semitone - half step (b/c & e/f is a half step)
		tone     - whole step

	types:
		harmonic interval - notes played simultaneously
		melodic  interval - notes played successively

	makeup:
		quantity - distance between two notes
		quality  - number of semitones between notes

	qualities:
		major/minor - 2nds, 3rds, 6ths, 7ths
		perfect     - 4ths, 5ths, octaves
		diminished  - minor/perfect - 1 semitone
		augmented   - major/perfect + 1 semitone'''
	print('I N T E R V A L S'.center(38))
	print('┌───────────┬────────────────┬───────┐')
	print('│ semitones │ quality        │ short │')
	print('├───────────┼────────────────┼───────┤')
	for interval, info in constants.intervals.items():
		print('│ {0} │ {1} │ {2} │'.format(str(info['semitones']).rjust(9), interval.ljust(14), info['short_name'].ljust(5)))
	print('└───────────┴────────────────┴───────┘')
	print('\nC O M P O U N D   I N T E R V A L S'.center(42))
	print('┌───────────┬────────────────────┬───────┐')
	print('│ semitones │ quality            │ short │')
	print('├───────────┼────────────────────┼───────┤')
	for interval, info in constants.compound_intervals.items():
		print('│ {0} │ {1} │ {2} │'.format(str(info['semitones']).rjust(9), interval.ljust(18), info['short_name'].ljust(5)))
	print('└───────────┴────────────────────┴───────┘')
	print(print_intervals.__doc__)

def print_scales():
	'''definition:
		any set of musical notes ordered by fundamental frequency or pitch

	note:
		1 - half step
		2 - whole step
		3 - whole step half step'''
	print('S C A L E S'.center(43))
	print('┌───────────────────────┬─────────────────┐')
	print('│ name                  │ intervals       │')
	print('├───────────────────────┼─────────────────┤')
	for name, pattern in constants.scales.items():
		print(f'│ {name.ljust(21)} │ {get_pattern(pattern).rjust(15)} │')
	print('└───────────────────────┴─────────────────┘')
	print(print_scales.__doc__)