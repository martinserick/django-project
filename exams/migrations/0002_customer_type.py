# Generated by Django 5.0.3 on 2024-03-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('Laboratório', 'Laboratório'), ('Geral', 'Geral'), ('Clínica', 'Clínica')], default='Geral', max_length=30),
        ),
    ]
