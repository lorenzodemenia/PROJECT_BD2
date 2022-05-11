from app import *
from auth import *
from struttura_db import *

# ---------------------------------------------------Stats page---------------------------------------------------------

headings = ("ID", "Title", "length", "Date", "Type")

data = ()
lol = db.session.query(Songs).all()

for u in lol:
    tmp = []
    tmp.append(u.id_songs)
    tmp.append(u.title)
    tmp.append(u.length)
    tmp.append(u.date_pub)
    tmp.append(u.type)
    data_list = list(data)
    data_list.append(tmp)
    data = tuple(data_list)


@app.route('/stats_listener', methods=['GET', 'POST'])
def stats_listener():
    return render_template('Stats/stats_listener.html', headings=headings, data=data)


@app.route('/songs_stats', methods=['GET', 'POST'])
def songs_stats():
    return render_template('Stats/DashStats/songs.html', headings=headings, data=data)


@app.route('/artists_stats', methods=['GET', 'POST'])
def artists_stats():
    return render_template('Stats/DashStats/artists.html', headings=headings, data=data)


@app.route('/playlists_stats', methods=['GET', 'POST'])
def playlists_stats():
    return render_template('Stats/DashStats/playlists.html', headings=headings, data=data)


@app.route('/types_stats', methods=['GET', 'POST'])
def types_stats():
    return render_template('Stats/DashStats/types.html', headings=headings, data=data)
