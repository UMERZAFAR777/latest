from django import template
import math
register = template.Library()


@register.simple_tag()

def calculate_price(Price,Discount):
    if Discount is None or Discount is 0:
        return Price
    sellprice = Price
    sellprice = Price - (Price * Discount/100)
    return math.floor (sellprice) 

@register.simple_tag()

def calculate_progress_bar(availbility, total_quantity):
    progress_value = availbility * (100 / total_quantity)
    return math.floor(progress_value)


