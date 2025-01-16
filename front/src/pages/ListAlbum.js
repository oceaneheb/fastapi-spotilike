import React, { useEffect, useState } from 'react';
import api from '../api.js';
import { Link } from 'react-router-dom';

const ListAlbum = () => {
    const [albums, setAlbums] = useState([]);

    const fetchAlbums = async () => {
        const response = await api.get('/api/albums/');
        setAlbums(response.data)
    };

    useEffect(() => {
        fetchAlbums()
    }, []);

    return (
        <div className='container'>
            <table className='table table-striped table-bordered table-hover'>
                <thead>
                    <th>Titre des albums</th>
                </thead>
                <tbody>
                    {albums.map((album) => (
                        <tr key={album.id}>
                            <td><Link to={`/album/${album.id}`}>{album.title}</Link></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
        
    )
}

export default ListAlbum;
