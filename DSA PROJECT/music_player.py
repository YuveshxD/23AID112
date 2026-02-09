class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
class MusicPlaylist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_song

    def remove_song(self, title):
        current = self.head
        previous = None

        while current:
            if current.title == title:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Removed: {title}")
                return
            previous = current
            current = current.next

        print("Song not found")
    def show_playlist(self):
        if not self.head:
            print("Playlist is empty")
            return

        current = self.head
        print("Playlist:")
        while current:
            print(" -", current.title)
            current = current.next

    def play(self):
        current = self.head
        while current:
            print(f" Playing: {current.title}")
            current = current.next
playlist = MusicPlaylist()

playlist.add_song("Faded")
playlist.add_song("No Batidao")
playlist.add_song("Starry Eyes")
playlist.add_song("White Ferrari")

playlist.show_playlist()

playlist.play()

playlist.remove_song("Starry Eyes")

playlist.show_playlist()
