# Container
```bash
docker run --rm -it -p 5433:5432 -e POSTGRES_PASSWORD=secret1234 postgres:alpine3.20
psql -h localhost -p 5433 -U postgres postgres
```

```bash
create database example;
```
