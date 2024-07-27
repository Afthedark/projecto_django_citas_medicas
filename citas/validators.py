from django.core.exceptions import ValidationError
from datetime import datetime


def validate_age(value):
    if value < 0:
        raise ValidationError(
            '%(value)s debe ser mayor a 0',
            params={'value': value},
        )
    elif value > 110:
        raise ValidationError(
            '%(value)s debe ser menor a 110',
            params={'value': value},
        )


    
def validate_name(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError(
                'El nombre solo puede contener letras',
                params={'value': value},
            )
        
        
        