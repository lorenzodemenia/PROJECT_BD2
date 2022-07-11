import json

from app import *
from auth import *
from stats import *
from stats import take_song, take_playlist, type_exists, count_type
from struttura_db import *


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


@app.route('/artist_page',  methods=['GET', 'POST'])
def artist_page():

    artist_user = db.session.query(Artists).filter(Artists.id_artists == current_user.id_users).first()

    user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'Netflix-avatar.png')

    type_list = stats_types()

    return render_template('Profile/profile.html', artist=artist_user, user_image=user_image, type=type_list)















