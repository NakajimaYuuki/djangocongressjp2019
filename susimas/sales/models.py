from django.db import models


class Sushi(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255, primary_key=True, help_text='ex ) 松コース、竹コース、シェフのお任せ10貫')
    price = models.IntegerField(default=0)
    sushi_lists = models.ManyToManyField(Sushi, related_name='menus')

    def __str__(self):
        return self.name


class Sale(models.Model):
    saled_date = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    sushi = models.ForeignKey(Sushi, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.menu.name}-{self.saled_date}'
