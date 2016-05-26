from scales import major_scales, minor_scales, cof_major, cof_minor, get_mode, chord_progression_names, get_chord_progression, scales, get_scale, get_relative_major, get_relative_minor, get_parallel_major, get_parallel_minor, get_fifth_chord, get_seventh_chord, print_cof_major, print_cof_minor

# Song Options
options = (
    "'scale': print scale",
    "'print cp': print chord progression",
    "'8notes': print 8 random notes",
    "'16notes': print 16 random notes",
    "'random melody cp': print 4 notes per chord in progression",
    "'stepwise melody cp': print 4 stepwise notes per chord in progression",
    "'get mode <mode>': get mode from song key",
    "'get relative <major/minor>': get relative minor/major key",
    "'get parallel <major/minor>': get parallel minor/major key",
    "'get base chord': get 1, 3, 5 of song scale",
    "'get seventh chord': get 1, 3, 5, 7 of song scale:",
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
    elif i == 'random melody cp':
        song.cp_random_melody()
    elif i == 'stepwise melody cp':
        song.cp_stepwise_melody()
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
    elif i == 'get base chord':
        chord = get_fifth_chord(song.scale)
        print chord
    elif i == 'get seventh chord':
        chord = get_seventh_chord(song.scale)
        print chord
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
                print_cof_major()
            elif chord_type == 'minor':
                print_cof_minor()
            else:
                print "Please use valid circle of fifths type"
        else:
            print "Please enter circle of fifths type"
    elif i == 'h' or i == 'help':
        for option in options:
            print option
