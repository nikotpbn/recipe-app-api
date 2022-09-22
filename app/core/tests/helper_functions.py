from django.contrib.auth import get_user_model


def create_user(password='default123', **kwargs):
    return get_user_model().objects.create_user(**kwargs)