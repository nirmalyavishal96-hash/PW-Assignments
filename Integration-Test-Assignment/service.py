from database import Database

class UserService:

    def __init__(self):
        self.db = Database()

    def get_user_name(self, user_id):

        user = self.db.get_user(user_id)

        if user:
            return f"User found: {user}"
        else:
            return "User not found"