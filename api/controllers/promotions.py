from datetime import date
from pydantic import BaseModel
import random
import string

class Promotion(BaseModel):
    promo_code: str
    expiration_date: date

def generate_promo_code(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
