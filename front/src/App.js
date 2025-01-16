import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ListAlbum from "./pages/ListAlbum";
import AlbumDetails from './pages/AlbumDetails';
import './App.css';
import NavBar from "./components/Navbar";

function App() {

  return (
    <div>
        <NavBar />
        <BrowserRouter>
        <Routes>
          <Route path='/' element={<ListAlbum />}></Route>
          <Route path="/album/:id" element={<AlbumDetails />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
