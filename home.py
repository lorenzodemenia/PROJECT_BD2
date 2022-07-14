from artist import *
from auth import *
from struttura_db import *


@app.route('/artist/<int:id_artists>')
@login_required
def artist(id_artists):
    artist = get_artist(id_artists)
    album = get_artist_albums(id_artists)
    user_image = os.path.join(app.config['UPLOAD_FOLDER'], current_user.image)

    return render_template('Home/artist.html', artist=artist, album=album, user_image=user_image)






