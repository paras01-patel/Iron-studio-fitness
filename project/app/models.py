from django.db import models


# REPORT MODEL
class report(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

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

    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# CONTACT MODEL
class con(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# TRAINER FORM MODEL
class TrainerForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    trainer = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


# JOIN MODEL
class Joined(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=54)
    phone = models.IntegerField()
    age = models.IntegerField()
    plan = models.CharField(max_length=30)
    trainer = models.CharField(max_length=30)
    goal = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name