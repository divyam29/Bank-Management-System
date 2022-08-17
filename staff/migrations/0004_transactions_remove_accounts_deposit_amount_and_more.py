# Generated by Django 4.0.2 on 2022-08-14 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_rename_acc_id_customers_acc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('acc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='staff.accounts')),
                ('withdrawal_amount', models.FloatField(blank=True, null=True)),
                ('deposit_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='deposit_amount',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='withdrawal_amount',
        ),
    ]
