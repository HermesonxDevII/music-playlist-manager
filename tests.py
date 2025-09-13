import pytest

from playlist_manager import (
    add_song,
    get_longest_song,
    filter_playlist,
    create_filter_by_artist,
    playlist, 
    Song
)

# garantindo que a playlist comece sempre vazia.
@pytest.fixture(autouse=True)
def clean_playlist_before_each_test():
    playlist.clear()
    yield
    playlist.clear()

"""Verifica se a função add_song realmente adiciona uma música à lista global."""
def test_add_song_populates_playlist():
    add_song(
        title="Stairway to Heaven",
        artist="Led Zeppelin",
        genre="Rock",
        duration=482
    )
    
    # Verifica se o estado global mudou como esperado
    assert len(playlist) == 1
    assert playlist[0]['title'] == "Stairway to Heaven"
    assert playlist[0]['duration'] == 482

"""Verifica se a função retorna None quando a playlist está vazia."""
def test_get_longest_song_returns_none_for_empty_playlist():
    longest_song = get_longest_song()
    
    # Verifica o resultado
    assert longest_song is None

"""Verifica se a música mais longa é encontrada corretamente."""
def test_get_longest_song_finds_correct_song():
    add_song(
        title="Song A",
        artist="Artist X",
        genre="Pop",
        duration=180
    )
    
    add_song(
        title="The Longest Song",
        artist="Artist Y",
        genre="Rock",
        duration=500
    )
    
    add_song(
        title="Song C",
        artist="Artist Z",
        genre="Jazz",
        duration=300
    )

    longest_song = get_longest_song()

    # Verifica a música mais longa
    assert longest_song is not None
    assert longest_song['title'] == "The Longest Song"
    assert longest_song['duration'] == 500


"""Verifica a função de filtrar por gênero."""
def test_filter_playlist_by_genre():
    add_song(
        title="Rock Song 1",
        artist="Band A",
        genre="Rock",
        duration=200
    )

    add_song(
        title="Pop Song",
        artist="Band B",
        genre="Pop",
        duration=150
    )
    
    add_song(
        title="Rock Song 2",
        artist="Band C",
        genre="Rock",
        duration=250
    )
    
    rock_songs = filter_playlist(lambda song: song['genre'] == "Rock")

    assert len(rock_songs) == 2

    # Verifica se os títulos das músicas filtradas estão corretos
    titles = {song['title'] for song in rock_songs}
    assert titles == {"Rock Song 1", "Rock Song 2"}


"""Testa se a closure cria um filtro de artista que funciona corretamente."""
def test_create_filter_by_artist_closure():
    add_song(
        title="Queen Song 1",
        artist="Queen",
        genre="Rock",
        duration=355
    )

    add_song(
        title="Outra Banda",
        artist="Outra Banda",
        genre="Pop",
        duration=210
    )
    
    add_song(
        title="Queen Song 2",
        artist="Queen",
        genre="Rock",
        duration=300
    )

    queen_filter = create_filter_by_artist("Queen")
    queen_songs = filter_playlist(queen_filter)

    # Verifica os artistas das músicas filtradas
    assert len(queen_songs) == 2
    assert queen_songs[0]['artist'] == "Queen"
    assert queen_songs[1]['artist'] == "Queen"