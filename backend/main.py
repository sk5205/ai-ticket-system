from fastapi import FastAPI, Depends
from pydantic import BaseModel
from utils.prediction import predict_ticket
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Ticket as TicketModel

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class Ticket(BaseModel):
    description: str

@app.post("/predict")
def predict(ticket: Ticket, db: Session = Depends(get_db)):
    category, priority = predict_ticket(ticket.description)

    new_ticket = TicketModel(
        description=ticket.description,
        category=category,
        priority=priority
    )

    db.add(new_ticket)
    db.commit()

    return {
        "category": category,
        "priority": priority
    }

@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(TicketModel).order_by(TicketModel.id.desc()).all()
    return tickets