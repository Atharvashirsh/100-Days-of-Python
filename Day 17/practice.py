class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Atharva")
user_2 = User("002", "Rishank")

# print(user_1.id, user_1.username, user_1.followers)
# print(user_2.id, user_2.username, user_2.followers)

user_1.follow(user_2)

print(
    f"""\tFollowers Following
User 1\t{user_1.followers}\t{user_1.following}
User 2\t{user_2.followers}\t{user_2.following}"""
)
