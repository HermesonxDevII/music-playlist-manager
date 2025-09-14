# 🐍 Atividade Parcial (Programação Funcional) - Gerenciador de Playlist 🎶

Projeto desenvolvido em **Python**.

---
## 📌 Objetivo
Aplicar os conceitos de **Programação Funcional** em um software:
- Funções **lambda**  
- **List comprehensions**  
- **Closures**  
- **Funções de alta ordem**

## 📦 Instalação

### ✅ Clonar o repositório

```bash
git clone git@github.com:HermesonxDevII/music-playlist-manager.git
cd music-playlist-manager
```

---
### ✅ Criar ambiente virtual
```bash
python -m venv venv
```
## ✅ Acessar ambiente virtual

#### ✅ Windows
```bash
venv\Scripts\activate
```

#### ✅ Linux/Mac
```bash
source venv/bin/activate
```

---
### ✅ Instalar dependências

```bash
pip install -r requirements.txt
```

---
### ✅ Executar aplicação

```bash
python main.py
```

---

## 👩‍💻 Atribuição de funções:
| Nome                                     | Matricula  | Função                     |
| ---------------------------------------- | ---------- | -------------------------- |
| [Francisco Hermeson O. dos Santos]       | [2326241]  | Desenvolvedor(a)           |
| [Maria Joselene da Costa C. de Barcelos] | [2314797]  | Desenvolvedor(a)           |
| [Francisco Clay Oliveira]                | [2317574]  | Documentação               | 
| [Francisco Tayson Araujo santos]         | [2323799]  | Testes                     | 
| [Leonardo Estevão Silva Dos Santos]      | [2315238]  | Testes                     | 

---
## ⚙️ Requisitos Funcionais
1. O sistema deve permitir adicionar uma nova música a uma playlist, com título, artista, gênero e duração.
2. O sistema deve permitir a visualização de todas as músicas cadastradas na playlist.
3. O sistema deve permitir filtrar as músicas da playlist por um gênero específico.
4. O sistema deve permitir filtrar as músicas da playlist por um artista específico.
5. O sistema deve ser capaz de encontrar e exibir a música de maior duração na playlist.

## 🚫 Requisitos Não Funcionais
- O sistema deve ser desenvolvido em **Python 3+** com anotações de tipo.
- O código deve ser publicado em um **repositório GitHub**.
- O sistema deve ser executado como uma **Interface de Linha de Comando (CLI)**.
- O sistema não deve apresentar erros em **tempo de execução**.
- O projeto deve incluir testes automatizados usando a biblioteca **Pytest**.

---
## 🧩 Estrutura do Código
- `add_song` → Adiciona um dicionário representando uma **música** à lista **playlist**.
- `view_playlist` → **Itera** sobre a **playlist** para exibir todas as **músicas**.
- `get_longest_song` → Encontra a **música** de **maior duração** usando a função **max** com uma função **lambda** como chave de busca.
- `filter_playlist` → Função de **alta ordem** que recebe uma função de **filtro** como argumento e aplica a filtragem usando **list comprehension**.
- `create_filter_by_artist` → **Closure** que cria e retorna uma **nova função** de filtro que "lembra" o nome do **artista** fornecido.

---
### 🧪 Casos de Teste

## **Test Case 01 (CT01)**

* **Requisito:** FR01 - O sistema deve permitir adicionar uma nova música.
* **Passos:**
    1.  Executar o script de testes `tests.py` com o Pytest.
    2.  Verificar o teste **test_add_song_populates_playlist**.
    3.  A função **add_song** é chamada.
    4.  O tamanho e o conteúdo da lista global **playlist** são verificados.
* **Valor de entrada:**
    * Título: `Stairway to Heaven`
    * Artista: `Led Zeppelin`
    * Gênero: `Rock`
    * Duração: `482`
* **Resultado esperado:** A **playlist** deve conter **1 item**, e os dados desse **item** devem corresponder aos **dados de entrada**.
* **Status:** Aprovado

## **Test Case 02 (CT02)**

* **Requisito:** FR02 - O sistema deve ser capaz de encontrar e exibir a música mais longa.
* **Passos:**
    1.  Executar o script de testes `tests.py` com o Pytest.
    2.  Verificar o teste **test_get_longest_song_finds_correct_song**.
    3.  Três músicas com **durações** diferentes são **adicionadas**.
    4.  A função **get_longest_song** é chamada.
* **Valor de entrada:**
    * Song 1: (Título: A, Artista: X, Gênero: Pop, Duração: 180)
    * Song 2: (Título: B, Artista: Y, Gênero: Rock, Duração: 240)
* **Resultado esperado:** A função deve retornar o dicionário correspondente à **"The Longest Song"**, cuja duração é 500.
* **Status:** Aprovado

---
## 🐳 Tecnologias Utilizadas

- Python
---

## 🤝 Contribuição

- [Hermeson Santos](https://github.com/HermesonxDevII/)
- [Maria Joselene](https://github.com/j0selene)
