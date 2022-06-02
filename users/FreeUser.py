from users.User import Users
from datetime import datetime

class FreeUser(Users):
    def __init__(self, first, last, phone, address, num_posts=0) -> None:
        super().__init__(first, last, phone, address)
        self.num_posts = num_posts

    def post(self, post) -> str:
        if(self.num_posts<2):
            self.num_posts+=1
            if(Users.last_post == self.fullname):
                Users.all_posts.append([self.fullname, post, f'{datetime.now().strftime("%m/%d/%Y")}', f'{datetime.now().strftime("%H:%M:%S")}'])
                return f""" > {post}"""
            else:
                Users.all_posts.append([self.fullname, post, f'{datetime.now().strftime("%m/%d/%Y")}', f'{datetime.now().strftime("%H:%M:%S")}'])
                Users.last_post = self.fullname
                return f"""{self.fullname}:\n > {post}"""
        else:
            Users.all_posts.append([self.fullname, '**POST LIMIT REACHED**', f'{datetime.now().strftime("%m/%d/%Y")}', f'{datetime.now().strftime("%H:%M:%S")}'])
            return f"**{self.fullname} reached their post limit. Please upgrade to Premium to unlock unlimited posts.**"
    