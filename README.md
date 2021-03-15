[![Lint](https://github.com/Lend-it/Rating/actions/workflows/black.yml/badge.svg)](https://github.com/Lend-it/Rating/actions/workflows/black.yml) [![Build](https://github.com/Lend-it/Rating/actions/workflows/sonar.yml/badge.svg)](https://github.com/Lend-it/Rating/actions/workflows/sonar.yml) [![Commit Linter](https://github.com/Lend-it/Rating/actions/workflows/commit-linter.yml/badge.svg)](https://github.com/Lend-it/Rating/actions/workflows/commit-linter.yml) [![Application Test](https://github.com/Lend-it/Rating/actions/workflows/app-test.yml/badge.svg)](https://github.com/Lend-it/Rating/actions/workflows/app-test.yml)
# Rating

Microsserviço responsável pelo sistema de feedbacks para os usuários da aplicação.

Todos os comandos abaixo requerem a instalação de Docker e Docker-Compose.

## Ambientes
### Local
**[Disponível na porta 5001.](http://localhost:5001/)**

### Ambiente de homologação
**[Disponível no Heroku](https://lendit-rating-homolog.herokuapp.com/)**

### Ambiente de produção
**[Disponível no Heroku](https://lendit-rating-prod.herokuapp.com/)**

***
## Colocando no ar localmente


1. Build
```shell
    make build
```
2. Executar
```shell
    make run
```
2.1 Executar em background
```shell
    make run-silent
```
2.2 Buildar e executar
```shell
    make run-build
```
3. Desativar o container
```shell
    make down
```

## Rodando os testes


```shell
    make test
```

## Acessando o banco de dados 

```shell
    make check-db
```

## Rodar o linter no código (Black) 

```shell
    make lint
```