from django.db import models

# Create your models here.


class Colleges(models.Model):
    StatusOptions = [
        ('notstarted', 'Not Started'),
        ('inprogress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('deferred', 'Deferred'),
        ('accepted', 'Accepted'),
        ('waitlisted', 'Waitlisted'),
        ('rejected', 'Rejected')
    ]

    TierOptions = [
        ('reach', "Reach"),
        ('match', 'Match'),
        ('safety', 'Safety')
    ]

    school_name = models.CharField(max_length=600)
    Satus = models.CharField(max_length=600, choices=StatusOptions)
    deadline = models.DateField()
    Tier = models.CharField(max_length=600, choices=TierOptions)
