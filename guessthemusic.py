import pygame
import random
import time

# Inisialisasi mixer
pygame.mixer.init()

# List Lagu dan Artist
songList = {
    "D:\\DS\\Code\\Music\\docs\\Likey.mp3": "Likey -> Twice",
    "D:\\DS\\Code\\Music\\docs\\BubbleGum.mp3": "Bubble Gum -> NewJeans",
    "D:\\DS\\Code\\Music\\docs\\Pop.mp3": "Pop! -> Nayeon",
    "D:\\DS\\Code\\Music\\docs\\Renegade.mp3": "Renegade -> One Ok Rock",
    "D:\\DS\\Code\\Music\\docs\\CanonRock.mp3": "Canon Rock -> Sungha Jung",
    "D:\\DS\\Code\\Music\\docs\\BadLife.mp3": "Bad Life -> Sigrid feat. Bring Me The Horizon",
    "D:\\DS\\Code\\Music\\docs\\LoveULikeThat.mp3": "Love U Like That -> Lauv",
    "D:\\DS\\Code\\Music\\docs\\LetYouDown.mp3": "Let You Down -> NF",
    "D:\\DS\\Code\\Music\\docs\\IntoTheNight.mp3": "Into The Night -> Yoasobi",
    "D:\\DS\\Code\\Music\\docs\\Unforgiven.mp3": "Unforgiven -> Le Sserafim",
}

# Merubah dict ke lis untuk list lagu
soundFiles = list(songList.keys())

# play lagu pakai mixer
def playSound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(start=90)
    pygame.mixer.music.fadeout(25000)

# acak lagu, buat cek lagu yg belum di play
def randomSong(unplayedSounds):
    return random.choice(unplayedSounds)

# menampilkan pertanyaan dan mendapatkan jawaban dari user
def answer(correctName, options):
    print(f"Lagu siapakah ini?\n")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    try:
        choice = int(input("\nMasukkan pilihan anda: ")) - 1
    except ValueError:
        print("Invalid. Masukkan angka.")
        return None

    if choice < 0 or choice >= len(options):
        print("Pilihan tidak tersedia.")
        return None

    selectedOption = options[choice]
    if selectedOption == correctName:
        print("Jawaban benar!")
        return True
    elif selectedOption == "Semua jawaban salah":
        print(f"Jawaban salah! Jawaban yang benar adalah {correctName}.")
        return False
    else:
        print(f"Jawaban salah! Jawaban yang benar adalah {correctName}.")
        return False

# Inti dari game
def main():
    score = 0
    print("\nSelamat Datang di Permainan Tebak Lagu!")
    
    # Lagu yg sudah diputar, akan disimpan di variabel playedsong
    playedSong = []

    # Cek lagu yg belum diputar
    for x in range(10):
        unplayedSong = [i for i in soundFiles if i not in playedSong]

        # cek apakah ada lagu yg belum diputar, Jika tidak ada lagu yg belum diputar, maka game selesai
        if not unplayedSong:
            print("Semua lagu sudah diputar. Game Over!")
            print(f"Skor akhir adalah: {score}")
            break

        currentSong = randomSong(unplayedSong)
        correctName = songList[currentSong]
        playedSong.append(currentSong)

        # Membuat list pilihan jawaban. isinya 1 jawaban benar, 3 jawaban salah
        options = [correctName]
        wrongOptions = [name for name in songList.values() if name != correctName]
        options += random.sample(wrongOptions, 2)
        options.append("Semua jawaban salah")
        random.shuffle(options)

        #jeda lagu untuk di play
        playSound(currentSong)
        time.sleep(3)

        # Kondisi jika jawaban benar dan salah. jika benar +1, jika salah game over
        if answer(correctName, options):
            score += 1
            print(f"Skor anda adalah: {score}\n")
        else:
            print(f"Game Over! skor akhir adalah: {score}")
            break

main()