# =================================================================
# ===                     Implementação                         ===
# =================================================================
from typing import List, Dict, Optional, Callable, TypedDict

class Song(TypedDict):
    title: str
    artist: str
    genre: str
    duration: int

playlist: List[Song] = []

def add_song(title: str, artist: str, genre: str, duration: int) -> None:
    song = {
        'title': title,
        'artist': artist,
        'genre': genre,
        'duration': duration
    }
    playlist.append(song)
    print(f"\n✅ A música '{title}' foi adicionada a playlist com sucesso!")

def view_playlist():
    if not playlist:
        print("\n A playlist esta vazia.")
        return
    
    print("\n--- Sua Playlist ---")
    for i, song in enumerate(playlist, start=1):
        print(f"{i}. '{song['title']}' de {song['artist']} ({song['genre']}) - {song['duration']}s")
    print("---------------------")

def get_longest_song() -> Optional[Song]:
    if not playlist:
        return None
    return max(playlist, key=lambda song: song['duration'])