from create import *


@app.route('/')
def hello_world():  # put application's code here
    user = db.session.query(Album)

    for r in user:
        print(r.title)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
