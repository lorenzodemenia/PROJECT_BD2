from struttura_db import *
from app import *
from struttura_db import *
from sign import *

#---------------------------------------------------Stats page---------------------------------------------------------


@app.route('/stats_listener', methods=['GET', 'POST'])
def stats_listener():
    return render_template('Stats/stats_listener.html')


def stats_type():
    id_user = current_user.id_users


