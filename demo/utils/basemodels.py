from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField('createTime', auto_now_add=True, editable=True)
    update_at = models.DateTimeField('updateTime', auto_now_add=True, editable=True)

    class Meta: 
        abstract = True
