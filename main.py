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

def filter_playlist(filter_function: Callable[[Song], bool]) -> List[Song]:
    return [song for song in playlist if filter_function(song)]

def create_filter_by_artist(artist_name: str) -> Callable[[Song], bool]:
    def filter_func(song):
        return song['artist'].lower() == artist_name.lower()
    return filter_func

# =================================================================
# ===                  Interface do Usuário                     ===
# =================================================================

def show_menu():
    print("\n🎶 Gerenciador de Playlist 🎶")
    print("1. Adicionar música")
    print("2. Ver playlist")
    print("3. Filtrar por gênero")
    print("4. Filtrar por artista")
    print("5. Mostrar música mais longa")
    print("0. Sair")

def main():
    while True:
        show_menu()
        choice = input("Selecione uma opção: ")

        if choice == '1':
            title = input("Digite o título: ")
            artist = input("Digite o nome do artista: ")
            genre = input("Digite o gênero: ")

            try:
                duration = int(input("Digite a duração (em segundos): "))
                add_song(title, artist, genre, duration)
            except ValueError:
                print("\n❌ Valor para duração invalido!. Por favor digite um número.")

        elif choice == '2':
            view_playlist()

        elif choice == '3':
            genre_to_filter = input("Digite o gênero que deseja filtrar: ")
            
            filtered_songs = filter_playlist(
                lambda song: song['genre'].lower() == genre_to_filter.lower()
            )

            print(f"\n--- Músicas do gênero '{genre_to_filter}' ---")
            for song in filtered_songs:
                print(f"- '{song['title']}' de {song['artist']}")
            print("---------------------------------")
        
        elif choice == '4':
            artist_to_filter = input("Digite o artista que deseja filtrar: ")
            artist_filter = create_filter_by_artist(artist_to_filter)
            filtered_songs = filter_playlist(artist_filter)
            print(f"\n--- Músicas do artista '{artist_to_filter}' ---")
            for song in filtered_songs:
                print(f"- '{song['title']}' ({song['genre']})")
            print("-----------------------------------")

        elif choice == '5':
            longest = get_longest_song()
            if longest:
                print(f"\n🎵 Música mais longa: '{longest['title']}' com {longest['duration']} segundos.")
            else:
                print("\n A playlist esta vazia.")

        elif choice == '0':
            print("Até a próxima, tchau! 👋")
            break

        else:
            print("\n❌ Opção invalida! Por favor tente novamente.")

if __name__ == "__main__":
    main()