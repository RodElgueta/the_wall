from django.db import models


class UsersManager(models.Manager):
    def user_valid(self,userData):
        errors = {}

        if len(userData['name']) < 3 or len(userData['name'])  > 45:
                errors["name"] = "Username must be at least 3 character and not more than 45 characters" 
        if len(userData['password']) < 4:
                errors['password'] = "Password must be at least 4 characters"
        return errors

class MessagesgManager(models.Manager):
    def msg_valid(self,msgData):
        errors = {}

        if len(msgData['message']) < 10:
            errors['message'] = "Your message should be at least 10 characters"
        return errors

