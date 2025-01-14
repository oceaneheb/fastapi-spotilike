from database import Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    avatar = Column(String)
    biography = Column(String)
    albums = relationship("Album", back_populates="artist") # One-to-many
    songs = relationship("Song", back_populates="artist") # One-to-many

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))
    release_date = Column(String)
    artist = relationship("Artist", back_populates="songs") # Many-to-One
    album = relationship("Album", back_populates="songs") # Many-to-One
    genres = relationship("Genre", secondary="song_genre", back_populates="songs") # Many-to-many relationship with Genre through the association table

class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    cover = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    release_date = Column(String)
    artist = relationship("Artist", back_populates="albums") # Many-to-One
    songs = relationship("Song", back_populates="album") # One-to-many

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    songs = relationship("Song", secondary="song_genre", back_populates="genres") # Many-to-many

# Association table for many-to-many relationship between Song and Genre
class SongGenre(Base):
    __tablename__ = "song_genre"

    song_id = Column(Integer, ForeignKey("songs.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)
    
