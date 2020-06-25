from django.db import models


# Create your models here.django框架为我们提供了ORM框架，可以根据代码自动生成数据表
# 1)自定义数据类型，修改models.py文件  2)进行数据迁移，在命令行执行 python manage.py makemigrations  生成0001_initial.py
# 生成迁移文件，执行迁移，修改models.py或定义更多字段以后执行命令 python manage.py migrate 更新库表字段
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
