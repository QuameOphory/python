import json
import json
import requests

#uses the requests library to get json data from jsonplaceholder site
response = requests.get("https://jsonplaceholder.typicode.com/todos")
#uses the loads method to deserialize the json data
todos = json.loads(response.text)
#create a dictionary of completed TODOs by each user
todos_by_user = {}
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] +=1
        except KeyError:
            todos_by_user[todo["userId"]] =1

#sort the completed TODOs dictionaries in descending order
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
#gets the maximum number of TODOs completed
max_complete = top_users[0][1]

#get the users who have completed the greatest number of TODOs
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
max_users = " and ".join(users)

s = "s" if len(top_users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} todos")