from __future__ import unicode_literals

from django.db import models

# Create your models here.

GRADE_FIR = 1
GRADE_SEC = 2
GRADE_THR = 3
GRADE_FOU = 4
GRADE_FIV = 5
GRADE_SIX = 6
GRADE_SEV = 7
GRADE_EIG = 8
GRADE_NIN = 9
GRADE_TEN = 10
GRADE_ELE = 11

GRADE_CHOICES = (
    (GRADE_FIR, 'Grade 1'),
    (GRADE_SEC, 'Grade 2'),
    (GRADE_THR, 'Grade 3'),
    (GRADE_FOU, 'Grade 4'),
    (GRADE_FIV, 'Grade 5'),
    (GRADE_SIX, 'Grade 6'),
    (GRADE_SEV, 'Grade 7'),
    (GRADE_EIG, 'Grade 8'),
    (GRADE_NIN, 'Grade 9'),
    (GRADE_TEN, 'Grade 10'),
    (GRADE_ELE, 'Grade 11'),
)

DAY_OF_MON = 1
DAY_OF_TUE = 2
DAY_OF_WED = 3
DAY_OF_THU = 4
DAY_OF_FRI = 5

DAY_OF_CHOICES = (
    (DAY_OF_MON, 'Monday'),
    (DAY_OF_TUE, 'Tuesday'),
    (DAY_OF_WED, 'Wednesday'),
    (DAY_OF_THU, 'Thursday'),
    (DAY_OF_FRI, 'Friday'),
)


class Schedule(models.Model):
    grade = models.IntegerField(verbose_name='Grade', unique=False, null=False, choices=GRADE_CHOICES)
    day_of = models.IntegerField(verbose_name='Day of', unique=False, null=False, choices=DAY_OF_CHOICES)
    lessons_fir = models.CharField(verbose_name='Lesson 1', unique=False, null=True, blank=True, max_length=20)
    lessons_sec = models.CharField(verbose_name='Lesson 2', unique=False, null=True, blank=True, max_length=20)
    lessons_trh = models.CharField(verbose_name='Lesson 3', unique=False, null=True, blank=True, max_length=20)
    lessons_fou = models.CharField(verbose_name='Lesson 4', unique=False, null=True, blank=True, max_length=20)
    lessons_fiv = models.CharField(verbose_name='Lesson 5', unique=False, null=True, blank=True, max_length=20)
    lessons_six = models.CharField(verbose_name='Lesson 6', unique=False, null=True, blank=True, max_length=20)

    def __unicode__(self):
        return ''


class New(models.Model):
    title = models.CharField(verbose_name='Title', unique=False, null=False, blank=False, max_length=54)
    description = models.CharField(verbose_name='Description', unique=False, blank=False, max_length=1024)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True, null=True)

    def __unicode__(self):
        return ''


class Student(models.Model):
    name = models.CharField(verbose_name='Name', unique=False, null=False, blank=False, max_length=24)
    surname = models.CharField(verbose_name='Surname', unique=False, null=False, blank=False, max_length=24)
    phone = models.IntegerField(verbose_name='Phone number', unique=False, null=False, blank=False, )
    grade = models.IntegerField(verbose_name='Grade', unique=False, null=False, choices=GRADE_CHOICES)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True, null=True)

    def __unicode__(self):
        return ''


class Support(models.Model):
    name = models.CharField(verbose_name='Name', unique=False, null=False, blank=False, max_length=24)
    surname = models.CharField(verbose_name='Surname', unique=False, null=False, blank=False, max_length=24)
    title = models.CharField(verbose_name='Title', unique=False, null=False, blank=False, max_length=54)
    description = models.CharField(verbose_name='Description', unique=False, blank=False, max_length=1024)
    phone = models.IntegerField(verbose_name='Phone number', unique=False, null=False, blank=False, )
    grade = models.IntegerField(verbose_name='Grade', unique=False, null=False, choices=GRADE_CHOICES)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True, null=True)

    def __unicode__(self):
        return ''
