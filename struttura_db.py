from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import *
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy import func

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ninninu'

# Radu
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zxcvbnm@localhost:5432/db_progetto"
# Lorenzo
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:A1n3m3d123!@localhost:5432/bd2_proj"
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
    id_users = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    sex = db.Column(db.String)
    mail = db.Column(db.String, unique=True)
    pwd = db.Column(db.String)
    birth_date = db.Column(db.Date)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, name, surname, sex, mail, pwd, birth_date):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.mail = mail
        self.pwd = pwd
        self.birth_date = birth_date

    def get_id(self):
        return self.id_users

    def is_artist(self):
        art = db.session.query(Artists).filter(Artists.id_artists == self.id_users)
        count = 0
        for a in art:
            count = count + 1

        if count >= 1:
            return True
        return False


class Artists(db.Model):
    id_artists = db.Column(db.Integer, db.ForeignKey('users.id_users'), primary_key=True, )
    art_name = db.Column(db.String)
    label = db.Column(db.String)

    def __init__(self, id_artists, art_name, label):
        self.id_artists = id_artists
        self.art_name = art_name
        self.label = label


class Songs(db.Model):
    id_songs = db.Column(db.Integer, primary_key=True)
    id_artist = db.Column(db.Integer, db.ForeignKey('artists.id_artists'))
    title = db.Column(db.String)
    length = db.Column(db.Integer)
    date_pub = db.Column(db.Date)
    type = db.Column(db.String)

    def __init__(self, id_artists, title, length, date_pub, type):
        self.id_artist = id_artists
        self.title = title
        self.length = length
        self.date_pub = date_pub
        self.type = type


class Playlist(db.Model):
    id_playlist = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    date_creation = db.Column(db.Date)
    private = db.Column(db.Boolean, default=False)

    def __init__(self, id_playlist, name, description, date_creation, private):
        self.id_playlist = id_playlist
        self.name = name
        self.description = description
        self.date_creation = date_creation
        self.private = private


class Album(db.Model):
    id_album = db.Column(db.Integer, primary_key=True)
    id_artist = db.Column(db.Integer, db.ForeignKey('artists.id_artists'))
    date_pub = db.Column(db.Date)
    title = db.Column(db.String)

    def __init__(self, id_artist, date_pub, title):
        self.id_artist = id_artist
        self.date_pub = date_pub
        self.title = title


class PlaylistSongs(db.Model):
    id_songs = db.Column(db.Integer, db.ForeignKey('songs.id_songs'), primary_key=True)
    id_playlist = db.Column(db.Integer, db.ForeignKey('playlist.id_playlist'), primary_key=True)

    def __init__(self, id_songs, id_playlist):
        self.id_songs = id_songs
        self.id_playlist = id_playlist


class PlaylistUsers(db.Model):
    id_users = db.Column(db.Integer, db.ForeignKey('users.id_users'), primary_key=True)
    id_playlist = db.Column(db.Integer, db.ForeignKey('playlist.id_playlist'), primary_key=True)
    count_song = db.Column(db.Integer)

    def __init__(self, id_users, id_playlist, count_song):
        self.id_users = id_users
        self.id_playlist = id_playlist
        count_song = count_song


class SongsAlbum(db.Model):
    id_album = db.Column(db.Integer, db.ForeignKey('album.id_album'), primary_key=True)
    id_songs = db.Column(db.Integer, db.ForeignKey('songs.id_songs'), primary_key=True)

    def __init__(self, id_album, id_songs):
        self.id_songs = id_album
        self.id_album = id_songs


class SongsListened(db.Model):
    id_songs = db.Column(db.Integer, db.ForeignKey('songs.id_songs'), primary_key=True)
    id_users = db.Column(db.Integer, db.ForeignKey('users.id_users'), primary_key=True)
    num_times = db.Column(db.Integer)
    date_list = db.Column(db.Date)

    def __init__(self, id_songs, id_users, num_times, date_list):
        self.id_songs = id_songs
        self.id_users = id_users
        self.num_times = num_times
        self.date_list = date_list


db.create_all()
