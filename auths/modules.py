import string
import random
from django.db.models import  Q
def generate_random_string(length=10):
    """
    Generate a random string of fixed length
    """
    _str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    return ''.join(random.choice(_str) for i in range(length))


def Check_username_holder(username, model):
    """
    Checks username, email and phone on the position of username.

    Args:
        username(String)

    Returns:
        profile object or False


    """
    try:
        user = model.objects.get(Q(phone =username) | Q(user__username = username) | Q(user__email = username))
        return user
    except model.DoesNotExist:
        return False