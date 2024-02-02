from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class CarModel(models.Model):

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
    ]

    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    year = models.DateField()
    
    def __str__(self):
        return f"{self.car_make} - {self.name}"



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership  = dealership #Id of dealership
        self.name = name #name of reviewer
        self.purchase = purchase #if they purchased
        self.review = review #text of review
        self.purchase_date = purchase_date #the purchase date
        self.car_make = car_make #car make
        self.car_model = car_model #car model
        self.car_year = car_year #car year
        self.sentiment = sentiment #sentiment of the review
        self.id = id #id of the review

    def __str__(self):
        return "Reviewer Name: " + self.name + \
            "Review: " + self.review