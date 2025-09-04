# Dictionary in place of match case

users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Charlie", "role": "guest"},
]

operating_costs = {    # Without logging in and with logging in
    "admin": (200, 110),
    "user": (250, 130),
    "guest": (400, 200)
}

for user_list in users:
    wt_login, login = operating_costs.get(user_list["role"], (1500,1000))
    print(f"User with ID {user_list['id']} named {user_list['name']} to pay ${wt_login} without logging in. In case if user logs in, to pay ${login}")  
