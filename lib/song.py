class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    _all_songs = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song._all_songs.append(self)
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def all_songs(cls):
        return cls._all_songs

    @classmethod
    def show_all_songs(cls):
        if not cls._all_songs:
            print("No songs in the library.")
        else:
            for song in cls._all_songs:
                print(song)

    def __str__(self):
        return f"'{self.name}' by {self.artist} [{self.genre}]"
