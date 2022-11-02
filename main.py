import json,shutil,vlc,os
songsunordered=[]
songordered=[]
print("""
░█████╗░██████╗░███████╗███╗░░██╗███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░
██╔══██╗██╔══██╗██╔════╝████╗░██║████╗░████║██║░░░██║██╔════╝██║██╔══██╗
██║░░██║██████╔╝█████╗░░██╔██╗██║██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝
██║░░██║██╔═══╝░██╔══╝░░██║╚████║██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗
╚█████╔╝██║░░░░░███████╗██║░╚███║██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝
░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░
-By Elliott Day
""")
def queue():
    jsonfloc = os.path.abspath("songs.json")
    list = []
    with open(jsonfloc, 'r') as file:
        data = json.load(file)
    i = 0
    while i == 0:
        user = input("(esc to break)What Song will be Added to Queue:")
        user = user.lower()
        if user == "esc":
            i==1
            break
        else:
            list.append(user)
    for songs in list:
        for dict in data['songs']:
            if songs in dict["SongName"]:
                songpath = (dict['Path'])
                print("Playing " + songs)
                media_player = vlc.MediaPlayer()
                media = vlc.Media(songpath)
                media_player.set_media(media)
                media_player.play()
                playfe(media_player)
    index()
def playfe(media_player):
    playf=input()
    if playf=='skip':
        media_player.set_pause(1)
    else:
        media_player.set_pause(1)
        input()
        media_player.set_pause(0)
        playfe(media_player)
def M_player(path):
    media_player = vlc.MediaPlayer()
    media = vlc.Media(path)
    media_player.set_media(media)
    media_player.play()
    pause(media_player)
def pause(media_player):
    pause1=input("ENTR to pause")
    pause1.strip().lower()
    if "esc"  in pause1:
        media_player.set_pause(1)
        index()
    else:
        media_player.set_pause(1)
        input()
        media_player.set_pause(0)
        pause(media_player)

def help():
    print("Thank you for choosing OpenMusic as your music libaray!")
    print("TYPE:\n upload-UPLOAD SOUND FILE\n play-PLAY SONG\n list-LIST SONGS\n remove-REMOVE A SONG (Deletes permanently)\n leave-LEAVE OpenMusic\n queue-QUEUE MUSIC TO PLAY IN ORDER")
    index()
def leave():
    print("Thank you!")
def choose_song():
        jsonfloc = os.path.abspath("songs.json")
        with open(jsonfloc, 'r') as file:
            data = json.load(file)
        user=input("What song do you want to play?:")
        user=user.lower()
        for dict in data['songs']:
            if user in dict["SongName"]:
                songpath=(dict['Path'])
                print("Playing "+user)
                M_player(songpath)
def remove():
    try:
        filename = os.path.abspath("songs.json")
        song = input("What song would you like to remove?:")
        with open(filename, 'r') as fp:
            data = json.load(fp)
        for dict in data['songs']:
            if song in dict["SongName"]:
                songpath = (dict['Path'])
        os.remove(songpath)
        for stuff in data["songs"]:
            if song in stuff["SongName"]:
                del stuff["SongName"]
            if stuff["Path"]==songpath:
                del stuff["Path"]
        data["songs"] = [song for song in data["songs"] if song]
        with open(filename, 'w') as fp:
            json.dump(data, fp,sort_keys=True, indent=4, separators=(",", ":"))
    except:
        print("Song Not Found")
    index()

def write_json(new_data, filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["songs"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def appendsong():
        jsonfloc=os.path.abspath("songs.json")
        with open(jsonfloc, 'r') as f:
            data = json.load(f)
        for item in data['songs']:
            if item['SongName'] in songsunordered:
                pass
            else:
                songsunordered.append(item['SongName'])

def alphabeticsort():
    appendsong()
    songordered=sorted(songsunordered)
    letters=[]
    for songs in songordered:
        adv=["the ",'a ','an ']
        for ad in adv:
            if ad in songs:
                length=len(ad)
                n=songs[length:]
                if n in letters:
                    pass
                else:
                    letters.append(n[:1].upper())
                    break
            else:
                if songs[:1].upper() in letters:
                    pass
                else:
                    letters.append(songs[:1].upper())
                    break
    for let in letters:
        print(let+")")
        for songs in songordered:
            adv=["the ",'a ','an ']
            for ad in adv:
                if ad in songs:
                    length=len(ad)
                    n=songs[length:]
                    n=n[:1].upper()
                    if n==let:
                        print(songs)
                        break
                else:
                    n=songs[:1].upper()
                    if n==let:
                        print(songs)
                        break

    index()

def sorter(dstpath):
    songname = input("What do you want to call the song?:")
    songname=songname.lower()
    songname.capitalize()
    if songname[-1:]==" ":
        songname=songname[:-1]
    filename =os.path.abspath("songs.json")
    dictionary = {
        "SongName": songname,
        "Path": dstpath
    }
    write_json(dictionary,filename)
    index()


def location():
    try:
        src_path = input("File Name:")
        fn=(os.path.basename(src_path).split('/')[-1])
        dst_path = os.path.abspath("songfolder/"+fn)
        shutil.move(src_path, dst_path)
        print("New Destination: " + dst_path)
        sorter(dst_path)
    except:
        print("Cannot find File from Path")
        index()

def index():
    user=input("Type help for manual\n")
    user.lower().strip()
    os.system('cls' if os.name == 'nt' else 'clear')
    if user=="help":
        help()
    elif user=="upload":
        location()
    elif user=="play":
        choose_song()
    elif user=="list":
        alphabeticsort()
    elif user=="leave":
        leave()
    elif user=="remove":
        remove()
    elif user=="queue":
        queue()
    else:
        print("Uknown Command")
        index()
index()
