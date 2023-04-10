# Generated by Django 3.0.7 on 2020-07-20 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('last_name', models.CharField(max_length=255, verbose_name='姓')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='名')),
                ('seller_id', models.CharField(max_length=255, unique=True)),
                # ('mws_auth_token', models.CharField(max_length=255)),
                ('market_place', models.CharField(max_length=255)),
                ('do_get_matching_product_for_id', models.BooleanField(default=True, verbose_name='GetMatchingProductForId')),
                ('do_get_competitive_pricing_for_asin', models.BooleanField(default=True, verbose_name='GetCompetitivePricingForASIN')),
                ('do_get_lowest_offer_listings_for_asin', models.BooleanField(default=True, verbose_name='GetLowestOfferListingsForASIN')),
                ('do_get_my_price_for_asin', models.BooleanField(default=True, verbose_name='GetMyPricingForASIN')),
                ('do_get_product_categories_for_asin', models.BooleanField(default=True, verbose_name='GetProductCategoriesForASIN')),
                ('asin_jan_one_to_one', models.BooleanField(default=True, verbose_name='JAN検索で最初のASINのみ利用する')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='管理者')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='利用開始')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', main.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aws_access_key', models.CharField(max_length=255)),
                ('aws_secret_key', models.CharField(max_length=255)),
                ('request_batch_size', models.IntegerField(default=5)),
                ('default_wait_sec', models.FloatField(default=1.0)),
                ('quota_wait_sec', models.FloatField(default=2.0)),
                ('paypal_client_id', models.CharField(default='Adt_Vhio0TLBSK1dsw3iOklDv_u-m87eFmdVqAPZ95O7lelQT8hsJ7zodnV2vo6kghB1HuRpBewqabqL', max_length=255)),
                ('paypal_client_secret', models.CharField(default='EINVdviKFC5XhnKyuyn6k0nOS1zz_iNxNjqb-Wc_uuR7WxSzZszTNSitz1ScLNNf6sTaXbdu8J-Icod9', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScrapeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('asin', 'ASIN'), ('jan', 'JAN')], default='asin', max_length=10)),
                ('id_text', models.TextField(null=True)),
                ('csv_file', models.FileField(null=True, upload_to='csv')),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', 'NEW'), ('2', 'IN_PROGRESS'), ('3', 'COMPLETED'), ('4', 'ERROR')], default='1', max_length=1)),
                ('error', models.CharField(default=None, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaypalSubscription',
            fields=[
                ('plan_id', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('subscription_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('approve_url', models.CharField(max_length=100)),
                ('ba_token', models.CharField(default=None, max_length=100, null=True)),
                ('token', models.CharField(default=None, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=100)),
                ('jan', models.CharField(default=None, max_length=13, null=True)),
                ('get_matching_product_for_id_raw', models.TextField(null=True)),
                ('get_competitive_pricing_for_asin_raw', models.TextField(null=True)),
                ('get_lowest_offer_listings_for_asin_raw', models.TextField(null=True)),
                ('get_my_price_for_asin_raw', models.TextField(null=True)),
                ('get_product_categories_for_asin_raw', models.TextField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'asin')},
            },
        ),
    ]
