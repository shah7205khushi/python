# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:36:41 2024

@author: khush
"""

class Songs:
    def __init__(self, song_name, singer, song_type):
        self.song_name = song_name
        self.singer = singer
        self.song_type = song_type

class AlbumsOfSongs(Songs):
    def __init__(self, song_name, singer, song_type, album_name):
        super().__init__(song_name, singer, song_type)
        self.album_name = album_name

class FilmSongs(Songs):
    def __init__(self, song_name, singer, song_type, film_name):
        super().__init__(song_name, singer, song_type)
        self.film_name = film_name

class Ratings(AlbumsOfSongs, FilmSongs):
    def __init__(self, song_name, singer, song_type, album_name, film_name, starred):
        AlbumsOfSongs.__init__(self, song_name, singer, song_type, album_name)
        FilmSongs.__init__(self, song_name, singer, song_type, film_name)
        self.starred = starred

    def display_details(self):
        print(f"Song Name: {self.song_name}")
        print(f"Singer: {self.singer}")
        print(f"Song Type: {self.song_type}")
        print(f"Album Name: {self.album_name}")
        print(f"Film Name: {self.film_name}")
        print(f"Rating: {self.starred} out of 5")

# Main function to read data from the user and display song details
def main():
    song_name = input("Enter the song name: ")
    singer = input("Enter the singer: ")
    song_type = input("Enter the song type: ")
    album_name = input("Enter the album name: ")
    film_name = input("Enter the film name: ")
    starred = float(input("Enter the rating (out of 5): "))

    rating = Ratings(song_name, singer, song_type, album_name, film_name, starred)
    rating.display_details()

if __name__ == "__main__":
    main()
