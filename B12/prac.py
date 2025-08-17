# MP3 player: music queue, current song | add song, play song, skip song
class MP3Player:
    def __init__(self):
        self.music_queue = []
        self.current_song = None

    def add_song(self, song: str):
        # them bai moi (vao cuoi danh sach)
        self.music_queue.append(song)
        print(f"Da them bai hat: {song}")

    def play_song(self):
        if len(self.music_queue):
            # lay phan tu dau danh sach
            self.current_song = self.music_queue.pop(0)
            print(f"Bai hat dang phat: {self.current_song}")
        else:
            self.current_song = None
            print("Danh sach bai hat dang trong!")

    def skip_song(self):
        if self.current_song:
            print(f"Bo qua bai hat: {self.current_song}")
            # phat tiep bai tiep theo
            self.play_song()
        else:
            print("Ko co bai hat nao dang phat de bo qua.")