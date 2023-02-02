from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import Client

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()


class Plan(models.Model):   # Виды тарифных планов
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)    # принимает кортеж кортежей
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                     MaxValueValidator(100)
                                                   ])

class Subscription(models.Model):   # Подписка где сходятся все связи
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)    # клиенты подписываются на сервисы на основе тарифного плана
    service= models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)