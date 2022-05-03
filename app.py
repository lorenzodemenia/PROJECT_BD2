from create import *

db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    user = db.session.query(Users)

    for r in user:
        print(r.name)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
