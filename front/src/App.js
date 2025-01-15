import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ListAlbum from "./pages/ListAlbum";
import './App.css';
import NavBar from "./components/Navbar";

function App() {

  return (
    <div>
        <NavBar />
        <BrowserRouter>
        <Routes>
          <Route path='/albums/' element={<ListAlbum />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
