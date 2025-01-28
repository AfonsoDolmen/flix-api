# Flix API

Este projeto é uma API RESTful que está sendo desenvolvida com **Django** e **Django REST Framework (DRF)**, voltada para o gerenciamento de filmes, gêneros, atores e avaliações. Foi criada com o objetivo de estudo e prática no desenvolvimento de APIs no padrão RESTful. Recentemente, foram implementadas novas funcionalidades, como a geração automática de resumos de filmes com a integração com a API do ChatGPT e métricas estatísticas para análise dos dados.

## Funcionalidades

A API permite realizar as seguintes operações:

- **Filmes**:
  - Listar, criar, atualizar e deletar filmes.
  - Associar gêneros e atores a um filme.
  - Geração automática de resumos dos filmes utilizando a API do ChatGPT.
- **Gêneros**:
  - Listar, criar, atualizar e deletar gêneros.
- **Atores**:
  - Listar, criar, atualizar e deletar atores.
  - Associar filmes aos atores.
- **Avaliações**:
  - Listar, criar, atualizar e deletar avaliações de filmes.
  - Avaliar filmes com até 5 estrelas e adicionar comentários.
- **Métricas Estatísticas**:
  - Consultar métricas como:
    - Quantidade total de filmes.
    - Quantidade de filmes por gênero.
    - Média das avaliações dos filmes.
    - Quantidade total de avaliações.

## Modelos

### Filme
- **`title`**: Título do filme.
- **`genre`**: Gênero associado ao filme (chave estrangeira).
- **`release_date`**: Data de lançamento.
- **`actors`**: Atores associados ao filme (relação muitos-para-muitos).
- **`resume`**: Resumo do filme gerado automaticamente pela API do ChatGPT, se não fornecido manualmente.

### Gênero
- **`name`**: Nome do gênero.

### Ator
- **`name`**: Nome do ator.
- **`birthday`**: Data de nascimento.
- **`nationality`**: Nacionalidade do ator (escolhas).

### Avaliação
- **`movie`**: Filme avaliado (chave estrangeira).
- **`stars`**: Nota (até 5 estrelas).
- **`comment`**: Comentário opcional sobre o filme.

## Tecnologias Utilizadas

- **Python 3.9+**
- **Django 4.x**
- **Django REST Framework 3.x**
- **OpenAI API** (para a geração automática de resumos dos filmes)

## Endpoints

### 1. Filmes

- `GET /movies/`: Lista todos os filmes.
- `POST /movies/`: Cria um novo filme.
- `PUT /movies/{id}/`: Atualiza um filme existente.
- `DELETE /movies/{id}/`: Deleta um filme.

### 2. Gêneros

- `GET /genres/`: Lista todos os gêneros.
- `POST /genres/`: Cria um novo gênero.
- `PUT /genres/{id}/`: Atualiza um gênero existente.
- `DELETE /genres/{id}/`: Deleta um gênero.

### 3. Atores

- `GET /actors/`: Lista todos os atores.
- `POST /actors/`: Cria um novo ator.
- `PUT /actors/{id}/`: Atualiza um ator existente.
- `DELETE /actors/{id}/`: Deleta um ator.

### 4. Avaliações

- `GET /reviews/`: Lista todas as avaliações.
- `POST /reviews/`: Cria uma nova avaliação.
- `PUT /reviews/{id}/`: Atualiza uma avaliação existente.
- `DELETE /reviews/{id}/`: Deleta uma avaliação.

### 5. Métricas Estatísticas

- `GET /metrics/`: Retorna as métricas estatísticas, como:
  - Quantidade total de filmes.
  - Quantidade de filmes por gênero.
  - Média das avaliações dos filmes.
  - Quantidade total de avaliações.
