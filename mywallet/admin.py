from django.contrib import admin
from mywallet.models import *

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Customer)
admin.site.register(Transactions)
