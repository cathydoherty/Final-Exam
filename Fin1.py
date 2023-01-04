#Cathy Doherty
class House:
    """This is a house on Zillow.
    The attributes are model, number of bedrooms, number of bathrooms, year built, and location."""

def greatHouse(greatHouse, model, bedrooms, bathrooms, year, location):
    greatHouse.model = "Victorian"
    greatHouse.bedrooms = 3
    greatHouse.bathrooms= 2
    greatHouse.year= 1920
    greatHouse.location = "WY"

print("A %s house with %d bedrooms and %d bathrooms, built in %d and located in %s." %("Victorian", 3, 2, 1920, "WY"))
