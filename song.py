from random import randint

# Scales
cMajor = ["C", "D", "E", "F", "G", "A", "B"]
gMajor = ["G", "A", "B", "C", "D", "E", "F#"]

# Scale Options

scales = {
    ('c', 'M'): cMajor,
    ('g', 'M'): gMajor,
}

# Song Options

options = (
    "'scale': print scale",
    "'8notes': print 8 random notes",
    "'h': help",
    "'e': exit song",
)

def check_scale_options(i, song):
    if i == 'scale':
        song.printScale()
    elif i == '8notes':
        song.random8Notes()
    elif i == 'h':
        for option in options:
            print option

def get_scale(key, m):
    return scales[(key, m)]    

class Song:
    
    def __init__(self, scale):
        self.scale = scale

    def printScale(self):
        print self.scale

    def random8Notes(self):
        eightNotes = []
        for x in range(0, 8):
            num = randint(0, len(self.scale)-1)
            eightNotes.append(cMajor[num])
        print "Random 8 Notes: " + str(eightNotes)

    def random16Notes(self):
        sixteenNotes = []
        for x in range(0, 8):
            num = randint(0, len(self.scale)-1)
            sixteenNotes.append(self.scale[num])
        print "Random 8 Notes: " + str(sixteenNotes)

def create_song():
    print "Input Key: (c, g)"
    key = raw_input('>>> ')
    print "Major or Minor? (M or m)"
    m_m = raw_input('>>> ')
    scale = get_scale(key, m_m)
    song = Song(scale)
    song.printScale()
    return song

def song_options(song):
    while True:
        print "What would you like to do with this song?"
        i = raw_input('>>> ')
        if i == 'e':
            break
        else:
            check_scale_options(i, song)
