# Generated by Django 4.0.6 on 2022-07-14 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_notice_notice_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_at', models.DateTimeField(auto_now_add=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.notice')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pic', models.FileField(null=True, upload_to='media/images/')),
                ('video', models.FileField(null=True, upload_to='media/video/')),
                ('venue', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
