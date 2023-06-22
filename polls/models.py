from django.db import models

class Gear(models.Model):
    name = models.CharField(max_length=128,
                            unique=True,
                            verbose_name="Nazwa")

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return f"{self.name}"
    
class Fuel(models.Model):
    namen = models.CharField(max_length=128,
                            unique=True,
                            verbose_name="Nazwa")

    class Meta:
        ordering = ["namen"]
    
    def __str__(self):
        return f"{self.namen}"


class Cars(models.Model):
    brand = models.CharField(max_length=128,
                                  null=False,
                                  default="",
                                  verbose_name="Marka")
    model = models.CharField(max_length=256,
                                 null=False,
                                 default="",
                                 verbose_name="Model")
    made_date = models.CharField(max_length=4,
                                 null=False,
                                 default="",
                                 verbose_name="Rok Produkcji")
    price = models.DecimalField(max_digits=12,
                                 decimal_places=2,
                                 default=0,
                                 verbose_name="Cena")
    horse = models.IntegerField(verbose_name="Moc")
    description = models.TextField(default="",
                                   blank=True,
                                   verbose_name="Opis")
    image = models.ImageField(upload_to="cars/",
                              null=True,
                              blank=True,
                              verbose_name="Zdjecie")
    gear = models.ForeignKey(Gear,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="Skrzynia Biegow")
    fuel = models.ForeignKey(Fuel,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="Paliwo")
    
    
    class Meta:
        ordering = ["model"]
    
    def __str__(self):
        return f"{self.brand} {self.model}"
