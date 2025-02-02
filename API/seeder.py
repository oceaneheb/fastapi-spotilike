from sqlalchemy.orm import Session
from models import User, Artist, Album, Song, Genre, SongGenre

def seed_data(session: Session):
    path_to_artists_avatars = "/assets/artists/"
    path_to_albums_covers = "/assets/albums/"

    # Seed Users
    user1 = User(name="John Doe",email="john@example.com", password="password123")
    user2 = User(name="Jane Smith", email="jane@example.com", password="password456")
    

    # Seed Artists
    artist1 = Artist(name="The Beatles", avatar=f"{path_to_artists_avatars}the-beatles.jpg", biography="Legendary band from Liverpool")
    artist2 = Artist(name="Taylor Swift", avatar=f"{path_to_artists_avatars}taylor-swift.jpg", biography="American singer-songwriter")

    # Seed Albums
	# Beatles
    album1 = Album(title="Abbey Road", artist=artist1, release_date="1969-09-26", cover=f"{path_to_albums_covers}abbey-road.jpg")
    album2 = Album(title="Sgt. Pepper's Lonely Hearts Club Band", artist=artist1, release_date="1967-05-26", cover=f"{path_to_albums_covers}club-band.jpg")
    album3 = Album(title="Revolver", artist=artist1, release_date="1966-08-05", cover=f"{path_to_albums_covers}revolver.jpg")
	# Taylor
    album4 = Album(title="1989", artist=artist2, release_date="2014-10-27", cover=f"{path_to_albums_covers}1989.jpg")
    album5 = Album(title="Red", artist=artist2, release_date="2012-10-22", cover=f"{path_to_albums_covers}red.jpg")
    album6 = Album(title="Fearless", artist=artist2, release_date="2008-11-11", cover=f"{path_to_albums_covers}fearless.jpg")

    # Seed Songs
    # Abbey Road
    song1 = Song(title="Come Together", album=album1, release_date="1969-09-26", artist_id=1)
    song2 = Song(title="Something", album=album1, release_date="1969-09-26", artist_id=1)
    song3 = Song(title="Maxwell's Silver Hammer", album=album1, release_date="1969-09-26", artist_id=1)
    # Sgt. Pepper
    song4 = Song(title="Sgt. Pepper's Lonely Hearts Club Band", album=album2, release_date="1967-05-26", artist_id=1)
    song5 = Song(title="With a Little Help from My Friends", album=album2, release_date="1967-05-26", artist_id=1)
    song6 = Song(title="Lucy in the Sky with Diamonds", album=album2, release_date="1967-05-26", artist_id=1)
	# Revolver
    song7 = Song(title="Taxman", album=album3, release_date="1966-08-05", artist_id=1)
    song8 = Song(title="Eleanor Rigby", album=album3, release_date="1966-08-05", artist_id=1)
    song9 = Song(title="Yellow Submarine", album=album3, release_date="1966-08-05", artist_id=1)
    # 1989
    song10 = Song(title="Welcome to New York", album=album4, release_date="2014-10-27", artist_id=2)
    song11 = Song(title="Blank Space", album=album4, release_date="2014-10-27", artist_id=2)
    song12 = Song(title="Style", album=album4, release_date="2014-10-27", artist_id=2)
	# Red
    song13 = Song(title="State of Grace", album=album5, release_date="2012-10-22", artist_id=2)
    song14 = Song(title="Red", album=album5, release_date="2012-10-22", artist_id=2)
    song15 = Song(title="Treacherous", album=album5, release_date="2012-10-22", artist_id=2)
	# Fearless
    song16 = Song(title="Fearless", album=album6, release_date="2008-11-11", artist_id=2)
    song17 = Song(title="Fifteen", album=album6, release_date="2008-11-11", artist_id=2)
    song18 = Song(title="Love Story", album=album6, release_date="2008-11-11", artist_id=2)

    # Seed Genres
    genre1 = Genre(name="Rock")
    genre2 = Genre(name="Pop")
    genre3 = Genre(name="Hip Hop")
    genre4 = Genre(name="Jazz")
    genre5 = Genre(name="Classical")
    genre6 = Genre(name="Electronic")
    genre7 = Genre(name="Country")
    genre8 = Genre(name="Reggae")
    genre9 = Genre(name="Blues")
    genre10 = Genre(name="Metal")

    # Add data to the session
    session.add_all([user1, user2, artist1, artist2, album1, album2, album3, album4, album5, album6, song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15, song16, song17, song18, genre1, genre2, genre3, genre4, genre5, genre6, genre7, genre8, genre9, genre10])
    
    session.commit()  # Commit the initial data to get generate the IDs

	# Fetch the IDs from the database
    song1_id = session.query(Song).filter_by(title="Come Together").first().id
    song2_id = session.query(Song).filter_by(title="Something").first().id
    song3_id = session.query(Song).filter_by(title="Maxwell's Silver Hammer").first().id
    song4_id = session.query(Song).filter_by(title="Sgt. Pepper's Lonely Hearts Club Band").first().id
    song5_id = session.query(Song).filter_by(title="With a Little Help from My Friends").first().id
    song6_id = session.query(Song).filter_by(title="Lucy in the Sky with Diamonds").first().id
    song7_id = session.query(Song).filter_by(title="Taxman").first().id
    song8_id = session.query(Song).filter_by(title="Eleanor Rigby").first().id
    song9_id = session.query(Song).filter_by(title="Yellow Submarine").first().id
    song10_id = session.query(Song).filter_by(title="Welcome to New York").first().id
    song11_id = session.query(Song).filter_by(title="Blank Space").first().id
    song12_id = session.query(Song).filter_by(title="Style").first().id
    song13_id = session.query(Song).filter_by(title="State of Grace").first().id
    song14_id = session.query(Song).filter_by(title="Red").first().id
    song15_id = session.query(Song).filter_by(title="Treacherous").first().id
    song16_id = session.query(Song).filter_by(title="Fearless").first().id
    song17_id = session.query(Song).filter_by(title="Fifteen").first().id
    song18_id = session.query(Song).filter_by(title="Love Story").first().id

    genre1_id = session.query(Genre).filter_by(name="Rock").first().id
    genre2_id = session.query(Genre).filter_by(name="Pop").first().id
    genre3_id = session.query(Genre).filter_by(name="Hip Hop").first().id
    genre4_id = session.query(Genre).filter_by(name="Jazz").first().id
    genre7_id = session.query(Genre).filter_by(name="Country").first().id

    song_genres = [
		SongGenre(song_id=song1_id, genre_id=genre1_id),
		SongGenre(song_id=song2_id, genre_id=genre1_id),
		SongGenre(song_id=song3_id, genre_id=genre1_id),
		SongGenre(song_id=song4_id, genre_id=genre2_id),
		SongGenre(song_id=song5_id, genre_id=genre2_id),
		SongGenre(song_id=song6_id, genre_id=genre2_id),
		SongGenre(song_id=song7_id, genre_id=genre3_id),
		SongGenre(song_id=song8_id, genre_id=genre3_id),
		SongGenre(song_id=song9_id, genre_id=genre3_id),
		SongGenre(song_id=song10_id, genre_id=genre4_id),
		SongGenre(song_id=song11_id, genre_id=genre4_id),
		SongGenre(song_id=song12_id, genre_id=genre4_id),
		SongGenre(song_id=song13_id, genre_id=genre2_id),
		SongGenre(song_id=song14_id, genre_id=genre2_id),
		SongGenre(song_id=song15_id, genre_id=genre2_id),
		SongGenre(song_id=song16_id, genre_id=genre7_id),
		SongGenre(song_id=song17_id, genre_id=genre7_id),
		SongGenre(song_id=song18_id, genre_id=genre7_id),
	]

    session.add_all(song_genres)
    session.commit()

# Usage example (ensure you have a Session instance ready):
if __name__ == "__main__":
    from database import SessionLocal

    # Initialize a session
    session = SessionLocal()
    try:
        seed_data(session)
        print("Database seeding completed.")
    finally:
        session.close()
