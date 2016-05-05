from random import randint

# Song Options
options = (
    "'scale': print scale",
    "'print cp': print chord progression",
    "'8notes': print 8 random notes",
    "'16notes': print 16 random notes",
    "'melody cp': print 4 notes per chord in progression",
    "'get mode <mode>': get mode from song key",
    "'get relative <major/minor>': get relative minor/major key",
    "'get parallel <major/minor>': get parallel minor/major key",
    "'cp <chord progression>': i.e. one five six four",
    "'cof <major/minor>': print circle of fifths",
    "'h' or 'help': help",
    "'e' or 'exit': exit song",
)

def check_scale_options(i, song):
    if i == 'scale':
        song.print_scale()
    if i == 'print cp':
        song.print_cp()
    elif i == '8notes':
        song.random8Notes()
    elif i == '16notes':
        song.random16Notes()
    elif i == 'melody cp':
        song.cp_melody()
    elif i[:8] == 'get mode':
        a = i.split(' ')
        if len(a) > 2:
            mode = a[2]
            new_scale = get_mode(mode, song.scale)
            print new_scale
        else:
            print "Please input mode name"
    elif i[:12] == 'get relative':
        a = i.split(' ')
        if len(a) > 2:
            relative = a[2]
            if relative == 'major':
                string = get_relative_major(song.scale)
                print string
            elif relative == 'minor':
                string = get_relative_minor(song.scale)
                print string 
            else:
                print "Please use valid relative"
        else:
            print "Please enter relative type"
    elif i[:12] == 'get parallel':
        a = i.split(' ')
        if len(a) > 2:
            parallel = a[2]
            if parallel == 'major':
                string = get_parallel_major(song.scale)
                print string
            elif parallel == 'minor':
                string = get_parallel_minor(song.scale)
                print string 
            else:
                print "Please use valid relative"
        else:
            print "Please enter relative type"
    elif i[:2] == 'cp':
        a = i.split(' ')
        if len(a) > 1:
            chord_progression = a[1:]
            get_chord_progression(chord_progression, song)
        else:
            print "Please enter valid chord progression"
    elif i[:3] == 'cof':
        a = i.split(' ')
        if len(a) > 1:
            chord_type = a[1]
            if chord_type == 'major':
                print cof_major
            elif chord_type == 'minor':
                print cof_minor
            else:
                print "Please use valid circle of fifths type"
        else:
            print "Please enter circle of fifths type"
    elif i == 'h' or i == 'help':
        for option in options:
            print option

# Major Scales
cMajor = (["C", "D", "E", "F", "G", "A", "B"], 'C Major')
gMajor = (["G", "A", "B", "C", "D", "E", "F#"], 'G Major')
dMajor = (["D", "E", "F#", "G", "A", "B", "C#"], 'D Major')
aMajor = (["A", "B", "C#", "D", "E", "F#", "G#"], 'A Major')
eMajor = (["E", "F#", "G#", "A", "B", "C#", "D#"], 'E Major')
bMajor = (["B", "C#", "D#", "E", "F#", "G#", "A#"], 'B Major')
fMajor = (["F", "G", "A", "Bb", "C", "D", "E"], 'F Major')
bbMajor = (["Bb", "C", "D", "Eb", "F", "G", "A"], 'Bb Major')
ebMajor = (["Eb", "F", "G", "Ab", "Bb", "C", "D"], 'Eb Major')
abMajor = (["Ab", "Bb", "C", "Db", "Eb", "F", "G"], 'Ab Major')
dbMajor = (["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"], 'Db Major')
gbMajor = (["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"], 'Gb Major')

# Minor Scales
aMinor = (["A", "B", "C", "D", "E", "F", "G"], 'A Minor')
eMinor = (["E", "F#", "G", "A", "B", "C", "D"], 'E Minor')
bMinor = (["B", "C#", "D", "E", "F#", "G", "A"], 'B Minor')
fsharpMinor = (["F#", "G#", "A", "B", "C#", "D", "E"], 'F# Minor')
csharpMinor = (["C#", "D#", "E", "F#", "G#", "A", "B"], 'C# Minor')
abMinor = (["Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"], 'Ab Minor')
dMinor = (["D", "E", "F", "G", "A", "Bb", "C"], 'D Minor')
gMinor = (["G", "A", "Bb", "C", "D", "Eb", "F"], 'G Minor')
cMinor = (["C", "D", "Eb", "F", "G", "Ab", "Bb"], 'C Minor')
fMinor = (["F", "G", "Ab", "Bb", "C", "Db", "Eb"], 'F Minor')
bbMinor = (["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"], 'Bb Minor')
ebMinor = (["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"], 'Eb Minor')

# Circle of Fifths: Major
cof_major = [
        cMajor, 
        gMajor, 
        dMajor, 
        aMajor, 
        eMajor, 
        bMajor, 
        gbMajor,
        dbMajor,
        abMajor,
        ebMajor,
        bbMajor,
        fMajor,
]

#Circle of Fifths: Minor
cof_minor = [
        aMinor,
        eMinor,
        bMinor,
        fsharpMinor,
        csharpMinor,
        abMinor,
        ebMinor,
        bbMinor,
        fMinor,
        cMinor,
        gMinor,
        dMinor,
]

# Major Chordal Relationships
def get_mode(mode, scale):
    # i.e. get_mode(lydian, cMajor): [F, G, A, B, C, D, E]
    if mode == "ionian" or mode == "one":
        return scale
    elif mode == "dorian" or mode == "two":
        dorian = scale[1:]
        dorian.append(scale[0])
        return dorian
    elif mode == "phrygian" or mode == "three":
        phrygian = scale[2:]
        for note in scale[:2]:
            phrygian.append(note)
        return phrygian
    elif mode == "lydian" or mode == "four":
        lydian = scale[3:]
        for note in scale[:3]:
            lydian.append(note)
        return lydian
    elif mode == "mixolydian" or mode == "dominant" or mode == "five":
        dominant = scale[4:]
        for note in scale[:4]:
            dominant.append(note)
        return dominant
    elif mode == "aeolian" or mode == "minor" or mode == "six":
        aeolian = scale[5:]
        for note in scale[:5]:
            aeolian.append(note)
        return aeolian
    elif mode == "locrian" or mode == "seven":
        locrian = scale[6:]
        for note in scale[:6]:
            locrian.append(note)
        return locrian
    else:
        return "Please enter valid mode" 

# Common Chord Progressions
chord_progression_names = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "dominant",
        "tonic",
]

def get_chord_progression(chord_progression, song):
    # Find chord progression based on starting key
    # i.e. one four five four
    # i.e. one five flat two six (currently not an option)
    for chord in chord_progression:
        if not chord in chord_progression_names:
            print "Chord isn't part of accepted progressions"
            print "i.e. 'one five six four'"
            return "ERROR" 
    song.chord_progression = chord_progression

# Scale Options
scales = {
    # Major
    ('c', 'M'): cMajor,
    ('g', 'M'): gMajor,
    ('d', 'M'): dMajor,
    ('a', 'M'): aMajor,
    ('e', 'M'): eMajor,
    ('b', 'M'): bMajor,
    ('f', 'M'): fMajor,
    ('bb', 'M'): bbMajor,
    ('eb', 'M'): ebMajor,
    ('ab', 'M'): abMajor,
    ('g#', 'M'): abMajor,
    ('db', 'M'): dbMajor,
    ('c#', 'M'): dbMajor,
    ('gb', 'M'): gbMajor,
    ('f#', 'M'): gbMajor,
    
    #Minor
    ('a', 'm'): aMinor,
    ('e', 'm'): eMinor,
    ('b', 'm'): bMinor,
    ('f#', 'm'): fsharpMinor,
    ('c#', 'm'): csharpMinor,
    ('db', 'm'): csharpMinor,
    ('ab', 'm'): abMinor,
    ('g#', 'm'): abMinor,
    ('d', 'm'): dMinor,
    ('g', 'm'): gMinor,
    ('c', 'm'): cMinor,
    ('f', 'm'): fMinor,
    ('bb', 'm'): bbMinor,
    ('eb', 'm'): ebMinor,
}

def get_scale(key, m):
    return scales[(key, m)]    

def get_relative_major(scale):
    # Only works if passed a minor scale 
    first_note = scale[0]
    for major_scale in cof_major:
        if major_scale[0][5] == first_note:
            return str(major_scale[1]) + ": " + str(major_scale[0])

def get_relative_minor(scale):
    # Only works if passed a major scale
    first_note = scale[0]
    for minor_scale in cof_minor:
        if minor_scale[0][2] == first_note:
            return str(minor_scale[1]) + ": " + str(minor_scale[0])

def get_parallel_major(scale):
    # Only works if passed a minor scale
    first_note = scale[0]
    for major_scale in cof_major:
        if major_scale[0][0] == first_note:
            return str(major_scale[1]) + ": " + str(major_scale[0])

def get_parallel_minor(scale):
    # Only works if passed a major scale
    first_note = scale[0]
    for minor_scale in cof_minor:
        if minor_scale[0][0] == first_note:
            return str(minor_scale[1]) + ": " + str(minor_scale[0])

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

    def cp_melody(self):
        if not self.chord_progression == None:
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
            print "No chord progression selected"

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
