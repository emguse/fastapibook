# FastAPI-book-demo

---
- form this book [動かして学ぶ！Python FastAPI開発入門](https://www.seshop.com/product/detail/25640)
---
- Enter the following command without `pyproject.toml` .
- By running the `poetry init` command with `fastapi` and `uvicorn` as arguments, we specify both as dependent packages.
- Answer the interactive dialog. If you only answer `Author` with `n`, there is no problem with the Enter key for everything else.

```bash
docker compose run --entrypoint "poetry init --name demo-app --dependency fastapi --dependency uvicorn[standard]" demo-app
```

- Install the package containing `fastapi`.

```bash
docker compose run --entrypoint "poetry install --no-root" demo-app
```

- Now that pyproject.toml and poetry.lock are ready with the two commands, rebuild the container.

```bash
docker compose build --no-cache
```

- Migration DB

```bash
docker compose exec demo-app poetry run python -m api.migrate_db
```

- Check db tables

```bash
docker compose exec db mysql demo
mysql> SHOW TABLES;
+----------------+
| Tables_in_demo |
+----------------+
| dones          |
| tasks          |
+----------------+
2 rows in set (0.00 sec)

mysql> DESCRIBE tasks;
+-------+---------------+------+-----+---------+----------------+
| Field | Type          | Null | Key | Default | Extra          |
+-------+---------------+------+-----+---------+----------------+
| id    | int           | NO   | PRI | NULL    | auto_increment |
| title | varchar(1024) | YES  |     | NULL    |                |
+-------+---------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> DESCRIBE dones;
+-------+------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+-------+------+------+-----+---------+-------+
| id    | int  | NO   | PRI | NULL    |       |
+-------+------+------+-----+---------+-------+
1 row in set (0.00 sec)
```