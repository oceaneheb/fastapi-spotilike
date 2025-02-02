import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api.js';

const AlbumDetails = () => {
    const { id } = useParams();
    const [album, setAlbum] = useState(null);

    const fetchAlbumDetails = async () => {
        const response = await api.get(`/api/albums/${id}/`);
        setAlbum(response.data);
    };

    useEffect(() => {
        fetchAlbumDetails();
    }, [id]);

    if (!album) {
        return <div>Chargement...</div>;
    }

    return (
        <div className="container">
            <h1 style={{marginBottom: '30px'}}>{album.title}</h1>
            <img src={album.cover} alt={album.title} style={{ width: '300px', marginBottom: '30px' }} />
            <p><strong>Date de sortie :</strong> {album.release_date}</p>
            {/* <p><strong>Description :</strong> {album.description}</p> */}
        </div>
    );
};

export default AlbumDetails;
