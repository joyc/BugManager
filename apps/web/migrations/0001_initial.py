# Generated by Django 3.0.6 on 2021-01-23 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(db_index=True, max_length=100, verbose_name='登录名')),
                ('username', models.CharField(max_length=100, verbose_name='姓名')),
                ('email', models.EmailField(max_length=200, verbose_name='邮箱')),
                ('mobile', models.CharField(max_length=100, verbose_name='手机号码')),
                ('password', models.CharField(max_length=300, verbose_name='密码')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
