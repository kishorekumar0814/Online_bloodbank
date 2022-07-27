# Generated by Django 4.0.4 on 2022-05-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blooddata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('ph_no', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=225)),
                ('lastname', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('confirm_password', models.CharField(max_length=225)),
                ('email_id', models.CharField(max_length=225)),
                ('ph_no', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('blood_group', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
    ]
