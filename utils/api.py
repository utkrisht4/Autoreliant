from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {
        "id": user_id,
        "name": "Test User"
    }

@app.post("/users")
def create_user(user: dict):
    if "name" not in user:
        raise HTTPException(status_code=400, detail="Name required")
    return {"message": "User created", "user": user}