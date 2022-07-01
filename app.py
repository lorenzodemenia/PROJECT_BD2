from views import *


@app.route('/artist/<int:id_artists>')
@login_required
def artist(id_artists):
    artist = get_artist(id_artists)
    return render_template('Home/artist.html', artist=artist)


@app.route('/add')
@login_required
def add():

    check = current_user.is_artist()#Un check in più non fa mai male...
    if check:
        return render_template('/Home/add.html')
    else:
        render_template('/Home/home.html')


@app.route('/add_album', methods=['GET', 'POST'])
@login_required
def add_album():
    if request.method == 'POST':
        #Mi faccio fare il form in forma di dizionario
        form = request.form
        #Mi salvo il nome dell'album
        album_name = form.get('album_name')

        #Mi faccio delle liste con ogni parametro: titolo, lunghezza, genere
        titles = form.getlist('title')
        lengths = form.getlist('length')
        genres = form.getlist('type')
        #Conto quante canzoni devo inserire
        counter = titles.__len__()

        #Creo oggetto album
        album = Album(current_user.id_users, date.today(), album_name)

        #Aggiungo l'album al db
        db.session.add(album)
        db.session.commit()

        album_id = Album.query.filter_by(id_album=album.id_album).first()

        song_ids = []

        #Inserisco con un ciclo for le canzoni
        for i in range(0, counter):
            song = Songs(current_user.id_users, titles[i], lengths[i], date.today(), genres[i])

            db.session.add(song)
            db.session.commit()

            song_ids.append(Songs.query.filter_by(id_songs=song.id_songs).first())

        print(song_ids)

        #Associo le canzoni inserite all'album inserito


        return redirect(url_for('home'))

    return render_template('Album/add_album.html')


@app.route('/add_single')
@login_required
def add_single():

    return render_template('Home/add_single.html')


if __name__ == '__main__':
    app.run()

