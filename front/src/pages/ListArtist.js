import React, { useEffect, useState } from 'react';
import api from '../api.js';
import { Link } from 'react-router-dom';

const ListArtist = () => {
    const [artists, setArtists] = useState([]);

    const fetchArtists = async () => {
        const response = await api.get('/api/artists/');
        setArtists(response.data)
    };

    useEffect(() => {
        fetchArtists()
    }, []);

    return (
        <div className='container'>
            <table className='table table-striped table-bordered table-hover'>
                <thead>
                    <th>Liste des artistes</th>
                </thead>
                <tbody>
                    {artists.map((artist) => (
                        <tr key={artist.id}>
                            <td><Link to={`/artists/${artist.id}`}>{artist.name}</Link></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
        
    )
}

export default ListArtist;
