import json

from app import *
from auth import *
from struttura_db import *


def is_artist():
    art = db.session.query(Artists).filter(Artists.id_artists == current_user.id_users)
    count = 0
    for a in art:
        count = count +1

    if count >= 1:
        return True
    return False


def count_song(id_song):

    song = db.session.query(SongsListened).filter(SongsListened.id_songs == id_song)
    x = 0
    for s in song:
        x = x + s.num_times
    return x


def id_play():
    playlist = db.session.query(Playlist).order_by(Playlist.id_playlist.desc()).first()
    return playlist.id_playlist


def get_artist(id):
    artist = db.session.query(Artists).filter(Artists.id_artists == id).first()

    return artist


def get_artist_albums(id):
    albums = db.session.query(Album).filter(Album.id_artist == id).all()

    return albums


def get_artist_songs(id):
    songs = db.session.query(Songs).filter(Songs.id_songs == id).all()

    return songs


@app.route('/song_ar', methods=['GET', 'POST'])
@login_required
def song_ar():

    title = ( "Title", "length", "Date", "Type", "Listened")
    sl = db.session.query(Songs).filter(Songs.id_artist == current_user.id_users)
    number = []
    songs_name = []
    list_tmp = []
    count = 0
    for s in sl:
        song_tmp = []
        x = count_song(s.id_songs)
        song_tmp.append(s.title)
        song_tmp.append(s.length)
        song_tmp.append(s.date_pub)
        song_tmp.append(s.type)
        song_tmp.append(x)
        list_tmp.append(song_tmp)
        if count <= 10:
            songs_name.append(s.title)
            number.append(x)
        count = count + 1

    list_tmp.sort(key=lambda x:x[4], reverse=True)
    song_list = tuple(list_tmp)
    return render_template('Stats/Artist/songs_artist.html', headings=title, data=song_list, number=number,
                           songs_name=json.dumps(songs_name), artist_b=is_artist())


def count_album(id_album):
    al = db.session.query(SongsAlbum).filter(SongsAlbum.id_album == id_album)
    x = 0
    for a in al:
        x = x + count_song(a.id_songs)

    return x


@app.route('/album_ar', methods=['GET', 'POST'])
@login_required
def alb_ar():
    title = ("Title", "Date", "Listened")

    sl = db.session.query(Album).filter(Album.id_artist == current_user.id_users)
    number = []
    songs_name = []
    list_tmp = []
    count = 0
    for s in sl:
        song_tmp = []
        x = count_album(s.id_album)
        song_tmp.append(s.title)
        song_tmp.append(s.date_pub)
        song_tmp.append(x)
        list_tmp.append(song_tmp)
        if count <= 10:
            songs_name.append(s.title)
            number.append(x)
        count = count + 1

    list_tmp.sort(key=lambda x: x[2], reverse=True)
    song_list = tuple(list_tmp)
    return render_template('Stats/Artist/albums_artist.html', headings=title, data=song_list, number=number,
                           songs_name=json.dumps(songs_name), artist_b=is_artist())




