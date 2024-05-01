# Generated by Django 5.0.4 on 2024-04-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cost',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]