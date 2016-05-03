import sys
sys.path.insert(0, '../')
import song

s = song.create_song()
cp = "one two three four".split(' ')

song.get_chord_progression(cp, s)

s.cp_melody()
