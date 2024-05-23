from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, DateTime
from datetime import date, datetime
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

database = databases.Database(DATABASE_URL)
metadata = MetaData()

invoices = Table(
    "invoices",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("invoice_number", String, index=True),
    Column("total", Numeric),
    Column("invoice_date", DateTime),
    Column("status", String),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

class Invoice(BaseModel):
    id: int
    invoice_number: str
    total: float
    invoice_date: datetime
    status: str

class DateRange(BaseModel):
    StartDate: date
    EndDate: date

app = FastAPI()

origins = [
    "http://localhost:4300",
    "http://127.0.0.1:4300"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/invoices/", response_model=list[Invoice])
async def get_invoices(date_range: DateRange):
    query = invoices.select().where(
        invoices.c.invoice_date.between(date_range.StartDate, date_range.EndDate)
    )
    results = await database.fetch_all(query)
    if not results:
        raise HTTPException(status_code=404, detail="No invoices found in the given date range")
    return results
