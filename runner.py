from users.User import Users
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
# Driver Code #
free_user = FreeUser('John', 'Doe', '123-456-7890', '123 Main St')
premium_user = PremiumUser('Jane', 'Doe', '098-765-4321', '456 Grand Blvd')

print(f"User 1: {free_user}")
print(f"User 2: {premium_user}")

print(free_user.post('Test'))
print(free_user.post('Good Morning'))
print(premium_user.post('Hi John!'))
print(free_user.post(f"Jane, I have something very important to tell you and I don't know if I'll ever have another chance. I love you!"))

Users.post_history()
premium_user.delete_post()
Users.post_history()