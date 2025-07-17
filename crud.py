from sqlalchemy.orm import Session
import models, schemas

def get_stations(db: Session):
    return db.query(models.ChargingStation).all()

def create_station(db: Session, station: schemas.StationCreate):
    new_station = models.ChargingStation(**station.dict())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return new_station

def create_booking(db: Session, booking: schemas.BookingCreate):
    new_booking = models.Booking(**booking.dict(), confirmed=True)
    db.add(new_booking)

    # Update slots
    station = db.query(models.ChargingStation).filter(models.ChargingStation.id == booking.station_id).first()
    if station and station.available_slots > 0:
        station.available_slots -= 1

    db.commit()
    db.refresh(new_booking)
    return new_booking