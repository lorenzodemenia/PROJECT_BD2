from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ninninu'

# Radu
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zxcvbnm@localhost:5432/db_progetto"
# Lorenzo
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:A1n3m3d123!@localhost:5432/bd2_proj"
# Daniele
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Internet10@localhost:5432/bd2progetto"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(id_users):
    user = db.session.query(Users).filter(Users.id_users == id_users).first()

    return user


class Users(UserMixin, db.Model):
    id_users = db.Column(db.VARCHAR(50), primary_key=True)
    name = db.Column(db.VARCHAR(50))
    surname = db.Column(db.VARCHAR(50))
    sex = db.Column(db.VARCHAR(1))
    mail = db.Column(db.VARCHAR(50), unique=True)
    pwd = db.Column(db.VARCHAR(100))
    birth_date = db.Column(db.Date)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, id_users, name, surname, mail, birth_date, authenticated):
        self.id_users = id_users
        self.name = name
        self.surname = surname
        self.mail = mail
        self.birth_date = birth_date
        self.authenticated = authenticated

    def get_id(self):
        return self.id_users


class Artists(db.Model):
    id_artists = db.Column(db.VARCHAR(50), db.ForeignKey('users.id_users'), primary_key=True, )
    art_name = db.Column(db.VARCHAR(50))
    label = db.Column(db.VARCHAR(50))

    def __init__(self, id_artists, art_name, label):
        self.id_artists = id_artists
        self.art_name = art_name
        self.label = label


class Songs(db.Model):
    id_songs = db.Column(db.VARCHAR(50), primary_key=True)
    id_artist = db.Column(db.VARCHAR(50), db.ForeignKey('artists.id_artists'))
    title = db.Column(db.VARCHAR(50))
    length = db.Column(db.Integer)
    date_pub = db.Column(db.Date)

    def __init__(self, id_songs, id_artists, title, length, date_pub):
        self.id_artist = id_artists
        self.id_songs = id_songs
        self.title = title
        self.length = length
        self.date_pub = date_pub


class Playlist(db.Model):
    id_playlist = db.Column(db.VARCHAR(50), primary_key=True)
    date_creation = db.Column(db.Date)
    type = db.Column(db.Boolean)

    def __init__(self, id_playlist, date_creation, type):
        self.id_playlist = id_playlist
        self.date_creation = date_creation
        self.type = type


class Album(db.Model):
    id_album = db.Column(db.VARCHAR(50), primary_key=True)
    date_pub = db.Column(db.Date)
    title = db.Column(db.VARCHAR(50))

    def __init__(self, id_album, date_pub, title):
        self.id_album = id_album
        self.date_pub = date_pub
        self.title = title


class PlaylistSongs(db.Model):
    id_songs = db.Column(db.VARCHAR(50), db.ForeignKey('songs.id_songs'), primary_key=True)
    id_playlist = db.Column(db.VARCHAR(50), db.ForeignKey('playlist.id_playlist'), primary_key=True)

    def __init__(self, id_songs, id_playlist):
        self.id_songs = id_songs
        self.id_playlist = id_playlist


class PlaylistUsers(db.Model):
    id_users = db.Column(db.VARCHAR(50), db.ForeignKey('users.id_users'), primary_key=True)
    id_playlist = db.Column(db.VARCHAR(50), db.ForeignKey('playlist.id_playlist'), primary_key=True)

    def __init__(self, id_users, id_playlist):
        self.id_users = id_users
        self.id_playlist = id_playlist


class SongsAlbum(db.Model):
    id_songs = db.Column(db.VARCHAR(50), db.ForeignKey('songs.id_songs'), primary_key=True)
    id_album = db.Column(db.VARCHAR(50), db.ForeignKey('album.id_album'), primary_key=True)

    def __init__(self, id_songs, id_album):
        self.id_songs = id_songs
        self.id_album = id_album


class SongsListened(db.Model):
    id_songs = db.Column(db.VARCHAR(50), db.ForeignKey('songs.id_songs'), primary_key=True)
    id_users = db.Column(db.VARCHAR(50), db.ForeignKey('users.id_users'), primary_key=True)
    num_times = db.Column(db.Integer)
    date_list = db.Column(db.Date)

    def __init__(self, id_songs, id_users, num_times, date_list):
        self.id_songs = id_songs
        self.id_users = id_users
        self.num_times = num_times
        self.date_list = date_list