
# Major Scales
major_scales = {
    "cMajor": (["C", "D", "E", "F", "G", "A", "B"], 'C Major'),
    "gMajor": (["G", "A", "B", "C", "D", "E", "F#"], 'G Major'),
    "dMajor": (["D", "E", "F#", "G", "A", "B", "C#"], 'D Major'),
    "aMajor": (["A", "B", "C#", "D", "E", "F#", "G#"], 'A Major'),
    "eMajor": (["E", "F#", "G#", "A", "B", "C#", "D#"], 'E Major'),
    "bMajor": (["B", "C#", "D#", "E", "F#", "G#", "A#"], 'B Major'),
    "fMajor": (["F", "G", "A", "Bb", "C", "D", "E"], 'F Major'),
    "bbMajor": (["Bb", "C", "D", "Eb", "F", "G", "A"], 'Bb Major'),
    "ebMajor": (["Eb", "F", "G", "Ab", "Bb", "C", "D"], 'Eb Major'),
    "abMajor": (["Ab", "Bb", "C", "Db", "Eb", "F", "G"], 'Ab Major'),
    "dbMajor": (["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"], 'Db Major'),
    "gbMajor": (["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"], 'Gb Major'),
}

# Minor Scales
minor_scales = {
    "aMinor": (["A", "B", "C", "D", "E", "F", "G"], 'A Minor'),
    "eMinor": (["E", "F#", "G", "A", "B", "C", "D"], 'E Minor'),
    "bMinor": (["B", "C#", "D", "E", "F#", "G", "A"], 'B Minor'),
    "fsharpMinor": (["F#", "G#", "A", "B", "C#", "D", "E"], 'F# Minor'),
    "csharpMinor": (["C#", "D#", "E", "F#", "G#", "A", "B"], 'C# Minor'),
    "abMinor": (["Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"], 'Ab Minor'),
    "dMinor": (["D", "E", "F", "G", "A", "Bb", "C"], 'D Minor'),
    "gMinor": (["G", "A", "Bb", "C", "D", "Eb", "F"], 'G Minor'),
    "cMinor": (["C", "D", "Eb", "F", "G", "Ab", "Bb"], 'C Minor'),
    "fMinor": (["F", "G", "Ab", "Bb", "C", "Db", "Eb"], 'F Minor'),
    "bbMinor": (["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"], 'Bb Minor'),
    "ebMinor": (["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"], 'Eb Minor'),
}

# Diminished Scales
whole_half_diminished = {
    "wh_cdim": (["C", "D", "Eb", "F", "Gb", "Ab", "A", "B"], 'C wh Dim'),
    "wh_c#dim": (["C#", "D#", "E", "F", "G", "Ab", "Bb", "B"], 'C# wh Dim')
}

half_whole_diminished = {
    "hw_cdim": (["C", "Db", "Eb", "Fb", "Gb", "G", "A", "Bb"], 'C hw Dim'),
    "hw_c#dim": (["C#", "D", "E", "F", "G", "Ab", "Bb", "B"], 'C# hw Dim'),
}

def convert_wh_dim(scale_start):
    wh_c = whole_half_diminished["wh_cdim"]
    wh_cs = whole_half_diminished["wh_c#dim"]
    if scale == "C":
        return wh_c
    elif scale == "C#":
        return wh_cs
    

def convert_hw_dim(scale_start):
    hw_c = half_whole_diminished["hw_cdim"]
    hw_cs = half_whole_diminished["hw_c#dim"]
    if scale == "C":
        return hw_c
    elif scale == "C#":
        return hw_cs

# Circle of Fifths: Major
cof_major = [
        major_scales["cMajor"], 
        major_scales["gMajor"], 
        major_scales["dMajor"], 
        major_scales["aMajor"], 
        major_scales["eMajor"], 
        major_scales["bMajor"], 
        major_scales["gbMajor"],
        major_scales["dbMajor"],
        major_scales["abMajor"],
        major_scales["ebMajor"],
        major_scales["bbMajor"],
        major_scales["fMajor"],
]

#Circle of Fifths: Minor
cof_minor = [
        minor_scales["aMinor"],
        minor_scales["eMinor"],
        minor_scales["bMinor"],
        minor_scales["fsharpMinor"],
        minor_scales["csharpMinor"],
        minor_scales["abMinor"],
        minor_scales["ebMinor"],
        minor_scales["bbMinor"],
        minor_scales["fMinor"],
        minor_scales["cMinor"],
        minor_scales["gMinor"],
        minor_scales["dMinor"],
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
    ('c', 'M'): major_scales["cMajor"],
    ('g', 'M'): major_scales["gMajor"],
    ('d', 'M'): major_scales["dMajor"],
    ('a', 'M'): major_scales["aMajor"],
    ('e', 'M'): major_scales["eMajor"],
    ('b', 'M'): major_scales["bMajor"],
    ('f', 'M'): major_scales["fMajor"],
    ('bb', 'M'): major_scales["bbMajor"],
    ('eb', 'M'): major_scales["ebMajor"],
    ('ab', 'M'): major_scales["abMajor"],
    ('g#', 'M'): major_scales["abMajor"],
    ('db', 'M'): major_scales["dbMajor"],
    ('c#', 'M'): major_scales["dbMajor"],
    ('gb', 'M'): major_scales["gbMajor"],
    ('f#', 'M'): major_scales["gbMajor"],
    
    #Minor
    ('a', 'm'): minor_scales["aMinor"],
    ('e', 'm'): minor_scales["eMinor"],
    ('b', 'm'): minor_scales["bMinor"],
    ('f#', 'm'): minor_scales["fsharpMinor"],
    ('c#', 'm'): minor_scales["csharpMinor"],
    ('db', 'm'): minor_scales["csharpMinor"],
    ('ab', 'm'): minor_scales["abMinor"],
    ('g#', 'm'): minor_scales["abMinor"],
    ('d', 'm'): minor_scales["dMinor"],
    ('g', 'm'): minor_scales["gMinor"],
    ('c', 'm'): minor_scales["cMinor"],
    ('f', 'm'): minor_scales["fMinor"],
    ('bb', 'm'): minor_scales["bbMinor"],
    ('eb', 'm'): minor_scales["ebMinor"],
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

# Chords

def get_fifth_chord(scale):
    # Get 1, 3, 5 of scale
    # i.e. get_fifth(cMajor) returns ['C', 'E', 'G']
    return [scale[0], scale[2], scale[4]]

def get_seventh_chord(scale):
    # Get 1, 3, 5, 7 of scale
    # i.e. get_seventh(cMajor) returns ['C', 'E', 'G', 'B']
    return [scale[0], scale[2], scale[4], scale[6]]
