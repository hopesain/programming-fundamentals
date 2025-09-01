class VLC:
    def __init__(self, video_name: str):
        self.video_name = video_name

    def play(self):
        self.__locate_video()
        self.__decode()
        self.__render()
        print(f"Playing the video")

    def __locate_video(self):
        print(f"Locating the video location of {self.video_name}")

    def __decode(self):
        print(f"Decoding the video {self.video_name}")

    def __render(self):
        print(f"Rendering the video {self.video_name}")

first_video = VLC("interstellar.mp4")
first_video.play()
