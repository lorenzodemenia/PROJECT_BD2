from create import *

db.create_all()
#prova
@app.route('/')
def hello_world():  # put application's code here
    user = db.session.query(Users)

    return render_template('index.html', users=user)


if __name__ == '__main__':
    app.run()
