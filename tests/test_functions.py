import sys
sys.path.insert(0, '../')
import song

# Check get_scale(key, m)
major_scale = song.get_scale('d', 'M')
minor_scale = song.get_scale('a', 'm')
if not major_scale[0] == ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']:
    print "ERROR: get_scale returning incorrect major scale"
if not minor_scale[0] == ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    print "ERROR: get_scale returnning incorrect minor scale"

# Check song.Song(__init__)
major_song = song.Song(major_scale[0], major_scale[1]) 
minor_song = song.Song(minor_scale[0], minor_scale[1])


# Check get_chord_progression(chord_progression, song)
# If no output, worked successfully
a = "one two three four".split(' ')
cp_major = song.get_chord_progression(a, major_song)
cp_minor = song.get_chord_progression(a, minor_song)
if cp_major == "ERROR":
    print "ERROR: get_chord_progression returned None"
if cp_minor == "ERROR":
    print "ERROR: get_chord_progression returned None"


# Check s.print_scale()
#s.print_scale()

# Check s.print_cp()
#s.print_cp()

# Check s.random8Notes()
#s.random8Notes()

# Check s.random16Notes()
#s.random16Notes()

# Check s.cp_melody()
#s.cp_melody()

# Check song.get_mode(mode, scale) return mode
mode = song.get_mode('dorian', major_song.scale)
if not mode == ['E', 'F#', 'G', 'A', 'B', 'C#', 'D']:
    print "ERROR: get_mode returning incorrect mode"

# Check get_relative_major(scale)
relative_major = song.get_relative_major(minor_song.scale)
print relative_major
print "Should be C Major"

# Check get_relative_minor(scale)
# Should be B Minor
relative_minor = song.get_relative_minor(major_song.scale)
print relative_minor
print "Should be B Minor"

# Check get_parallel_major(scale)
# Incorrect use, but should be D Major
parallel_major = song.get_parallel_major(minor_song.scale)
print parallel_major
print "Should be A Major"

# Check get_parallel_minor(scale)
# Should be D Minor
parallel_minor = song.get_parallel_minor(major_song.scale)
print parallel_minor
print "Should be D Minor"
