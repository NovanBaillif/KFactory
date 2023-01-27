from dataclasses import dataclass
from datetime import datetime
import app

class Task(app.db.Model):
    id = app.db.Column(app.db.Integer(), primary_key=True)
    title = app.db.Column(app.db.String(140))
    date = app.db.Column(app.db.DateRime(), default=datetime.now())
    completed = app.db.Column(app.db.Boolean(), default=False)

    def __init__(self,*args, **kwargs):
        super(). __init__(*args, **kwargs)