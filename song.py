from random import randint

# Song Options
options = (
    "'scale': print scale",
    "'8notes': print 8 random notes",
    "'16notes': print 16 random notes",
    "'get mode <mode>': get mode from song key",
    "'h': help",
    "'e': exit song",
)

def check_scale_options(i, song):
    if i == 'scale':
        song.printScale()
    elif i == '8notes':
        song.random8Notes()
    elif i == '16notes':
        song.random16Notes()
    elif i[:8] == 'get mode':
        a = i.split(' ')
        if len(a) > 2:
            mode = a[2]
            new_scale = get_mode(mode, song.scale)
            print new_scale
        else:
            print "Please input mode name"
    elif i == 'h':
        for option in options:
            print option

# Major Scales
cMajor = ["C", "D", "E", "F", "G", "A", "B"]
gMajor = ["G", "A", "B", "C", "D", "E", "F#"]
dMajor = ["D", "E", "F#", "G", "A", "B", "C#"]
aMajor = ["A", "B", "C#", "D", "E", "F#", "G#"]
eMajor = ["E", "F#", "G#", "A", "B", "C#", "D#"]
bMajor = ["B", "C#", "D#", "E", "F#", "G#", "A#"]
fMajor = ["F", "G", "A", "Bb", "C", "D", "E"]
bbMajor = ["Bb", "C", "D", "Eb", "F", "G", "A"]
ebMajor = ["Eb", "F", "G", "Ab", "Bb", "C", "D"]
abMajor = ["Ab", "Bb", "C", "Db", "Eb", "F", "G"]
dbMajor = ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"]
gbMajor = ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"]

# Minor Scales
aMinor = ["A", "B", "C", "D", "E", "F", "G"]
eMinor = ["E", "F#", "G", "A", "B", "C", "D"]
bMinor = ["B", "C#", "D", "E", "F#", "G", "A"]
fsharpMinor = ["F#", "G#", "A", "B", "C#", "D", "E"]
csharpMinor = ["C#", "D#", "E", "F#", "G#", "A", "B"]
abMinor = ["Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"]
dMinor = ["D", "E", "F", "G", "A", "Bb", "C"]
gMinor = ["G", "A", "Bb", "C", "D", "Eb", "F"]
cMinor = ["C", "D", "Eb", "F", "G", "Ab", "Bb"]
fMinor = ["F", "G", "Ab", "Bb", "C", "Db", "Eb"]
bbMinor = ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"]
ebMinor = ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"]

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
        bMinor
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
    if mode == "ionian":
        return scale
    elif mode == "dorian":
        dorian = scale[1:]
        dorian.append(scale[0])
        return dorian
    elif mode == "phrygian":
        phrygian = scale[2:]
        for note in scale[:2]:
            phrygian.append(note)
        return phrygian
    elif mode == "lydian":
        lydian = scale[3:]
        for note in scale[:3]:
            lydian.append(note)
        return lydian
    elif mode == "mixolydian" or mode == "dominant":
        dominant = scale[4:]
        for note in scale[:4]:
            dominant.append(note)
        return dominant
    elif mode == "aeolian" or mode == "minor":
        aeolian = scale[5:]
        for note in scale[:5]:
            aeolian.append(note)
        return aeolian
    elif mode == "locrian":
        locrian = scale[6:]
        for note in scale[:6]:
            locrian.append(note)
        return locrian
    else:
        return None

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

# Song Class
class Song:
    
    def __init__(self, scale):
        self.scale = scale

    def printScale(self):
        print self.scale

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

def create_song():
    print "Input Key: (c, g, d, a, e, b, f, bb, eb, ab, db, gb, c#)"
    key = raw_input('>>> ')
    print "Major or Minor? (M or m)"
    m_m = raw_input('>>> ')
    scale = get_scale(key, m_m)
    song = Song(scale)
    song.printScale()
    return song

# Song Loop
def song_options(song):
    while True:
        print "What would you like to do with this song? ('h' for help)"
        i = raw_input('>>> ')
        if i == 'e':
            break
        else:
            check_scale_options(i, song)
