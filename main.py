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
