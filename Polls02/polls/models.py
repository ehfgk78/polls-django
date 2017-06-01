from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class 질문틀(models.Model):
    질문내용 = models.CharField(max_length = 200)
    질문날짜 = models.DateTimeField()

    def __str__(self):
        return self.질문내용

    def 최근24시간내질문인가(self):
        바로지금 = timezone.now()
        하루전 = timezone.now() - datetime.timedelta(days=1)
        return 하루전 <= 질문날짜 <= 바로지금

class 선택틀(models.Model):
    관련질문 = models.ForeignKey(질문틀, on_delete = models.CASCADE)
    선택지 = models.CharField(max_length = 200)
    투표수 = models.IntegerField(default= 0)

    def __str__(self):
        return self.선택지
