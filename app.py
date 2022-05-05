from create import *


@app.route("/login", methods=['GET', 'POST'])
def login():

    return render_template('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():

    return render_template('signup.html')


@app.route('/')
def hello_world():  # put application's code here
    user = db.session.query(Users)
    for r in user:
        print(r.mail)
    return render_template('index.html', users=user)


if __name__ == '__main__':
    app.run()
