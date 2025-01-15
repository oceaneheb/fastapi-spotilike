import React from 'react';

function NavBar() {

  return (
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <a class="nav-link" href="/albums/">Liste albums</a>
                        <a class="nav-link" href="/artists/">Liste artistes</a>
                    </div>
                </div>
            </div>
        </nav>
    </div>
  )
}

export default NavBar