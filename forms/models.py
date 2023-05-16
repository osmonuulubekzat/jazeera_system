import datetime
from django.db import models


# Create your models here.
class OurСlints(models.Model):
    FirstName = models.CharField(verbose_name="Имя", max_length=120)
    LastName = models.CharField(verbose_name="Фамилия", max_length=120)
    PhoneNumber = models.CharField(verbose_name="Номер Телефона", max_length=120)
    Email = models.EmailField(verbose_name="Е-почта", max_length=120)
    Region = models.CharField(verbose_name="Регион", max_length=120)
    date = models.DateField(verbose_name="Дата Регистрации", default=datetime.date.today)

    def __str__(self):
        return self.FirstName

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"
