from django.db import models


# Create your models here.
class WiseSaying(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Board(models.Model):
    board_no = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
