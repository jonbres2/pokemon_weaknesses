from django.db import models

class NormalType(models.Model):
    superEffective = "Fighting"
    notVeryEffective = ["Rock", "Steel"]
    immune = "Ghost"

class NoneType(models.Model):
    superEffective = ""
    notVeryEffective = ""
    immune = ""
