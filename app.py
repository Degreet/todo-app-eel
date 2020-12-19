import eel
from config import host
from pymongo import MongoClient

cluster = MongoClient(host)
db = cluster["todo-app-eel"]
users = db["users"]

@eel.expose
def reg_user(data):
  login = data['login']
  pwd = data['pass'].encode()
  candidate = users.find_one({ "login": login })
  error = ""

  if candidate:
    error = "Такой логин уже занят"

  if error:
    return error
  else:
    users.insert_one({
      "login": login,
      "password": pwd
    })

    return "success"

eel.init("web")
eel.start("index.html", size=(800, 600))