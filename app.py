import eel, string, random
from config import host
from pymongo import MongoClient

cluster = MongoClient(host)
db = cluster["todo-app-eel"]

users = db["users"]
todos = db["todos"]

@eel.expose
def reg_user(data):
  login = data['login']
  pwd = data['pass'].encode()
  candidate = users.find_one({ "login": login })
  error = ""
  data = {}

  if candidate:
    error = "Такой логин уже занят"

  if not error:
    token = get_random_string(32)

    data["success"] = True
    data["token"] = token

    users.insert_one({
      "login": login,
      "password": pwd,
      "token": token
    })
  else:
    data["msg"] = error

  return data

@eel.expose
def check_user(data):
  login = data['login']
  pwd = data['pass'].encode()
  candidate = users.find_one({ "login": login, "password": pwd })
  data = {}

  if candidate:
    token = get_random_string(32)
    data["success"] = True
    data["token"] = token
    users.update_one({ "login": login }, {
      "$set": {
        "token": token
      }
    })
  else:
    data["msg"] = "Неверный логин или пароль"
  
  return data

@eel.expose
def get_todos(token, page=1):
  candidate = users.find_one({ "token": token })
  data = {}

  if candidate:
    ten_todos = todos.find_one({ user: candidate['login'] }).skip(page * 10 - 10).limit(page * 10)
    data['todos'] = ten_todos

  return data

def get_random_string(length):
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

eel.init("web")
eel.start("index.html", size=(800, 600))