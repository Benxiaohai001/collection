# users = {'Hans': "active", "Eleonore": "inactive", "shabi": "active"}

# for user, status in users.copy().items():
#     if status == "inactive":
#         del users[user]

# print(users)
# active_users = {}
# for user, status in users.items():
#     if status == "active":
#         active_users[user] = status
# print(active_users)

# 4.7 match语句
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("origin")
        case Point(x=0, y=y):
            print(f"Y is {y}")
        case Point(x=x, y=0):
            print(f"X is {x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
    
if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(0, 10)
    p3 = Point(10, 0)
    p4 = Point(10, 10)
    # p5 = Point()
    p6 = Point(1, 1)
    where_is(p1)
    where_is(p2)
    where_is(p3)
    where_is(p4)
    # where_is(p5)
    where_is(p6)