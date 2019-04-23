# Generated by Django 2.1.1 on 2019-04-23 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('nativeAccountCurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencies.Currency', verbose_name='Linked currency')),
                ('userObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Linked user object')),
            ],
        ),
        migrations.CreateModel(
            name='ClientBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balanceValue', models.DecimalField(decimal_places=4, default=0.0, max_digits=190, null=True, verbose_name='Value of the balance')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('balanceCurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencies.Currency', verbose_name='Linked currency')),
                ('balanceOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='Linked Client object')),
            ],
        ),
    ]
