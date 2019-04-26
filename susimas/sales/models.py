from django.db import models


class SushiTopping(models.Model):
    name = models.CharField(max_length=255, help_text="ex) トロ、穴子、サーモン、ハマチ、ブリ")

    def __str__(self):
        return self.name


class Sushi(models.Model):
    name = models.CharField(max_length=255, primary_key=True, help_text='ex ) 松コース、シェフのお任せ10貫、単品も含む')
    price = models.IntegerField(default=0)
    sushi_toppings = models.ManyToManyField(SushiTopping)

    def __str__(self):
        return self.name


class Sale(models.Model):
    saled_date = models.CharField(max_length=255)
    sushi = models.ForeignKey(Sushi, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.sushi.name}-{self.saled_date}'
