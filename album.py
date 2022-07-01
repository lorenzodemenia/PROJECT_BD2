from views import *
from app import *


@app.route('/album_list', methods=['GET', 'POST'])
def album_list():
    return render_template('Album/album.html')
