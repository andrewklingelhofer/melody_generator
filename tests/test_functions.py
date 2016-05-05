import sys
sys.path.insert(0, '../')
import song

error = [] 

# Check get_scale(key, m)
major_scale = song.get_scale('d', 'M')
minor_scale = song.get_scale('a', 'm')
if not major_scale[0] == ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']:
    msg = "ERROR: get_scale returning incorrect major scale"
    error.append(msg)
if not minor_scale[0] == ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    msg = "ERROR: get_scale returnning incorrect minor scale"
    error.append(msg)

# Check song.Song(__init__)
major_song = song.Song(major_scale[0], major_scale[1]) 
minor_song = song.Song(minor_scale[0], minor_scale[1])


# Check get_chord_progression(chord_progression, song)
# If no output, worked successfully
a = "one two three four".split(' ')
cp_major = song.get_chord_progression(a, major_song)
cp_minor = song.get_chord_progression(a, minor_song)
if cp_major == "ERROR":
    msg = "ERROR: get_chord_progression returned None"
    error.append(msg)
if cp_minor == "ERROR":
    msg = "ERROR: get_chord_progression returned None"
    error.append(msg)

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
    msg = "ERROR: get_mode returning incorrect mode"
    error.append(msg)

# Check get_relative_major(scale)
relative_major = song.get_relative_major(minor_song.scale)
if not relative_major == "C Major: ['C', 'D', 'E', 'F', 'G', 'A', 'B']":
    msg = "ERROR: get_relative_major incorrect output"
    error.append(msg)

# Check get_relative_minor(scale)
# Should be B Minor
relative_minor = song.get_relative_minor(major_song.scale)
if not relative_minor == "B Minor: ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']":
    msg = "ERROR: get_relative_minor incorrect output"
    error.append(msg)

# Check get_parallel_major(scale)
# Incorrect use, but should be D Major
parallel_major = song.get_parallel_major(minor_song.scale)
if not parallel_major == "A Major: ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']":
    msg = "ERROR: get_parallel_major incorrect output"
    error.append(msg)

# Check get_parallel_minor(scale)
# Should be D Minor
parallel_minor = song.get_parallel_minor(major_song.scale)
if not parallel_minor == "D Minor: ['D', 'E', 'F', 'G', 'A', 'Bb', 'C']":
    msg = "ERROR: get_parallel_minor incorrect output"
    error.append(msg)

# Check get_fifth_chord(scale)
chord = song.get_fifth_chord(major_song.scale)
if not chord == ['D', 'F#', 'A']:
    msg = "ERROR: get_fifth_chord incorrect output"
    error.append(msg)

# Check get_seventh_chord(scale)
chord = song.get_seventh_chord(minor_song.scale)
if not chord == ['A', 'C', 'E', 'G']:
    msg = "ERROR: get_seventh_chord incorrect output"
    error.append(msg)

if error:
    for msg in error:
        print msg
else:
    print "Functions run as expected"
