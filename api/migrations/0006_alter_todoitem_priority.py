# Generated by Django 4.0.2 on 2022-02-03 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_todoitem_due_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(choices=[('0', 'Low'), ('1', 'Medium'), ('2', 'High')], default='0', max_length=1),
        ),
    ]
