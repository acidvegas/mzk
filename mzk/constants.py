#!/usr/bin/env python
# mzk music theory helper - developed by acidvegas in python (https://git.acid.vegas/mzk)
# constants.py

chords = {
	'major'              : {'symbol':'',      'pattern':'1 3 5'},
	'minor'              : {'symbol':'m',     'pattern':'1 b3 5'},
	'7th'                : {'symbol':'7',     'pattern':'1 3 5 b7'},
	'minor_7th'          : {'symbol':'m7',    'pattern':'1 b3 5 b7'},
	'major_7th'          : {'symbol':'maj7',  'pattern':'1 3 5 7'},
	'minor_7th_flat_5th' : {'symbol':'m7b5',  'pattern':'1 b3 b5 b7'},
	'suspended_4th'      : {'symbol':'sus4',  'pattern':'1 4 5'},
	'diminished'         : {'symbol':'dim',   'pattern':'1 b3 b5'},
	'augmented'          : {'symbol':'aug',   'pattern':'1 3 #5'},
	'6th'                : {'symbol':'6',     'pattern':'1 3 5 6'},
	'minor_6th'          : {'symbol':'m6',    'pattern':'1 b3 5 6'},
	'minor_6th_add_9th'  : {'symbol':'6add9', 'pattern':'1 3 5 6 9'},
	'9th'                : {'symbol':'9',     'pattern':'1 3 5 b7 9'},
	'minor_9th'          : {'symbol':'m9',    'pattern':'1 b3 5 b7 9'},
	'major_9th'          : {'symbol':'maj9',  'pattern':'1 3 5 7 9'}
}

circle = '''                        major

                          C
               F                     G
                          ♮
                  1♭              1♯
                          a
      B♭             d         c               D
           2♭                           2♯
                g       minor       b


    E♭   3♭   c                       f♯   3♯   A


                f                   c♯
           4♭                            4
      A♭            b♭         g♯             E
                        e♭/d♯
              5♭/7♯               7♭/5♯
                        6♭/6♯
              D♭                     B
                        G♭/F♯
          C♯                           C♭'''

colors = {
	'gray'  : '\033[0;90m',
	'red'   : '\033[0;91m',
	'green' : '\033[0;92m',
	'reset' : '\033[0m'
}

compound_intervals = {
	'minor_ninth'        : {'semitones':13, 'short_name':'m9'},
	'major_ninth'        : {'semitones':14, 'short_name':'M9'},
	'minor_tenth'        : {'semitones':15, 'short_name':'m10'},
	'major_tenth'        : {'semitones':16, 'short_name':'M10'},
	'perfect_eleventh'   : {'semitones':17, 'short_name':'P11'},
	'augmented_eleventh' : {'semitones':18, 'short_name':'TT'},
	'perfect_twelfth'    : {'semitones':19, 'short_name':'P12'},
	'minor_thirteenth'   : {'semitones':20, 'short_name':'m13'},
	'major_thirteenth'   : {'semitones':21, 'short_name':'M13'},
	'minor_fourteenth'   : {'semitones':22, 'short_name':'m14'},
	'major_fourteenth'   : {'semitones':23, 'short_name':'M14'},
	'double_octave'      : {'semitones':24, 'short_name':'15ma'}
}

intervals = {
	'perfect_unison' : {'semitones':0,  'short_name':'P1'},
	'minor_second'   : {'semitones':1,  'short_name':'m2'},
	'major_second'   : {'semitones':2,  'short_name':'M2'},
	'minor_third'    : {'semitones':3,  'short_name':'m3'},
	'major_third'    : {'semitones':4,  'short_name':'M3'},
	'perfect_fourth' : {'semitones':5,  'short_name':'P4'},
	'tritone'        : {'semitones':6,  'short_name':'TT'}, # diminished fifth / augmented fourt
	'perfect_fifth'  : {'semitones':7,  'short_name':'P5'},
	'minor_sixth'    : {'semitones':8,  'short_name':'m6'},
	'major_sixth'    : {'semitones':9,  'short_name':'M6'},
	'minor_seventh'  : {'semitones':10, 'short_name':'m7'},
	'major_seventh'  : {'semitones':11, 'short_name':'M7'},
	'perfect_octave' : {'semitones':12, 'short_name':'P8'}
}

notes         = ('A', 'A#', 'B',   'C',  'C#', 'D',  'D#',  'E',    'F',  'F#', 'G',  'G#') # Chromatic scale
numerals      = ('I', 'II', 'III', 'IV', 'V',  'VI', 'VII', 'VIII', 'IX', 'X',  'XI', 'XII')
scale_degrees = ('tonic','supertonic','mediant','subdominant','dominant''submediant','subtonic')

scales = {
	'algerian'              :  '2131131',
	'aeolian'               :  '2122122',
	'blues'                 :   '321132',
	'dorian'                :  '2122212',
	'half_whole_diminished' : '12121212',
	'harmonic_minor'        :  '2122131',
	'ionian'                :  '2212221',
	'locrian'               :  '1221222',
	'lydian'                :  '2221221',
	'major'                 :  '2212221',
	'major_pentatonic'      :    '22323',
	'melodic_minor'         :  '2122221',
	'mixolydian'            :  '2212212',
	'natural_minor'         :  '2122122',
	'persian'               :  '1311231',
	'phrygian'              :  '1222122',
	'whole_half_diminished' : '21212121',
	'whole_tone'            :  '2222222'
}
