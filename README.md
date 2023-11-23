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