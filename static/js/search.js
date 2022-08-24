function clearCache(){
    location.reload()
}
function  searchPlaylist(){
    const input = document.getElementById('filter-playlist').value.toUpperCase();
    const card_playlist =  document.getElementsByClassName('prova-playlist');

    for(let i=0; i<card_playlist.length; i++){
        let title_song = card_playlist[i].querySelector(".dropdown-item");

        txtValue_song =  title_song.innerText;
        if (txtValue_song.toUpperCase().indexOf(input) > -1) {
            card_playlist[i].style.display = "";
        } else {
            card_playlist[i].style.display = "none";
        }
    }
}

function  searchPlaylistHome(){
    const input = document.getElementById('filter-playlist-home').value.toUpperCase();
    const card_playlist =  document.getElementsByClassName('prova-home');

    for(let i=0; i<card_playlist.length; i++){
        let title_song = card_playlist[i].querySelector(".dropdown-item");

        txtValue_song =  title_song.innerText;
        if (txtValue_song.toUpperCase().indexOf(input) > -1) {
            card_playlist[i].style.display = "";
        } else {
            card_playlist[i].style.display = "none";
        }
    }
}

function  searchPlaylistSearch(){
    const input = document.getElementById('filter-playlist-search').value.toUpperCase();
    const card_playlist =  document.getElementsByClassName('prova-search');


    for(let i=0; i<card_playlist.length; i++){
        let title_song = card_playlist[i].querySelector(".dropdown-item");

        txtValue_song =  title_song.innerText;
        if (txtValue_song.toUpperCase().indexOf(input) > -1) {
            card_playlist[i].style.display = "";
        } else {
            card_playlist[i].style.display = "none";
        }
    }
}

function searchProduct(){
    const input = document.getElementById('filter').value.toUpperCase();


    // normal card, like album, playlist, artist in search page
    const cards = document.getElementsByClassName('flip-card');
    for(let i=0; i<cards.length; i++){
        let title = cards[i].querySelector(".flip-card-back h4.card-title");

        txtValue = title.textContent || title.innerText;

        if (txtValue.toUpperCase().indexOf(input) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }

    }

    // song list in search
    const card_song = document.getElementsByClassName('lol');
    for(let i=0; i<card_song.length; i++){
        let title_song = card_song[i].querySelector(".mona  ");

        txtValue_song =  title_song.innerText;
        if (txtValue_song.toUpperCase().indexOf(input) > -1) {
            card_song[i].style.display = "";
        } else {
            card_song[i].style.display = "none";
        }

    }

}