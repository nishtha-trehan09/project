# Generated by Django 4.0.1 on 2022-01-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=20)),
                ('user_choice', models.CharField(choices=[('rock', 'ROCK'), ('paper', 'PAPER'), ('scissors', 'SCISSORs')], max_length=10)),
                ('comp_choice', models.CharField(choices=[('rock', 'ROCK'), ('paper', 'PAPER'), ('scissors', 'SCISSORs')], max_length=10)),
                ('user_score', models.IntegerField(blank=True, null=True)),
                ('comp_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]