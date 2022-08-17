from django.db import models

class Accounts(models.Model):
    acc_id = models.IntegerField(primary_key=True,default=None)
    acc_type = models.CharField(max_length=250)
    trans_limit=models.FloatField()
    balance=models.FloatField()
    overdraft=models.FloatField(null=True,blank=True)

class Transactions(models.Model):
    acc = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    withdrawal_amount = models.FloatField(null=True,blank=True)
    deposit_amount = models.FloatField(null=True,blank=True)

class Customers(models.Model):
    cust_id = models.IntegerField(primary_key=True,default=None)
    acc = models.OneToOneField(Accounts, on_delete=models.CASCADE,null=True,blank=True)
    cust_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250,null=True,blank=True)
    pan = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)

class Loans(models.Model):
    loan_id=models.IntegerField(primary_key=True,default=None)
    acc=models.ManyToManyField(Accounts)
    loan_type=models.CharField(max_length=250)
    principle=models.FloatField()
    time_mnths=models.IntegerField()
    rate=models.FloatField()


