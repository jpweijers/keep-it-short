
## Setup DB

Create a database with docker:
```
docker run --name keep-it-short-postgres \
	-e POSTGRES_USER=docker \
	-e POSTGRES_PASSWORD=docker \
	-e POSTGRES_DB=keep-it-short \
	-p 5432:5432 \
	-d postgres
```
