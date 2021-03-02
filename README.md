# Rating

Microsserviço responsável pelo sistema de feedbacks para os usuários da aplicação.

## Colocando no ar

Com o Docker e Docker-Compose instalados, basta apenas utilizar os comandos:

```shell
    sudo docker-compose -f docker-compose-dev.yml up --build
```

## Rodando os testes

Com o Docker e Docker-Compose instalados, basta apenas utilizar os comandos:  

```shell
    sudo docker-compose -f docker-compose-dev.yml run rating python manage.py test
```
