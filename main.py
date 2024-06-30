from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, User, Base

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def main():
    return templates.TemplateResponse("main_page.html", {"request": {}})

@app.get("/get_users", response_class=HTMLResponse)
async def get_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("get_users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def view_profile(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})

@app.post("/add_user_to_db", response_class=HTMLResponse)
async def add_user(request: Request, name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return templates.TemplateResponse("user_added.html", {"request": request, "user": db_user})

@app.get("/add_user", response_class=HTMLResponse)
async def add_user_form(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
