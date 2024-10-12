from django.db import models

class UserSign(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'users_signup'

    def __str__(self):
        return self.username
    

class IPOInfo(models.Model):
    company_logo_path = models.TextField()

    company_name = models.CharField(max_length=255)
    price_band = models.CharField(max_length=100)
    open = models.CharField(max_length=100)
    close = models.CharField(max_length=100)
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    listing_date = models.CharField(max_length=100)
    status = models.IntegerField()
    ipo_price = models.CharField(max_length=100)
    listing_price = models.CharField(max_length=100)
    listing_gain = models.CharField(max_length=100)
    cmp = models.CharField(max_length=100)
    current_return = models.CharField(max_length=100)
    rhp = models.CharField(max_length=100)
    drhp = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'ipo_info'

    def __str__(self):
        return self.company_name
