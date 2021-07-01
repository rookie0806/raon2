from django.db import models

# Create your models here.
class Reservation(models.Model):
    STATUS_CHOICE = (
        ('입금대기', '입금대기'),
        ('입금완료', '입금완료'),
    )
    date = models.DateField(auto_now_add=False)
    package = models.TextField(max_length=100,null=True)
    name = models.TextField(max_length=100,null=True)
    headcount = models.IntegerField()
    others = models.TextField(max_length=100,null=True)
    phonenumber = models.TextField(max_length=100,null=True)
    status = models.TextField(max_length=100,choices=STATUS_CHOICE,default="입금대기")