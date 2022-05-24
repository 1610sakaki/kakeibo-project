# Generated by Django 4.0.4 on 2022-05-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('給料', '給料'), ('賞与', '賞与'), ('副業', '副業'), ('臨時収入', '臨時収入')], max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='category',
            field=models.CharField(choices=[('食費', '食費'), ('外食費', '外食費'), ('水道光熱費', '水道光熱費'), ('通信費', '通信費'), ('日用品費', '日用品費'), ('住居備品費', '住居備品費'), ('衣服', '衣服費'), ('教養費', '教養費'), ('趣味・娯楽', '趣味・娯楽'), ('美容', '美容'), ('医療費', '医療費'), ('交際費', '交際費'), ('交通費', '交通費'), ('サブスクリプション費', 'サブスクリプション費'), ('郵便・宅配・その他雑費', '郵便・宅配・その他雑費'), ('保険代', '保険代')], max_length=100),
        ),
    ]