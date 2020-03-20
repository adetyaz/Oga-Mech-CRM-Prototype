# Generated by Django 2.2 on 2020-03-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20200320_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='crm.Tag'),
        ),
    ]