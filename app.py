from views import *


@app.route('/<int:id_artists>')
@login_required
def artist(id_artists):
    artist = get_artist(id_artists)
    return render_template('/Home/artist.html', artist=artist)


@app.route('/add')
@login_required
def add():

    check = current_user.is_artist()#Un check in più non fa mai male...
    if check:
        return render_template('/Home/add.html')
    else:
        render_template('/Home/home.html')


@app.route('/add_album')
@login_required
def add_album():

    return render_template('/Home/add_album.html')


@app.route('/add_single')
@login_required
def add_single():

    return render_template('/Home/add_single.html')


if __name__ == '__main__':
    app.run()

