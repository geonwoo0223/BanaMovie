from django.contrib import admin
from .models import Board, BoardComment

# Register your models here.
admin.site.register(Board)
admin.site.register(BoardComment)