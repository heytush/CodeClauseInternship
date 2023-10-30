import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed

        while pygame.mixer.music.get_busy():
            continue
    except pygame.error:
        print("Could not play the music. Please check the file path.")

    pygame.quit()

if __name__ == "__main__":
    print("Simple Music Player")
    file_path = input("Enter the path to the music file (e.g., 'song.mp3'): ")

    play_music(file_path)
