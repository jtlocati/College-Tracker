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


class userprofile(models.Model):
    #Geograohical INFO
    State = models.CharField(max_length=600)
    City = models.CharField(max_length=600)
    School = models.CharField(max_length=600)

    #GPA
    OverallGPA = models.FloatField(max_length=4)
    FreshGPAUW= models.FloatField(max_length=4)
    FreshGPAU = models.FloatField(max_length=4)
    SophGPAUW = models.FloatField(max_length=4)
    SophGPAW = models.FloatField(max_length=4)
    JunGPAUW = models.FloatField(max_length=4)
    JunGPAW = models.FloatField(max_length=4)
    SenGPAUW = models.FloatField(max_length=4)
    SenGPAW = models.FloatField(max_length=4)

    #AP testing (SEE CLASS: APScore)

    #studio testing
    SAT = models.IntegerField(max_length=4)
    ACT = models.IntegerField(max_length=2)

    #Activitys
    Activity1 = models.CharField(max_length=100)
    Description1 = models.CharField(max_length=150)
    Activity2 = models.CharField(max_length=100)
    Description2 = models.CharField(max_length=150)
    Activity3 = models.CharField(max_length=100)
    Description3 = models.CharField(max_length=150)
    Activity4 = models.CharField(max_length=100)
    Description4 = models.CharField(max_length=150)
    Activity5 = models.CharField(max_length=100)
    Description5 = models.CharField(max_length=150)
    Activity6 = models.CharField(max_length=100)
    Description6 = models.CharField(max_length=150)
    Activity7 = models.CharField(max_length=100)
    Description7 = models.CharField(max_length=150)
    Activity8 = models.CharField(max_length=100)
    Description8 = models.CharField(max_length=150)
    Activity9 = models.CharField(max_length=100)
    Description9 = models.CharField(max_length=150)
    Activity10 = models.CharField(max_length=100)
    Description10 = models.CharField(max_length=150)

    #Letters of rec
    Teacher1 = models.CharField(max_length=100)
    Teacher2 = models.CharField(max_length=100)
    Teacher3 = models.CharField(max_length=100)
    Teacher4 = models.CharField(max_length=100)


class APScore(models.Model):
    SCORE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]


    user_profile = models.ForeignKey(
        userprofile,
        on_delete=models.CASCADE,
        related_name="ap_scores"
    )

    AP_EXAM_CHOICES = [

    # Arts
    ('AP Art and Design', 'AP Art and Design'),
    ('AP Art History', 'AP Art History'),
    ('AP Music Theory', 'AP Music Theory'),

    # English
    ('AP English Language and Composition', 'AP English Language and Composition'),
    ('AP English Literature and Composition', 'AP English Literature and Composition'),

    # History and Social Sciences
    ('AP African American Studies', 'AP African American Studies'),
    ('AP Comparative Government and Politics', 'AP Comparative Government and Politics'),
    ('AP European History', 'AP European History'),
    ('AP Human Geography', 'AP Human Geography'),
    ('AP Macroeconomics', 'AP Macroeconomics'),
    ('AP Microeconomics', 'AP Microeconomics'),
    ('AP Psychology', 'AP Psychology'),
    ('AP United States Government and Politics', 'AP United States Government and Politics'),
    ('AP United States History', 'AP United States History'),
    ('AP World History: Modern', 'AP World History: Modern'),

    # Math and Computer Science
    ('AP Calculus AB', 'AP Calculus AB'),
    ('AP Calculus BC', 'AP Calculus BC'),
    ('AP Computer Science A', 'AP Computer Science A'),
    ('AP Computer Science Principles', 'AP Computer Science Principles'),
    ('AP Precalculus', 'AP Precalculus'),
    ('AP Statistics', 'AP Statistics'),

    # Sciences
    ('AP Biology', 'AP Biology'),
    ('AP Chemistry', 'AP Chemistry'),
    ('AP Environmental Science', 'AP Environmental Science'),
    ('AP Physics 1', 'AP Physics 1: Algebra-Based'),
    ('AP Physics 2', 'AP Physics 2: Algebra-Based'),
    ('AP Physics C E&M', 'AP Physics C: Electricity and Magnetism'),
    ('AP Physics C Mechanics', 'AP Physics C: Mechanics'),

    # World Languages and Cultures
    ('AP Chinese Language and Culture', 'AP Chinese Language and Culture'),
    ('AP French Language and Culture', 'AP French Language and Culture'),
    ('AP German Language and Culture', 'AP German Language and Culture'),
    ('AP Italian Language and Culture', 'AP Italian Language and Culture'),
    ('AP Japanese Language and Culture', 'AP Japanese Language and Culture'),
    ('AP Latin', 'AP Latin'),
    ('AP Spanish Language and Culture', 'AP Spanish Language and Culture'),
    ('AP Spanish Literature and Culture', 'AP Spanish Literature and Culture'),

    # Capstone and New Courses
    ('AP Research', 'AP Research'),
    ('AP Seminar', 'AP Seminar'),
    ('AP Business with Personal Finance', 'AP Business with Personal Finance'),
    ('AP Cybersecurity', 'AP Cybersecurity'),
    ]


    exam_name = models.CharField(choices=AP_EXAM_CHOICES)
    score = models.IntegerField(choices=SCORE_CHOICES)

    def __str__(self):
        return f"{self.exam_name}: {self.score}"