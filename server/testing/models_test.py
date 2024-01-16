from datetime import datetime

from app import app
from models import db, Message

class TestMessage:
    '''Message model in models.py'''

    with app.app_context():
        m = Message.query.filter(
            Message.body == "Hello 👋"
            ).filter(Message.username == "Aisha")

        for message in m:
            db.session.delete(message)

        db.session.commit()

    def test_has_correct_columns(self):
        '''has columns for message body, username, and creation time.'''
        with app.app_context():

            hello_from_Aisha = Message(
                body="Hello 👋",
                username="Aisha")
            
            db.session.add(hello_from_Aisha)
            db.session.commit()

            assert(hello_from_Aisha.body == "Hello 👋")
            assert(hello_from_Aisha.username == "Aisha")
            assert(type(hello_from_Aisha.created_at) == datetime)
