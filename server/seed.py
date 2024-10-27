#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Message

fake = Faker()

# Create a list of usernames
usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    # Clear existing messages
    Message.query.delete()
    
    messages = []

    for _ in range(20):
        message = Message(
            body=fake.sentence(),  # Only include the body attribute
            # Remove username as it's not defined in the Message model
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()        

if __name__ == '__main__':
    with app.app_context():
        make_messages()
