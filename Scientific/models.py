from django.db import models


class MyProject(models.Model):
    status = models.TextField(max_length=200, verbose_name='Статус проекта', default=' ')
    place = models.IntegerField(verbose_name='Занятое место', default=0)

'''
Название награды (приза) за результаты НИР, проводимой студентом (доклады на конференции не учитываются)
'''
class Scientific_Research_Work(models.Model):
    title = models.TextField()
    place = models.TextField()
    individual_team = models.BooleanField()
    RTU_reward = models.BooleanField()
    date = models.TextField()

'''
Название документа, удостоверяющегоисключительное право студента на достигнутый им научный 
(научно-методический, научно-технический, научно-творческий) результат интеллектуальной деятельности (патент, свидетельство)
'''
class Patent(models.Model):
    title = models.TextField()
    individual_team = models.BooleanField()
    RTU_reward = models.BooleanField()
    date = models.TextField()

'''
Название гранта на выполнение НИР (только для получателей гранта, исполнители гранта не учитываются
'''
class Grant(models.Model):
    title = models.TextField()
    individual_team = models.BooleanField()
    RTU_reward = models.BooleanField()
    date = models.TextField()


'''
Перечень публикаций в  научном  (учебно-научном,  учебно-методическом)  международном,  
всероссийском,  ведомственном  или региональном издании, в издании Университетаили иной 
организации в течение 1-ого года, предшествующего назначению повышенной государственной академической стипендии
'''
class Publications(models.Model):
    title = models.TextField()
    volume_title = models.TextField()
    level = models.TextField()
    authors_quantity = models.IntegerField()
    date = models.TextField()
