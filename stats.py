import json

import auth
from app import *
from auth import *
from struttura_db import *

user = current_user

# ---------------------------------------------------Stats page---------------------------------------------------------


def take_song(id_songs):
    song = db.session.query(Songs).filter(Songs.id_songs == id_songs).first()
    return song


def take_artist(id_songs):
    song = take_song(id_songs)
    artist = db.session.query(Artists).filter(Artists.id_artists == song.id_artist).first()
    return artist


@app.route('/stats_listener', methods=['GET', 'POST'])
def stats_listener():
    return render_template('Stats/stats_listener.html', headings=headings, data=data)


# ---------------------------------------------------Songs Stats--------------------------------------------------------

@app.route('/songs_stats', methods=['GET', 'POST'])
def songs_stats():
    title = ("Title", "length", "Date", "Type")

    song_list = ()
    sl = db.session.query(SongsListened).order_by(SongsListened.id_users)
    number = []
    songs_name = []
    for s in sl:
        if s.id_users == user.id_users:
            song_tmp = []
            prova = take_song(s.id_songs)
            song_tmp.append(prova.title)
            song_tmp.append(prova.length)
            song_tmp.append(prova.date_pub)
            song_tmp.append(prova.type)
            list_tmp = list(song_list)
            list_tmp.append(song_tmp)
            song_list = tuple(list_tmp)

            song = take_song(s.id_songs)
            songs_name.append(song.title)
            number.append(s.num_times)

    return render_template('Stats/DashStats/songs.html', headings=title, data=song_list, number=number,
                           songs_name=json.dumps(songs_name))


# ---------------------------------------------------Artists Stats------------------------------------------------------


def exists_artist(artist_id, id):
    for artist in artist_id:
        if artist == id:
            return False
    return True


def count_artist(artist_id, id):
    count = 0
    for artist in artist_id:
        prova = take_song(artist.id_songs)
        if prova.id_artist == id:
            count = count + artist.num_times
    return count


@app.route('/artists_stats', methods=['GET', 'POST'])
def artists_stats():
    title = ('Name', 'Label', 'Last Time')
    artists_list = ()
    artis_listened = db.session.query(SongsListened).filter(SongsListened.id_users == user.id_users)
    artist_id = []
    count_times = []
    artists_name = []
    for artists in artis_listened:

        listened = []
        prova = take_artist(artists.id_songs)

        if exists_artist(artist_id, prova.id_artists):
            list_tmp = list(artists_list)
            artist_id.append(prova.id_artists)
            count_times.append(count_artist(artis_listened, prova.id_artists))
            artists_name.append(prova.art_name)

            listened.append(prova.art_name)
            listened.append(prova.label)
            listened.append(artists.date_list)

            list_tmp.append(listened)
            artists_list = tuple(list_tmp)

    return render_template('Stats/DashStats/artists.html', headings=title, data=artists_list,
                           number=count_times, songs_name=json.dumps(artists_name))


# ---------------------------------------------------Playlists Stats----------------------------------------------------

def exist_playlist(playlist_id, id):
    for playlist in playlist_id:
        if playlist == id:
            return False
    return True


def take_playlist(id):
    prova = db.session.query(Playlist)

    for p in prova:
        if p.id_playlist == id:
            return p

    return 0


@app.route('/playlists_stats', methods=['GET', 'POST'])
def playlists_stats():
    headings = ['Name', 'Date Creation']
    playlist_listened = db.session.query(PlaylistUsers).filter(PlaylistUsers.id_users == user.id_users)
    playlist_list = ()
    playlist_id = []
    for playlist in playlist_listened:
        listened = []
        prova = take_playlist(playlist.id_playlist)
        if exist_playlist(listened, playlist.id_playlist):
            list_tmp = list(playlist_list)
            listened.append(prova.name)
            listened.append(prova.date_creation)
            playlist_id.append(playlist.id_playlist)

            list_tmp.append(listened)
            playlist_list = tuple(list_tmp)

    return render_template('Stats/DashStats/playlists.html', headings=headings, data=playlist_list,
                           number=[], songs_name=json.dumps(playlist_id))


# ---------------------------------------------------Type Stats--------------------------------------------------------

def type_exists(type_list, type):
    for t in type_list:
        if t == type:
            return False
    return True


def count_type(type_name, name):
    count = 0
    for type in type_name:
        prova = take_song(type.id_songs)
        if prova.type == name:
            count = count + type.num_times
    return count


@app.route('/types_stats', methods=['GET', 'POST'])
def types_stats():
    title = ['Name', 'Last Time']
    types_list = ()
    types_listened = db.session.query(SongsListened).filter(SongsListened.id_users == user.id_users)
    type_name = []
    count = []

    for type in types_listened:
        listened = []
        prova = take_song(type.id_songs)
        if type_exists(type_name, prova.type):
            list_tmp = list(types_list)
            type_name.append(prova.type)
            count.append(count_type(types_listened, prova.type))
            listened.append(prova.type)
            listened.append(type.date_list)
            list_tmp.append(listened)
            types_list = tuple(list_tmp)

    return render_template('Stats/DashStats/types.html', headings=title, data=types_list,
                           number=count, songs_name=json.dumps(type_name))
