import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api.js';

const ArtistDetails = () => {
    const { id } = useParams();
    const [artist, setArtist] = useState(null);

    const fetchArtistDetails = async () => {
        const response = await api.get(`/api/artists/${id}/`);
        setArtist(response.data);
    };

    useEffect(() => {
        fetchArtistDetails();
    }, [id]);

    if (!artist) {
        return <div>Chargement...</div>;
    }

    return (
        <div className="container">
            <h1 style={{marginBottom: '30px'}}>{artist.name}</h1>
            <img src={artist.avatar} alt="" style={{ width: '300px', marginBottom: '30px' }} />
            <p><strong>Biographie de l'artiste :</strong> {artist.biography}</p>
        </div>
    );
};

export default ArtistDetails;


