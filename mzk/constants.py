#!/usr/bin/env python
# mzk music theory helper - developed by acidvegas in python (https://acid.vegas/mzk)
# constants.py

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

intervals = {
	'unison'           : {'semitones':0,  'short_name':'P1' },
	'minor_second'     : {'semitones':1,  'short_name':'m2' },
	'major_second'     : {'semitones':2,  'short_name':'M2' },
	'minor_third'      : {'semitones':3,  'short_name':'m3' },
	'major_third'      : {'semitones':4,  'short_name':'M3' },
	'perfect_fourth'   : {'semitones':5,  'short_name':'P4' },
	'augmented_fourth' : {'semitones':6,  'short_name':'+4' },
	'diminished_fifth' : {'semitones':6,  'short_name':'d5' },
	'perfect_fifth'    : {'semitones':7,  'short_name':'P5' },
	'minor_sixth'      : {'semitones':8,  'short_name':'m6' },
	'major_sixth'      : {'semitones':9,  'short_name':'M6' },
	'minor_seventh'    : {'semitones':10, 'short_name':'m7' },
	'major_seventh'    : {'semitones':11, 'short_name':'M7' },
	'perfect_octave'   : {'semitones':12, 'short_name':'8va'}
}

notes         = ('A', 'A#', 'B',   'C',  'C#', 'D',  'D#',  'E',    'F',  'F#', 'G',  'G#'     )
numerals      = ('I', 'II', 'III', 'IV', 'V',  'VI', 'VII', 'VIII', 'IX', 'X',  'XI', 'XII'    )
scale_degrees = ('tonic','supertonic','mediant','subdominant','dominant''submediant','subtonic')

scales = {
	'algerian'              :  '2131131',
	'aeolian'               :  '2122122',
	'blues'                 :   '321132',
	'chromatic'             :  '1111111',
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