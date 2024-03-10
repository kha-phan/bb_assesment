from django.db import models
from .base import BaseModel


class Account(BaseModel):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False, verbose_name='Is Active')
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff')
    is_superuser = models.BooleanField(default=False, verbose_name='Is Supper User')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'account'
