from django.db import models

# Create your models here.


class College(models.Model):
    name = models.TextField(max_length=60)
    city = models.TextField(max_length=60)
    state = models.TextField(max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.TextField(max_length=60)
    colleges = models.ManyToManyField(College)

    def __str__(self):
        return self.title


class Ksa(models.Model):
    KSA_TYPE_CHOICES = (("1", "knowledge"), ("2", "skill"), ("3", "ability"))
    id = models.TextField(max_length=3, primary_key=True, unique=True)
    ksa_type = models.TextField(max_length=10, choices=KSA_TYPE_CHOICES)
    description = models.TextField(max_length=200)
    jobs = models.ManyToManyField(Job)
    colleges = models.ManyToManyField(College)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id} {self.description}"
