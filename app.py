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
        #Qua dentro mi salvo gli id delle canzoni che ho appena inserito
        song_ids = []

        #Inserisco con un ciclo for le canzoni
        for i in range(0, counter):
            song = Songs(current_user.id_users, titles[i], lengths[i], date.today(), genres[i])
            # Aggiungo la canzone
            db.session.add(song)
            db.session.commit()
            # Mi salvo il
            song_ids.append(last_song_id())

        # Associo le canzoni inserite all'album inserito
        x = song_ids.__len__()

        for j in range(0, x):
            print('Provo a inserire:')
            print(last_album_id(), song_ids[j])

            song_album = SongsAlbum(last_album_id(), song_ids[j])

            db.session.add(song_album)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template('Album/add_album.html')

def last_song_id():
    # So che l'id è sequenziale, quindi ritorno il valore massimo
    return db.session.query(func.max(Songs.id_songs)).first()[0]

def last_album_id():
    # So che l'id è sequenziale, quindi ritorno il valore massimo
    return db.session.query(func.max(Album.id_album)).first()[0]


@app.route('/add_single')
@login_required
def add_single():

    return render_template('Home/add_single.html')


if __name__ == '__main__':
    app.run()

