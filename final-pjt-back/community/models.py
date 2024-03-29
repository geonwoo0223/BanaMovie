from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model



def set_FK_Model_user():
    return get_user_model().objects.get(username="삭제된유저")

# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(set_FK_Model_user))
    title = models.CharField(max_length=200)
    content = models.TextField()
    board_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BoardComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(set_FK_Model_user))
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)