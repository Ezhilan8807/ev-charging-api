from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stations/", response_model=list[schemas.StationOut])
def read_stations(db: Session = Depends(get_db)):
    return crud.get_stations(db)

@app.post("/stations/", response_model=schemas.StationOut)
def add_station(station: schemas.StationCreate, db: Session = Depends(get_db)):
    return crud.create_station(db, station)

@app.post("/book/", response_model=schemas.BookingOut)
def book_slot(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking)