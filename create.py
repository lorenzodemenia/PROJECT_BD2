from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#CULO
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:A1n3m3d123!@localhost:5432/bd2_proj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id_users = db.Column(db.VARCHAR(50),primary_key=True)
    name = db.Column(db.VARCHAR(50))
    surname = db.Column(db.VARCHAR(50))
    mail = db.Column(db.VARCHAR(50))
    date_n = db.Column(db.Date)

    def __init__(self, id_users, name, surname, mail, date_n):
        self.id_users = id_users
        self.name = name
        self.surname = surname
        self.mail = mail
        self.date_n = date_n


class Artists(db.Model):
    __tablename__ = 'artists'

    id_artists = db.Column(db.VARCHAR(50), db.ForeignKey('users.id_users'), primary_key=True,)

    def __init__(self, id_artists):
        self.id_artists = id_artists


class Songs(db.Model):
    __tablename__ = 'songs'

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


class Playlist (db.Model):
    __tablename__= 'playlist'

    id_playlist = db.Column(db.VARCHAR(50), primary_key=True)
    date_creation = db.Column(db.Date)
    type = db.Column(db.Boolean)

    def __init__(self, id_playlist, date_creation, type):
        self.id_playlist = id_playlist
        self.date_creation = date_creation
        self.type = type


class Album(db.Model):
    __tablename__ = 'album'

    id_album = db.Column(db.VARCHAR(50), primary_key=True)
    date_pub = db.Column(db.Date)
    title = db.Column(db.VARCHAR(50))

    def __init__(self, id_album, date_pub, title):
        self.id_album = id_album
        self.date_pub = date_pub
        self.title = title


class PlaylistSongs(db.Model):
    __tablename__ = 'playlist_songs'

    id_songs = db.Column(db.VARCHAR(50), db.ForeignKey('songs.id_songs'), primary_key=True)
    id_playlist = db.Column(db.VARCHAR(50), db.ForeignKey('playlist.id_playlist'), primary_key=True)

    def __init__(self, id_songs, id_playlist):
        self.id_songs = id_songs
        self.id_playlist = id_playlist


class PlaylistUsers(db.Model):
    __tablename__ = 'playlist_users'

    id_users = db.Column(db.VARCHAR(50), db.ForeignKey('users.id_users'), primary_key=True)
    id_playlist = db.Column(db.VARCHAR(50), db.ForeignKey('playlist.id_playlist'), primary_key=True)

    def __init__(self, id_users, id_playlist):
        self.id_users = id_users
        self.id_playlist = id_playlist


class SongsAlbum(db.Model):
    __tablename__ = 'songs_album'

    id_songs = db.Column(db.VARCHAR(50), db.ForeignKey('songs.id_songs'), primary_key=True)
    id_album = db.Column(db.VARCHAR(50), db.ForeignKey('album.id_album'), primary_key=True)

    def __init__(self, id_songs, id_album):
        self.id_songs = id_songs
        self.id_album = id_album


class SongsListened(db.Model):
    __tablename__ = 'songs_listened'

    id_songs = db.Column(db.VARCHAR(50), db.ForeignKey('songs.id_songs'), primary_key=True)
    id_users = db.Column(db.VARCHAR(50), db.ForeignKey('users.id_users'), primary_key=True)
    num_times = db.Column(db.Integer)
    date_list = db.Column(db.Date)

    def __init__(self, id_songs, id_playlist, num_times, date_list):
        self.id_songs = id_songs
        self.id_playlist = id_playlist
        self.num_times = num_times
        self.date_list = date_list
