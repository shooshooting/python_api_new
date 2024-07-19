from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/data")
def get_data():
   # Read JSON file
    try:
        with open('api/dataset.json', 'r') as f:
            data = json.load(f)
            print(data)
        return data
    except Exception as e:  
        return {"error": str(e)}

'''

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)

'''










# podman build -t python_api -f Podmanfile .
# podman run -d -p 8000:8000 python_api
# podman logs <container_id>
# curl http://localhost:8000/api/data
# podman exec -it <container_id> /bin/sh








