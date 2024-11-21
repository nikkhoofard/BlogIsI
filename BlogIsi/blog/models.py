from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    summery = models.TextField(default="none")
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )],
        help_text='Enter phone number'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    is_done=models.BooleanField(default=False)


    def __str__(self):
        return f'{self.first_name} {self.last_name}' \
               f'-{self.field}-{self.degree} '
