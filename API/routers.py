from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from auth import get_current_user

router = APIRouter()

class UserBase(BaseModel):
	name: str
	email: str 
	password: str

class UserModel(UserBase):
	id: int

	class Config:
		orm_mode = True

class ArtistBase(BaseModel):
	name: str
	avatar: str
	biography: str

class ArtistModel(ArtistBase):
	id: int

	class Config:
		orm_mode = True

class AlbumBase(BaseModel):
	title: str
	cover: str
	artist_id: int
	release_date: str

class AlbumModel(AlbumBase):
	id: int

	class Config:
		orm_mode = True

class GenreBase(BaseModel):
	name: str
	
class GenreModel(GenreBase):
	id: int

	class Config:
		orm_mode = True

class SongBase(BaseModel):
	title: str
	album_id: int
	artist_id: int
	release_date: str

class SongModel(SongBase):
	id: int

	class Config:
		orm_mode = True

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[UserModel, Depends(get_current_user)]

models.Base.metadata.create_all(bind=engine)

# Endpoints

# Users
# Créer un nouvel utilisateur
@router.post("/api/users/signup", response_model=UserModel)
async def create_user(user: UserBase, db: db_dependency):
	db_user = models.User(**user.dict())
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

# Supprimer un utilisateur par id
@router.delete("/api/users/{user_id}", response_model=UserModel)
async def delete_user(initiator: user_dependency ,user_id: int, db: db_dependency):
	if initiator is None:
		raise HTTPException(status_code=401, detail="Vous n'êtes pas autorisé à effectuer cette action")
	db_user = db.query(models.User).filter(models.User.id == user_id).first()
	if db_user is None:
		raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
	db.delete(db_user)
	db.commit()
	return db_user

# Albums
# Récupère la liste de tous les albums
@router.get("/api/albums/", response_model=List[AlbumModel])
async def get_albums(db: db_dependency):
	albums = db.query(models.Album).all()
	return albums

# Récupère les détails de l'album précisé par id
@router.get("/api/albums/{album_id}", response_model=AlbumModel)
async def get_album(album_id: int, db: db_dependency):
	album = db.query(models.Album).filter(models.Album.id == album_id).first()
	if not album:
		raise HTTPException(status_code=404, detail="Aucun album trouvé")
	return album

# Ajout d'un album
@router.post("/api/albums/", response_model=AlbumModel)
async def create_album(album: AlbumBase, db: db_dependency):
	db_album = models.Album(**album.dict())
	db.add(db_album)
	db.commit()
	db.refresh(db_album)
	return db_album

# Supprimer un album par id
@router.delete("/api/albums/{album_id}", response_model=AlbumModel)
async def delete_album(initiator: user_dependency, album_id: int, db: db_dependency):
	if initiator is None:
		raise HTTPException(status_code=401, detail="Vous n'êtes pas autorisé à effectuer cette action")
	db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
	if db_album is None:
		raise HTTPException(status_code=404, detail="Album non trouvé")
	db.delete(db_album)
	db.commit()
	return db_album

# Genres
# Récupère la liste de tous les genres
@router.get("/api/genres", response_model=List[GenreModel])
async def get_genres(db: db_dependency):
	genres = db.query(models.Genre).all()
	return genres

# Artists
# Get all artists
@router.get("/api/artists", response_model=List[ArtistModel])
async def get_artists(db: db_dependency):
	artists = db.query(models.Artist).all()
	return artists

# Get artist's detail using the artist ID
@router.get("/api/artists/{artist_id}", response_model=ArtistModel)
async def get_artist_detail(artist_id: int, db: db_dependency):
	db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
	if not db_artist:
		raise HTTPException(status_code=404, detail="Aucun artiste avec l'ID demandé")
	return db_artist

# Supprimer un artiste par id
@router.delete("/api/artists/{artist_id}", response_model=ArtistModel)
async def delete_artist(initiator: user_dependency, artist_id: int, db: db_dependency):
	if initiator is None:
		raise HTTPException(status_code=401, detail="Vous n'êtes pas autorisé à effectuer cette action")
	db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
	if db_artist is None:
		raise HTTPException(status_code=404, detail="Artiste non trouvé")
	db.delete(db_artist)
	db.commit()
	return db_artist

# Songs
# Get all songs from an album using the album ID
@router.get("/api/albums/{album_id}/songs", response_model=List[SongModel])
async def read_songs_from_album(album_id: int, db: db_dependency):
	songs = db.query(models.Song).filter(models.Song.album_id == album_id).all()
	if not songs:
		raise HTTPException(status_code=404, detail="Album not found or no songs available")
	return songs

# Get all songs from an artist using the artist ID
@router.get("/api/artists/{artist_id}/songs", response_model=List[SongModel])
async def read_songs_from_artist(artist_id: int, db: db_dependency):
	songs = db.query(models.Song).filter(models.Song.artist_id == artist_id).all()
	if not songs:
		raise HTTPException(status_code=404, detail="Artist not found or no songs available")
	return songs

# Add a new song to an album using the album ID
@router.post("/api/albums/{album_id}/songs", response_model=SongModel)
async def create_song_for_album(album_id: int, song: SongBase, db: db_dependency):
	album = db.query(models.Album).filter(models.Album.id == album_id).first()
	if not album:
		raise HTTPException(status_code=404, detail="Album not found")
	new_song = models.Song(**song.model_dump())
	new_song.album_id = album_id
	db.add(new_song)
	db.commit()
	db.refresh(new_song)
	return new_song

# Modify an artist's information using the artist ID
@router.put("/api/artists/{artist_id}", response_model=ArtistModel)
async def update_artist(artist_id: int, artist: ArtistBase, db: db_dependency):
	db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
	if not db_artist:
		raise HTTPException(status_code=404, detail="Artist not found")
	for key, value in artist.dict().items():
		setattr(db_artist, key, value)
	db.commit()
	db.refresh(db_artist)
	return db_artist

# Modify an album's information using the album ID
@router.put("/api/albums/{album_id}", response_model=AlbumModel)
async def update_album(album_id: int, album: AlbumBase, db: db_dependency):
	db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
	if not db_album:
		raise HTTPException(status_code=404, detail="Album not found")
	for key, value in album.dict().items():
		setattr(db_album, key, value)
	db.commit()
	db.refresh(db_album)
	return db_album

# Modify a genre's information using the genre ID
@router.put("/api/genres/{genre_id}", response_model=GenreModel)
async def update_genre(genre_id: int, genre: GenreBase, db: db_dependency):
	db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
	if not db_genre:
		raise HTTPException(status_code=404, detail="Genre not found")
	for key, value in genre.dict().items():
		setattr(db_genre, key, value)
	db.commit()
	db.refresh(db_genre)
	return db_genre