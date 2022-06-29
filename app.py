from auth import *
from search import *
from struttura_db import *
from artist import *
from auth import *

@app.route('/<int:id_artists>')
@login_required
def artist(id_artists):
    artist = get_artist(id_artists)
    return render_template('/Home/artist.html', artist=artist)


if __name__ == '__main__':
    app.run()

