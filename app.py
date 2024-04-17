import sqlalchemy
import greenlet

def handler():
    print(sqlalchemy.__version__)
    print(greenlet.__version__)

handler()
