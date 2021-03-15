# Rating

Microsserviço responsável pelo sistema de feedbacks para os usuários da aplicação.

Todos os comandos abaixo requerem a instalação de Docker e Docker-Compose.

*** 
**[Disponível na porta 5001.](http://localhost:5001/)**
***

## Colocando no ar


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