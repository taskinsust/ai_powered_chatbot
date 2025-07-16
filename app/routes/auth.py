from fastapi import APIRouter, Depends, Form
from app.core.security import create_access_token

router = APIRouter()

@router.post("/token")
def login(username: str = Form(...), password: str = Form(...)):
    # Replace with real authentication
    if username == "admin" and password == "admin":
        token = create_access_token(data={"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")