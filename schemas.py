from pydantic import BaseModel

class StationBase(BaseModel):
    name: str
    location: str
    available_slots: int

class StationCreate(StationBase):
    pass

class StationOut(StationBase):
    id: int
    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    user_name: str
    station_id: int
    slot_time: str

class BookingCreate(BookingBase):
    pass

class BookingOut(BookingBase):
    id: int
    confirmed: bool
    class Config:
        orm_mode = True