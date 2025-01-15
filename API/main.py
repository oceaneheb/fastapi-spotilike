from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
	"http://localhost:3000"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
)

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

models.Base.metadata.create_all(bind=engine)

# Endpoints

# Users
# Créer un nouvel utilisateur
@app.post("/users/", response_model=UserModel)
async def create_user(user: UserBase, db: db_dependency):
	db_user = models.User(**user.dict())
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

# Supprimer un utilisateur par id
@app.delete("/users/{user_id}", response_model=UserModel)
async def delete_user(user_id: int, db: db_dependency):
	db_user = db.query(models.User).filter(models.User.id == user_id).first()
	if db_user is None:
		raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
	db.delete(db_user)
	db.commit()
	return db_user

# Albums
# Récupère la liste de tous les albums
@app.get("/albums/", response_model=List[AlbumModel])
async def get_albums(db: db_dependency):
	albums = db.query(models.Album).all()
	return albums

# Récupère les détails de l'album précisé par id
@app.get("/albums/{album_id}", response_model=AlbumModel)
async def get_album(album_id: int, db: db_dependency):
	album = db.query(models.Album).filter(models.Album.id == album_id).first()
	if not album:
		raise HTTPException(status_code=404, detail="Aucun album trouvé")
	return album

# Ajout d'un album
@app.post("/albums/", response_model=AlbumModel)
async def create_album(album: AlbumBase, db: db_dependency):
	db_album = models.Album(**album.dict())
	db.add(db_album)
	db.commit()
	db.refresh(db_album)
	return db_album

# Supprimer un album par id
@app.delete("/albums/{album_id}", response_model=AlbumModel)
async def delete_album(album_id: int, db: db_dependency):
	db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
	if db_album is None:
		raise HTTPException(status_code=404, detail="Album non trouvé")
	db.delete(db_album)
	db.commit()
	return db_album

# Genres
# Récupère la liste de tous les genres
@app.get("/genres", response_model=List[GenreModel])
async def get_genres(db: db_dependency):
	genres = db.query(models.Genre).all()
	return genres

# Artists
# Supprimer un artiste par id
@app.delete("/artists/{artist_id}", response_model=ArtistModel)
async def delete_artist(artist_id: int, db: db_dependency):
	db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
	if db_artist is None:
		raise HTTPException(status_code=404, detail="Artiste non trouvé")
	db.delete(db_artist)
	db.commit()
	return db_artist
@app.get("/users", response_model=List[AlbumModel])
async def read_albums(db: db_dependency, skip: int = 0, limit: int = 100):
	albums = db.query(models.Album).offset(skip).limit(limit).all()
	return albums

# Songs
# Get all songs from an album using the album ID
@app.get("/albums/{album_id}/songs", response_model=List[SongModel])
async def read_songs_from_album(album_id: int, db: db_dependency):
	songs = db.query(models.Song).filter(models.Song.album_id == album_id).all()
	if not songs:
		raise HTTPException(status_code=404, detail="Album not found or no songs available")
	return songs

# Get all songs from an artist using the artist ID
@app.get("/artists/{artist_id}/songs", response_model=List[SongModel])
async def read_songs_from_artist(artist_id: int, db: db_dependency):
	songs = db.query(models.Song).filter(models.Song.artist_id == artist_id).all()
	if not songs:
		raise HTTPException(status_code=404, detail="Artist not found or no songs available")
	return songs

# Add a new song to an album using the album ID
@app.post("/albums/{album_id}/songs", response_model=SongModel)
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
@app.put("/artists/{artist_id}", response_model=ArtistModel)
async def update_artist(artist_id: int, artist: ArtistBase, db: db_dependency):
	artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
	if not artist:
		raise HTTPException(status_code=404, detail="Artist not found")
	for key, value in artist.dict().items():
		setattr(artist, key, value)
	db.commit()
	db.refresh(artist)
	return artist
