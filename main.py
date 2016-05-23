from song import Song, create_song, song_options

# Option Dictionary

options = (
    "'c': create song",
    "'h': help",
    "'q', 'e', 'exit', or 'quit': quit program",
)

def checkOptions(i):
    song = None 
    if i == 'c':
        song = create_song()
    elif i == 'h':
        for option in options:
            print option
    elif i == 'q' or i == 'e' or i == 'exit' or i == 'quit':
        exit()
    if not song == None:
        return song

if __name__ == "__main__":
    while True:
        print "What would you like to do? ('h' for help)"
        i = raw_input('>>> ')
        song = checkOptions(i)
        if song:
            song_options(song)
        song = None 
