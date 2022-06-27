from auth import *
from search import *
from struttura_db import *
from artist import *
from auth import *

@app.route('/artist')
@login_required
def artist():

    return render_template('artist')


if __name__ == '__main__':
    app.run()

