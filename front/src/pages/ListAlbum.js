import React, { useEffect, useState } from 'react';
import api from '../api.js';
import NavBar from '../components/Navbar.js';

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
        <div>
            {/* <NavBar /> */}
            <div className='container'>
                <table className='table table-striped table-bordered table-hover'>
                    <thead>
                        <th>Titre</th>
                        <th>Couverture</th>
                        <th>Date de sortie</th>
                    </thead>
                    <tbody>
                        {albums.map((album) => (
                            <tr key={album.id}>
                                <td>{album.title}</td>
                                <td>{album.cover}</td>
                                <td>{album.release_date}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
        
    )
}

export default ListAlbum;
