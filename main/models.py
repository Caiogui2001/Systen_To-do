from django.db import models

class Registro(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    





class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    