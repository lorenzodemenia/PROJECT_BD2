import json

import auth
from app import *
from auth import *
from struttura_db import *

user = load_user(1)

# ---------------------------------------------------Stats page---------------------------------------------------------

headings = ("ID", "Title", "length", "Date", "Type")

data = ()
lol = db.session.query(SongsListened).order_by(SongsListened.id_users)

for u in lol:
    # if u.id_users==user.id_users:
    tmp = []
    tmp.append(u.id_songs)
    tmp.append(u.id_users)
    tmp.append(u.num_times)
    tmp.append(u.date_list)
    data_list = list(data)
    data_list.append(tmp)
    data = tuple(data_list)


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


def exists(artist_id, id):
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

        if exists(artist_id, prova.id_artists):
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


@app.route('/playlists_stats', methods=['GET', 'POST'])
def playlists_stats():
    return render_template('Stats/DashStats/playlists.html', headings=headings, data=data)


@app.route('/types_stats', methods=['GET', 'POST'])
def types_stats():
    return render_template('Stats/DashStats/types.html', headings=headings, data=data)
