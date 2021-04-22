from django.db import models


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
   

'''
Состояние подтверждения (ссылки на пользователя и админа)
'''
class Confirmation_Status(models.Model):
    user = models.TextField()
    admin = models.TextField()
