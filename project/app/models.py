from django.db import models

# Create your models here.

class report(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    problem = models.CharField(
        max_length=50,
        choices=[
            ('Login Issue', 'Login Issue'),
            ('Membership Problem', 'Membership Problem'),
            ('Payment Issue', 'Payment Issue'),
            ('Website Bug', 'Website Bug'),
            ('Trainer Complaint', 'Trainer Complaint'),
            ('Other', 'Other')
        ]
    )
    message=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name