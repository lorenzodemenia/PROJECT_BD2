from struttura_db import *


@app.route('/')#Splashpage
def index():
    if current_user.is_authenticated:#Se l'utente è autenticato
        return redirect(url_for('home'))#Lo mando alla home
    else:
        return redirect(url_for('login'))#ALtrimenti lo faccio loggare

#----------------------------------------------------Login--------------------------------------------------------------
#Da fare: implementare l'hashing della password, fare differenza tra un listener e un artist quando questo si logga


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db.session.query(Users).filter(Users.mail == request.form['mail']).first()  # Controllo se la mail dell'user sta nel db, ergo se l'utente è registrato

        if user:  # Se effettivamente c'è un user registrato con quella mail
            user_real_pwd = db.session.query(Users).filter(Users.mail == request.form['mail']).first().pwd  # Mi faccio dare la pwd dell'utente

            if user_real_pwd is not None:
                if request.form['pwd'] == user_real_pwd:  # Controllo se la pwd del form è uguale a quella nel db
                    user = db.session.query(Users).filter(Users.mail == request.form['mail']).first()  # Mi faccio ritornare un oggetto di tipo user con tutti i campi
                    login_user(user)  # Loggo l'utente

                    return redirect(url_for('home'))
                else:
                    flash('E-mail - password combination is wrong!', category='error')

            return redirect(url_for('login'))

        else:
            flash('No user with that e-mail is registered', category='error')

            return redirect(url_for('login'))

    return render_template('login.html')
#----------------------------------------------------Homepage-----------------------------------------------------------


@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')
#----------------------------------------------------Signup-------------------------------------------------------------


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/signup_listener", methods=['GET', 'POST'])
def signup_listener():
    if request.method == 'POST':

        name = request.form['name']
        surname = request.form['surname']
        sex = request.form['sex']
        mail = request.form['mail']
        pwd = request.form['pwd']
        birth_date = request.form['birth_date']

        user = Users(name, surname, sex, mail, pwd, birth_date)
        check = db.session.query(Users).filter(Users.mail == request.form['mail']).first()

        if request.form['pwd_repeat'] == user.pwd:#Se le password sono uguali procedo con l'inserimento

            if user.mail and check:#Se la mail c'è e non è già stata usata da un altro user
                db.session.add(user)  # Aggiungo l'user da inserire
                db.session.commit()  # Apporto effettivamente l'INSERT del database
            else:#Altrimenti lo avviso che non va bene
                flash('Mail already in use!', category='error')

            return redirect(url_for('login'))
        else:#Altrimenti avviso che non combaciano!
            flash("""Passwords don't coincide!""", category='error')

    return render_template('signup_listener.html')


@app.route("/signup_artist", methods=['GET', 'POST'])
def signup_artist():
    return render_template('signup_artist.html')
#----------------------------------------------------Logout-------------------------------------------------------------


@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
#---------------------------------------------------Profile page--------------------------------------------------------


@app.route('/profile')
@login_required
def profile():
    user = current_user
    print(user.name)

    return render_template('profile.html', user=user)
#------------------------------------------------------Run app----------------------------------------------------------


if __name__ == '__main__':
    app.run()
