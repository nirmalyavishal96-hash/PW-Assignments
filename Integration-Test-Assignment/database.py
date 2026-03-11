class Database:

    def __init__(self):
        self.data = {
            1: "Alice",
            2: "Bob",
            3: "Charlie"
        }

    def get_user(self, user_id):
        return self.data.get(user_id)