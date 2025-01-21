# Flix API

Este projeto é uma API RESTful que está sendo desenvolvida com **Django** e **Django REST Framework (DRF)**, voltada para o gerenciamento de filmes, gêneros, atores e avaliações. Foi criada com o objetivo de estudo e prática no desenvolvimento de APIs no padrão RESTful.

## Funcionalidades

A API permite realizar as seguintes operações:

- **Filmes**:
  - Listar, criar, atualizar e deletar filmes.
  - Associar gêneros e atores a um filme.
- **Gêneros**:
  - Listar, criar, atualizar e deletar gêneros.
- **Atores**:
  - Listar, criar, atualizar e deletar atores.
  - Associar filmes aos atores.
- **Avaliações**:
  - Listar, criar, atualizar e deletar avaliações de filmes.
  - Avaliar filmes com até 5 estrelas e adicionar comentários.

## Modelos

### Filme
- **`title`**: Título do filme.
- **`genre`**: Gênero associado ao filme (chave estrangeira).
- **`release_date`**: Data de lançamento.
- **`actors`**: Atores associados ao filme (relação muitos-para-muitos).
- **`resume`**: Resumo do filme.

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
