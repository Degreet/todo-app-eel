import eel
from config import host
from pymongo import MongoClient

cluster = MongoClient(host)
db = cluster["todo-app-eel"]

@eel.expose
def reg_user():
  pass

eel.init("web")
eel.start("index.html", size=(800, 600))