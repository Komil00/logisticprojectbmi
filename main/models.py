from django.db import models

# Create your models here.

class Cartransport(models.Model):
    character = models.CharField(max_length=200, null=True, blank=True)
    weight = models.IntegerField()
    route = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.character
    
    class Meta:
        verbose_name = "Автомобильные перевозки"
        verbose_name_plural = "Автомобильные перевозки"


class Necessary_equipment(models.Model):
    character = models.CharField(max_length=30)

    def __str__(self):
        return self.character
    
    class Meta:
        verbose_name = "Необходимая техника"
        verbose_name_plural = "Необходимая техника"


class Rent_of_special_equipment(models.Model):
    necessary_equipment = models.ForeignKey(Necessary_equipment,on_delete=models.CASCADE, null=True, blank=True)
    route = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Аренда спецтехники"
        verbose_name_plural = "Аренда спецтехники"


class Passenger_Transportation(models.Model):
    number_of_passengers = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Пассажирские перевозки"
        verbose_name_plural = "Пассажирские перевозки"