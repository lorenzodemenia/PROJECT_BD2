import json

from app import *
from auth import *
from stats import *
from struttura_db import *

user = current_user


@app.route('/play_page', methods=['GET', 'POST'])
def pl_page():

    playlist = db.session.query(PlaylistUsers).filter(PlaylistUsers.id_users == user.id_users)
    play_list = []

    for play in playlist:
        tmp = []
        p = take_playlist(play.id_playlist)
        tmp.append(p.name)
        tmp.append(play.count_song)
        play_list.append(tmp)

    return render_template('Home/templates/Playlist/playlist_list.html', playlist=play_list)




