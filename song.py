# Things to do:
# 1. Add more chords i.e. diminished, augmented
# 2. Add ability to cp i.e. 'one flat two three' (cMajor, dbMajor/minor, eMinor)
# 3. And more...

from random import randint
from scales import major_scales, minor_scales, cof_major, cof_minor, get_mode, chord_progression_names, get_chord_progression, scales, get_scale, get_relative_major, get_relative_minor, get_parallel_major, get_parallel_minor, get_fifth_chord, get_seventh_chord
from options_song import options, check_scale_options

# Add function for leap
def random_leap(scale, prev_note, leap_len):
    # Scale should be modal version (for now)
    # Returns next note 
    if prev_note in scale:
        spot = scale.index(prev_note)
        num = randint(-(leap_len), leap_len)
        if num < 0:
            spot += num
            if spot < 0:
                spot += len(scale)
        elif num > 0:
            spot += num
            if spot >= len(scale):
                spot -= len(scale)
        return scale[spot]
    else:
        print "ERROR: prev_note " + prev_note + " not in scale: " + str(scale)

# Direction set to 1 or 0 for up or down respectively
def set_leap(scale, prev_note, leap_len, direction):
    # Scale should be modal version (for now)
    # Returns next note 
    if prev_note in scale:
        spot = scale.index(prev_note)
        if direction == 1:
            num = leap_len - 1
        else:
            num = -(leap_len) + 1
        spot += num
        if spot < 0:
            spot += len(scale)
        elif spot >= len(scale):
            spot -= len(scale)
        return scale[spot]
    else:
        print "ERROR: prev_note " + prev_note + " not in scale: " + str(scale)

# Song Class
class Song:
    
    def __init__(self, scale, scale_name):
        self.scale = scale
        self.scale_name = scale_name
        self.chord_progression = None

    def print_scale(self):
        print self.scale_name + ": " + str(self.scale)

    def print_cp(self):
        print str(self.chord_progression)

    def random8Notes(self):
        # Always begins with tonic
        eightNotes = [self.scale[0]]
        for x in range(0, 8-1):
            num = randint(0, len(self.scale)-1)
            eightNotes.append(self.scale[num])
        print "Random 8 Notes: " + str(eightNotes)

    def random16Notes(self):
        # Always begins with tonic
        sixteenNotes = [self.scale[0]]
        for x in range(0, 16-1):
            num = randint(0, len(self.scale)-1)
            sixteenNotes.append(self.scale[num])
        print "Random 16 Notes: " + str(sixteenNotes)

    def cp_random_melody(self):
        if not self.chord_progression == None or len(self.chord_progression) < 2:
            melody = [self.scale[0]]
            for x in range(0, 3):
                num = randint(0, len(self.scale)-1)
                melody.append(self.scale[num])
            for x in range(0, len(self.chord_progression)-1):
                # Done three more times to get 16
                chord_name = self.chord_progression[x+1]
                chord = get_mode(chord_name, self.scale)
                for y in range(0, 4):
                    num = randint(0, len(chord)-1)
                    melody.append(chord[num])
            print melody 
        else:
            print "No chord progression or length too short"

    # Add functions for stepwise notes or certain leaps, then make those functions random

    def cp_stepwise_melody(self):
        if not self.chord_progression == None or len(self.chord_progression) < 2:
            count = 0
            spot = 0
            melody = [self.scale[0]]
            for x in range(0, 3):
                note = melody[count] 
                spot = self.scale.index(note)
                diff = randint(-1, 1)
                spot += diff
                if spot == -1:
                    spot = len(self.scale) - 1
                elif spot == len(self.scale):
                    spot = 0
                note = self.scale[spot]
                melody.append(note)
            for x in range(0, len(self.chord_progression)-1):
                chord_name = self.chord_progression[x+1]
                chord = get_mode(chord_name, self.scale)
                for y in range(0, 4):
                    # Same mode for this, so should be fine
                    # But need to fix if note doesn't exist in chord progression
                    note = melody[count]
                    spot = chord.index(note)
                    diff = randint(-1, 1)
                    spot += diff
                    if spot == -1:
                        spot = len(chord) - 1
                    elif spot == len(chord):
                        spot = 0
                    note = chord[spot]
                    melody.append(note)
            print melody
        else:
            print "No chord progression or length too short"

def create_song():
    print "Input Key: (c, g, d, a, e, b, f, bb, eb, ab, db, gb, c#)"
    key = raw_input('>>> ')
    print "Major or Minor? (M or m)"
    m_m = raw_input('>>> ')
    scale = get_scale(key, m_m)
    song = Song(scale[0], scale[1])
    song.print_scale()
    return song

# Song Loop
def song_options(song):
    while True:
        print "What would you like to do with this song? ('h' for help)"
        i = raw_input('>>> ')
        if i == 'e' or i == 'exit':
            break
        else:
            check_scale_options(i, song)
