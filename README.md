
# Python API 


## Structure

```
python_api/
├── .pytest_cache/
├── api/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── dataset.json
│   ├── main.py
│   └── test_main.py
├── Podmanfile
└── requirements.txt
```

- `api/__init__.py`: Initializes the API module.
- `api/dataset.json`: The JSON file containing the data to be served by the API.
- `api/main.py`: The main FastAPI application.
- `api/test_main.py`: Tests for the main API application.
- `Podmanfile`: Configuration file for building the Podman container.
- `requirements.txt`: List of dependencies required by the project.




## Running

### Podman


1. Build :

```sh
podman build -t python_api -f Podmanfile .
```

2. Run :

```sh
podman run -d -p 8000:8000 python_api
```

3. Check logs:

```sh
podman logs <container_id>
```

4. Access API endpoint:

```sh
curl http://localhost:8000/api/data
```

5. Access the container's shell:

```sh
podman exec -it <container_id> /bin/sh
```


## Running Tests

```sh
pytest
```
