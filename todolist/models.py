from django.db import models
from users.models import CustomUser


class ToDoList(models.Model):
    
    CHECK = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    
    task = models.CharField('Task', max_length=300)
    date = models.DateField('Deadline')
    check = models.CharField('Done', max_length=1, choices=CHECK, default='N', blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task