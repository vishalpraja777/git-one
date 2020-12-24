import pywhatkit
option = input("Want to play video(1) or search(2) :")
if option == '1':
    play = input("What do you want to play: ")
    pywhatkit.playonyt(play)
else:
    search = input("What do you want to search: ")
    pywhatkit.search(search)