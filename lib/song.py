class Song:
    count=0
    genres=set()
    artists=set()
    genre_count={}
    artist_count={}
    def __init__(self, name, artist, genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()


    
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    
    def add_to_genres(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
        Song.genres.add(self.genre)


    def add_to_artists(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
        Song.artists.add(self.artist)



