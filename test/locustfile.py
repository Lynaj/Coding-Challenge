from locust import HttpLocust, TaskSet
from random import randrange
import json

# def register(l):
#     l.client.post("/api/v1/users/register/", {"email": l.randomizedField, "password": l.randomizedField, "repeatPassword": l.randomizedField, "firstName": l.randomizedField,
#      "lastName": l.randomizedField})

def computational_function_invoke(l):
    auth_response = l.client.get("//api/v1/transactions/summedtransactions/?EMAIL=")
    auth_token = json.loads(auth_response.text)['token']
    l.token = 'Bearer ' + auth_token

def index(l):
    l.client.get("/")

def balance(l):
    l.client.get("/api/v1/balances/",
        headers={'Authorization': l.jwt_auth_token}
    )

class UserBehavior(TaskSet):
    tasks = {index: 2, balance: 1}

    randomizedField = str(
        randrange(1000000000)
    ) + "am@wp.pl"
    token = ''

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

