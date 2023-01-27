from pathlib import Path

BASE_DIR = path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.joinpath('db.dqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
