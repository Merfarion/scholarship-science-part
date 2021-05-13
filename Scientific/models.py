from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Scientific(models.Model):
    title = models.TextField()
    date = models.DateField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    name = models.TextField(max_length=300, default='')
    superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)


'''
Название награды (приза) за результаты НИР, проводимой студентом (доклады на конференции не учитываются)
'''
class Scientific_Research_Work(models.Model):
    user = models.TextField()
    title = models.TextField()
    place = models.TextField()
    individual_team = models.BooleanField()
    RTU_reward = models.BooleanField()
    date = models.TextField()
    scores = models.IntegerField(default=-1)
    application_id = models.IntegerField()
    files = models.TextField() # JSON Array of attached files


'''
Название документа, удостоверяющегоисключительное право студента на достигнутый им научный 
(научно-методический, научно-технический, научно-творческий) результат интеллектуальной деятельности (патент, свидетельство)
'''
class Patent(models.Model):
    user = models.TextField()
    title = models.TextField()
    individual_team = models.BooleanField()
    RTU_reward = models.BooleanField()
    date = models.TextField()
    scores = models.IntegerField(default=-1)
    application_id = models.IntegerField()
    files = models.TextField() # JSON Array of attached files


'''
Название гранта на выполнение НИР (только для получателей гранта, исполнители гранта не учитываются
'''
class Grant(models.Model):
    user = models.TextField()
    title = models.TextField()
    individual_team = models.BooleanField()
    RTU_reward = models.BooleanField()
    date = models.TextField()
    scores = models.IntegerField(default=-1)
    application_id = models.IntegerField()
    files = models.TextField() # JSON Array of attached files


'''
Перечень публикаций в  научном  (учебно-научном,  учебно-методическом)  международном,  
всероссийском,  ведомственном  или региональном издании, в издании Университетаили иной 
организации в течение 1-ого года, предшествующего назначению повышенной государственной академической стипендии
'''
class Publications(models.Model):
    user = models.TextField()
    title = models.TextField()
    volume_title = models.TextField()
    level = models.TextField()
    authors_quantity = models.IntegerField()
    date = models.TextField()
    scores = models.IntegerField(default=-1)
    application_id = models.IntegerField()
    files = models.TextField() # JSON Array of attached files


'''
Модель БД для хранения файлов
Краткое описание структуры:
id          - Primary Key
owner       - ID владельца файла
file_uuid   - UUID файла. Имя файла в файловой системе
file_name   - Оригинальное имя файла с расширением
'''
class Files(models.Model):
    owner = models.TextField()
    file_uuid = models.TextField()
    file_name = models.TextField()