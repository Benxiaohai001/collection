users = {'Hans': "active", "Eleonore": "inactive", "shabi": "active"}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print(users)
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)