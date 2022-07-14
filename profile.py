import json

from app import *
from auth import *
from stats import *
from stats import take_song, take_playlist, type_exists, count_type
from struttura_db import *

list_image = ['chicken-avatar.png', 'monster-avatar.png', 'panda-avatar.png', 'penguin-avatar.png', 'yellow-avatar.jpeg',
              'Netflix-avatar.png']
artist_bool = False
# ----------------------------------------------------Artist------------------------------------------------------------


def stats_types():
    list_type = db.session.query(Songs).filter(Songs.id_artist == current_user.id_users)
    list_listened = db.session.query(SongsListened)
    end_list = []
    prova = []
    for t in list_type:
        if type_exists(prova, t.type):
            tmp = []
            prova.append(t.type)
            tmp.append(t.type)
            tmp.append(count_type(list_listened, t.type))
            end_list.append(tmp)

    return end_list


def stats_album():
    list_album = db.session.query(Album).filter(Album.id_artist == current_user.id_users)
    album = []
    count = 1
    for al in list_album:
        if count < 5:
            tmp = []
            tmp.append(al)
            tmp.append(count_album(al.id_album))
            album.append(tmp)
            count += 1
        else:
            return album

    return album


@app.route('/artist_page',  methods=['GET', 'POST'])
def artist_page():

    artist_user = db.session.query(Artists).filter(Artists.id_artists == current_user.id_users).first()

    user_image = os.path.join(app.config['UPLOAD_FOLDER'], current_user.image)

    type_list = stats_types()
    album_list = stats_album()

    artist_bool = True

    return render_template('Profile/profile_artist.html', artist=artist_user, user_image=user_image,
                           type=type_list, album=album_list)


# ----------------------------------------------------Listener----------------------------------------------------------

def listener_type(num):
    song_list = db.session.query(SongsListened).filter(SongsListened.id_users == current_user.id_users)
    type_list = []
    end_list = []

    count = 0
    for sl in song_list:
        song = take_song(sl.id_songs)
        count += 1
        if type_exists(type_list, song.type) and count <= num:
            tmp = []
            tmp.append(song.type)
            tmp.append(count_type(song_list, song.type))
            end_list.append(tmp)

    return end_list


def listener_song(num):
    song_list = db.session.query(SongsListened).filter(SongsListened.id_users == current_user.id_users)
    end_list = []
    count = 0
    for sl in song_list:
        count += 1
        if count <= num:
            tmp = []
            tmp.append(take_song(sl.id_songs))
            tmp.append(sl)
            end_list.append(tmp)

    return end_list


def listener_artist(num):

    artist_list = db.session.query(SongsListened).filter(SongsListened.id_users == current_user.id_users)
    artist_id = []
    list_tmp = []
    count = 0
    for artists in artist_list:
        prova = take_artist(artists.id_songs)
        count += 1
        if exists_artist(artist_id, prova.id_artists) and count <= num:
            listened = []
            artist_id.append(prova.id_artists)
            listened.append(prova)
            listened.append(count_artist(artist_list, prova.id_artists))
            list_tmp.append(listened)

    return list_tmp


def listener_playlist(num):
    playlist_listened = db.session.query(PlaylistUsers).filter(PlaylistUsers.id_users == current_user.id_users)
    list_tmp = []
    count = 1
    for playlist in playlist_listened:
        listened = []
        prova = take_playlist(playlist.id_playlist)
        count += 1
        if exist_playlist(listened, playlist.id_playlist) and count <= num:
            listened.append(prova)
            listened.append(take_playlist_song(playlist.id_playlist))

            list_tmp.append(listened)

    return list_tmp


@app.route('/listener_page', methods=['GET', 'POST'])
def listener_page():
    dim = 5
    user_image = os.path.join(app.config['UPLOAD_FOLDER'], current_user.image)
    type_list = listener_type(dim)
    song_list = listener_song(dim)
    artist_list = listener_artist(dim)
    playlist_list = listener_playlist(dim)

    artist_bool = False

    return render_template('Profile/profile_listener.html', user_image=user_image, type=type_list, song=song_list,
                           artist=artist_list, playlist=playlist_list)

# ----------------------------------------------------Change Icon-------------------------------------------------------


@app.route('/change_avatar', methods=['GET', 'POST'])
def change_avatar():

    images = []

    for ls in list_image:
        tmp = []
        tmp.append(os.path.join(app.config['UPLOAD_FOLDER'], ls))
        tmp.append(ls)
        images.append(tmp)

    return render_template('Profile/avatar_change.html', images=images)


@app.route('/choose_avatar/<name_avatar>', methods=['GET', 'POST'])
def choose_avatar(name_avatar):

    if request.method == 'GET':
        print(name_avatar)
        current_user.image = name_avatar
        db.session.commit()

        if artist_bool:
            return redirect(url_for('listener_page'))
        else:
            return redirect(url_for('artist_page'))

