import json

from app import *
from auth import *
from stats import *
from stats import take_song, take_playlist
from struttura_db import *


def get_album():
    album_list = db.session.query(Album).filter(Album.id_artist == user.id_users)
    album = []
    for al in album_list:
        tmp = []
        tmp.append(al)
        tmp.append(db.session.query(Artists).filter(Artists.id_artists == al.id_artist).first())
        album.append(tmp)

    return album


@app.route('/album_list_page', methods=['GET', 'POST'])
def album_list_page():

    album_list = get_album()

    return render_template('Album/album_list.html', album=album_list)


def exists_song_album(id_song, id_album):
    song_album = db.session.query(SongsAlbum).filter(SongsAlbum.id_album == id_album)

    for sa in song_album:
        if sa.id_songs == id_song:
            return True

    return False


def take_song_album(id_album):
    song_album = db.session.query(SongsAlbum).filter(SongsAlbum.id_album == id_album)
    songs = []

    for al in song_album:
        if not exists_song_album(al.id_songs, id_album):
            songs.append(al)

    return songs


@app.route('/album_page/<id_album>', methods=['GET', 'POST'])
def album_page(id_album):

    title = ("#", "Title", "Artist", "length", "Date", "Type")

    album = db.session.query(SongsAlbum).filter(SongsAlbum.id_album == id_album)
    list_tmp = []
    count = 0
    for al in album:
        song_tmp = []
        count = count + 1
        prova = take_song(al.id_songs)
        song_tmp.append(count)
        song_tmp.append(prova.title)
        art = db.session.query(Artists).filter(Artists.id_artists == prova.id_artist).first()
        song_tmp.append(art.art_name)
        song_tmp.append(prova.length)
        song_tmp.append(prova.date_pub)
        song_tmp.append(prova.type)
        list_tmp.append(song_tmp)

    song_list = tuple(list_tmp)
    album_list = get_album()
    play = db.session.query(Album).filter(Album.id_album == id_album).first()
    song_choose = take_song_album(id_album)
    artist = db.session.query(Artists).filter(Artists.id_artists == play.id_artist).first()

    return render_template('Album/album.html', headings=title, data=song_list, albums=album_list,
                           album_obj=play, artist_obj=artist, song_choose=song_choose)

