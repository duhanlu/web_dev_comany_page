from django.db import models
from utils.basemodels import BaseModel
# Create your models here.


class User(BaseModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField('username', max_length=30, null = True, blank = True, unique = True)
    password = models.CharField('password', max_length=30)
    email = models.CharField('email', max_length = 30, unique=True)

    class Meta: 
        db_table = 'user'
        verbose_name = 'userinfo'