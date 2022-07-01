import json

from app import *
from auth import *
from stats import *
from stats import take_song, take_playlist
from struttura_db import *

user = current_user


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


@app.route('/playlist/<id_playlist>', methods=['GET', 'POST'])
def playlist_page(id_playlist=None):
    title = ("#", "Title", "length", "Date", "Type")

    playlist = db.session.query(PlaylistSongs).filter(PlaylistSongs.id_playlist == id_playlist)

    list_tmp = []
    count = 0
    for s in playlist:
        song_tmp = []
        count = count + 1
        prova = take_song(s.id_songs)
        song_tmp.append(count)
        song_tmp.append(prova.title)
        song_tmp.append(prova.length)
        song_tmp.append(prova.date_pub)
        song_tmp.append(prova.type)
        list_tmp.append(song_tmp)

    song_list = tuple(list_tmp)
    play_list = get_playlist()
    play = take_playlist(id_playlist)

    return render_template('Playlist/playlist.html', headings=title, data=song_list, playlist=play_list,
                           playlist_obj=play)
