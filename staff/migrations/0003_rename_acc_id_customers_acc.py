# Generated by Django 4.0.2 on 2022-08-14 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_accounts_deposit_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='acc_id',
            new_name='acc',
        ),
    ]
