"""I've included a csv file ('100MostStreamedSongs.csv') in this repl that contains data from a music streaming service.

Your program should:

Read in the data.
Categorize the songs by artist, like this:
Create one empty folder per artist.
Create one blank text file per song by that artist in the relevant folder. The file name of the text file should be the name of the song."""

import csv, os

with open("100MostStreamedSongsproject56.csv", encoding="utf-8") as file:
    cleaned_file = csv.DictReader(file)
    for row in cleaned_file:
        if row["Artist(s)"] not in os.listdir():
            os.mkdir(row["Artist(s)"])
        song_name = row["Song"]
        artist_path = f"{row['Artist(s)']}/"
        file_name = os.path.join(artist_path, song_name)
        print(row["Song"])
        if file_name not in os.listdir():
            f = open(file_name, "w")
            f.close()
        