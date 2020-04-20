# Generated by Django 2.2 on 2020-04-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_name', models.CharField(max_length=200)),
                ('credit_price', models.CharField(max_length=200)),
                ('credit_detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]