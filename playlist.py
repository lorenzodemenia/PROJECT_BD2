import json

from app import *
from auth import *
from stats import *
from stats import take_song, take_playlist
from struttura_db import *


def get_playlist():
    playlist = db.session.query(PlaylistUsers).filter(PlaylistUsers.id_users == user.id_users)
    play_list = []

    for play in playlist:
        tmp = []
        p = take_playlist(play.id_playlist)
        tmp.append(p.name)
        tmp.append(play.count_song)
        tmp.append(play.id_playlist)
        play_list.append(tmp)

    return play_list


@app.route('/play_page', methods=['GET', 'POST'])
def pl_page():
    play_list = get_playlist()

    return render_template('Playlist/playlist_list.html', playlist=play_list)


def take_list_song(id_playlist):
    song = db.session.query(Songs)
    song_list = []
    for s in song:
        if not exits_song_playlist(id_playlist, s.id_songs):
            tmp = []
            tmp.append(s.id_songs)
            tmp.append(s.title)
            song_list.append(tmp)

    return song_list




@app.route('/playlist_page/<id_playlist>', methods=['GET', 'POST'])
def playlist_page(id_playlist):
    title = ("#", "Title", "Artist", "length", "Date", "Type")

    playlist = db.session.query(PlaylistSongs).filter(PlaylistSongs.id_playlist == id_playlist)
    list_tmp = []
    count = 0
    for s in playlist:
        song_tmp = []
        count = count + 1
        prova = take_song(s.id_songs)
        song_tmp.append(count)
        song_tmp.append(prova.title)
        art = db.session.query(Artists).filter(Artists.id_artists == prova.id_artist).first()
        song_tmp.append(art.art_name)
        song_tmp.append(prova.length)
        song_tmp.append(prova.date_pub)
        song_tmp.append(prova.type)
        list_tmp.append(song_tmp)

    song_list = tuple(list_tmp)
    play_list = get_playlist()
    play = take_playlist(id_playlist)
    song_choose = take_list_song(id_playlist)

    return render_template('Playlist/playlist.html', headings=title, data=song_list, playlist=play_list,
                           playlist_obj=play, song_choose=song_choose)


def count_id_playlist():
    return db.session.query(func.max(Playlist.id_playlist)).first()


def exits_song_playlist(id_playlist, id_song):
    song = db.session.query(PlaylistSongs).filter(PlaylistSongs.id_playlist == id_playlist)

    for s in song:
        if s.id_songs == id_song:
            return True
    return False


@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'POST':
        lol = count_id_playlist()

        id_playlist = lol[0]+1
        name = request.form['name']
        private = request.form['type']
        description = request.form['description']
        date_creation = date.today()

        if private == "True":
            playlist = Playlist(id_playlist, name, description, date_creation, True)
        else:
            playlist = Playlist(id_playlist, name, description, date_creation, False)

        db.session.add(playlist)
        db.session.commit()

        playlist_user = PlaylistUsers(user.id_users, id_playlist, 0)

        db.session.add(playlist_user)
        db.session.commit()

        return playlist_page(id_playlist)

    return render_template('Playlist/add_playlist.html')


@app.route('/addSongPlaylist/<id_song>/<id_playlist>', methods=['GET', 'POST'])
def add_song_playlist(id_song, id_playlist):

    playlist_song = PlaylistSongs(id_song, id_playlist)

    db.session.add(playlist_song)
    db.session.commit()

    return playlist_page(id_playlist)
