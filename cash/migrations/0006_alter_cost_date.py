# Generated by Django 5.0.4 on 2024-04-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0005_alter_cost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
