# Generated by Django 3.2.5 on 2021-07-23 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210723_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='contact_num',
            new_name='contact_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='employee',
            field=models.CharField(blank=True, choices=[('1', 'Job Seeker'), ('2', 'Employer')], max_length=1, null=True),
        ),
    ]
