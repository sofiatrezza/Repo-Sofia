music = {
    "Iron Maiden":{
        "The Number of the Beast": [
            {
                "name": "Run to the Hills",
                "duration": "3:53"
            },
            {
                "name": "Hallowed Be Thy Name",
                "duration": "7:11"
            }
        ],
        "Piece of Mind":[
            {
                "name": "Flight of Icarus",
                "duration": "3:50"
            },
            {
                "name": "The Trooper",
                "duration": "4:12"
            },
            {
                "name": "Quest for Fire",
                "duration": "3:42"
            }
        ],
        "Dance of Death":[
            {
                "name": "No More Lies",
                "duration": "7:21"
            },
            {
                "name": "Dance of Death",
                "duration": "8:36"
            }
        ]
    },
    "Guns N Roses":{
        "Use Your Illusion I":[
            {
                "name": "Live and Let Die",
                "duration": "3:02"
            },
            {
                "name": "Don't Cry",
                "duration": "4:43"
            },
            {
                "name": "November Rain",
                "duration": "8:56"
            }
        ],
        "Appetite for Destruction":[
            {
                "name": "Welcome to the Jungle",
                "duration": "4:32"
            },
            {
                "name": "Paradise City",
                "duration": "6:45"
            },
            {
                "name": "Sweet Child o' Mine",
                "duration": "5:54"
            }
        ]
    },
    "AC/DC": {
        "Back in Black": [
            {
                "name": "Hells Bells",
                "duration": "5:12"
            },
            {
                "name": "Back in Black",
                "duration": "4:15"
            }
        ]
    }
}

while True:
        menu = int(input('Please enter a valid option: \n1 Songs\n2 Select song\n3 Play queue\n4 Exit \n ->'))
        if menu == 1:
            author = ["Iron Maiden", "Guns N Roses", "AC/DC"]
            authors = int(input('Please enter your favorite author: \n1 "Iron Maiden"\n2 "Guns N Roses"\n3 "AC/DC" \n->'))
            for singer, albums in music.items():
                if singer == author[authors]:
                    print(albums)
                    for albums, songs in albums.items():
                
                        for songs in songs:
                            name = music.get("name")
                            duration = music.get("duration")
                            print(f'{name}-{duration}')
            
        elif menu == 2:
            playing = []
            song_name = input('Enter de name of the song you want to play in this format <Hells Bells>: ')
            '''for singer, albums in music.items():
                    for albums, songs in music.items():
                        for song in songs:'''
            if song_name == music.get("name"):
                playing.append(song_name) 
                print(f'Your now listening to {song_name}')
                break

        elif menu == 3:
            print(f'Play queue is {playing}')
            
        elif menu== 4:
            if input("Do you want to exit?: \nY- Yes \nN - No \n").upper() == "Y": 
                break
        else:
            continue