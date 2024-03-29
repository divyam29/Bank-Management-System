# Generated by Django 4.0.2 on 2022-08-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('acc_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('withdrawal_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cust_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=250)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('pan', models.CharField(max_length=250)),
                ('dob', models.CharField(max_length=250)),
                ('acc_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.accounts')),
            ],
        ),
    ]
