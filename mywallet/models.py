import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(TimeStamp):
    customer_xid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Wallet(TimeStamp):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, unique=True)
    is_active = models.BooleanField(default=False)
    balance = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.id

class Transactions(TimeStamp):
    StatusChoices = (
        ("success", "success"),
        ("failure", "failure"), 
        ("pending", "pending")
    )
    TransactionChoices =(
        ("deposit", "deposit"),
        ("withdrawal", "withdrawal")
    )
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=StatusChoices, default="pending")
    transaction_type = models.CharField(max_length=50, choices=TransactionChoices)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.id