# Generated by Django 5.0.4 on 2024-04-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_alter_cost_options_alter_income_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
