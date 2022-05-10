from app import *
from sign import *
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


def stats_type():
    id_user = current_user.id_users
