from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.contrib.auth.models import User

class Colleges(models.Model):
    StatusOptions = [
        ('notstarted', 'Not Started'),
        ('inprogress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('deferred', 'Deferred'),
        ('accepted', 'Accepted'),
        ('waitlisted', 'Waitlisted'),
        ('rejected', 'Rejected'),
    ]
    TierOptions = [
        ('reach', "Reach"),
        ('match', 'Match'),
        ('safety', 'Safety'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="colleges")
    school_name = models.CharField(max_length=600)
    Satus = models.CharField(max_length=600, choices=StatusOptions, default="notstarted")

    deadline_type = models.CharField(max_length=20, blank=True)

    deadline = models.DateField(blank=True, null=True)

    Tier = models.CharField(max_length=600, choices=TierOptions)
    major = models.CharField(max_length=200, blank=True)

    likelihood = models.CharField(max_length=20, blank=True)

    notes = models.CharField(max_length=500, blank=True)

    portal_url = models.CharField(max_length=600, blank=True)

    def __str__(self):
        return f"{self.school_name} ({self.Tier}) for {self.user.username}"


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", default=None)

    # Geographical INFO
    State = models.CharField(max_length=600, blank=True)
    City = models.CharField(max_length=600, blank=True)
    School = models.CharField(max_length=600, blank=True)

    # GPA
    OverallGPAUW = models.FloatField(blank=True, null=True)
    OverallGPAW = models.FloatField(blank=True, null=True)
    FreshGPAUW = models.FloatField(blank=True, null=True)
    FreshGPAU = models.FloatField(blank=True, null=True)
    SophGPAUW = models.FloatField(blank=True, null=True)
    SophGPAW = models.FloatField(blank=True, null=True)
    JunGPAUW = models.FloatField(blank=True, null=True)
    JunGPAW = models.FloatField(blank=True, null=True)
    SenGPAUW = models.FloatField(blank=True, null=True)
    SenGPAW = models.FloatField(blank=True, null=True)

    # AP testing (SEE CLASS: APScore)

    # Standardized testing
    SAT = models.IntegerField(blank=True, null=True)
    ACT = models.IntegerField(blank=True, null=True)

    # Activities
    Activity1 = models.CharField(max_length=100, blank=True)
    Description1 = models.CharField(max_length=150, blank=True)
    Activity2 = models.CharField(max_length=100, blank=True)
    Description2 = models.CharField(max_length=150, blank=True)
    Activity3 = models.CharField(max_length=100, blank=True)
    Description3 = models.CharField(max_length=150, blank=True)
    Activity4 = models.CharField(max_length=100, blank=True)
    Description4 = models.CharField(max_length=150, blank=True)
    Activity5 = models.CharField(max_length=100, blank=True)
    Description5 = models.CharField(max_length=150, blank=True)
    Activity6 = models.CharField(max_length=100, blank=True)
    Description6 = models.CharField(max_length=150, blank=True)
    Activity7 = models.CharField(max_length=100, blank=True)
    Description7 = models.CharField(max_length=150, blank=True)
    Activity8 = models.CharField(max_length=100, blank=True)
    Description8 = models.CharField(max_length=150, blank=True)
    Activity9 = models.CharField(max_length=100, blank=True)
    Description9 = models.CharField(max_length=150, blank=True)
    Activity10 = models.CharField(max_length=100, blank=True)
    Description10 = models.CharField(max_length=150, blank=True)

    #Awards
    Award1 = models.CharField(max_length=150, blank=True)
    Award2 = models.CharField(max_length=150, blank=True)
    Award3 = models.CharField(max_length=150, blank=True)
    Award4 = models.CharField(max_length=150, blank=True)
    Award5 = models.CharField(max_length=150, blank=True)

    # Letters of rec
    Teacher1 = models.CharField(max_length=100, blank=True)
    Teacher2 = models.CharField(max_length=100, blank=True)
    Teacher3 = models.CharField(max_length=100, blank=True)
    Teacher4 = models.CharField(max_length=100, blank=True)

    note = models.CharField(max_length=1000, blank=True)
    pref_area = models.CharField(max_length=1000, blank=True)
    major = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


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

    exam_name = models.CharField(choices=AP_EXAM_CHOICES, max_length=100)
    score = models.IntegerField(choices=SCORE_CHOICES)

    def __str__(self):
        return f"{self.exam_name}: {self.score}"
