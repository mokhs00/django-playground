from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    register = models.ForeignKey(Person, on_delete=models.CASCADE)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)