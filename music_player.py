import os


def available_songs():
    print("Please select the serial no. of the ringtone from below shown options :\n",
          "1. Hyouka-Sicilienne OST\n",
          "2. Moonlight Sonata-Eminence in Shadow\n",
          "3. Loki Theme Music\n",
          "4. Blue Lock Ending Theme\n",
          "5. Requiem Aranea-Hunter X Hunter\n",
          "6. Next To You-Parasyte\n",
          "7. Assassin's Creed Rogue\n")


def play_song(name):
    address = os.getcwd() + f"/ringtones/{name}.mp3"
    os.startfile(address)


if __name__ == '__main__':
    play_song("7th")
