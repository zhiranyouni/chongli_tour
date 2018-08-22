# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SnowPack(models.Model):
    code = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=12, blank=True, null=True)
    contact_dept = models.CharField(max_length=20, blank=True, null=True)
    contacts = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_operator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_operator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snow_pack'


class SnowTicket(models.Model):
    snow_pack_id = models.IntegerField()
    product_code = models.CharField(max_length=20)
    market_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    prefer_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    spare_number = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    product_type = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    create_operator = models.IntegerField(blank=True, null=True)
    update_operator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_online = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'snow_ticket'


class SnowTicketType(models.Model):
    include_board = models.IntegerField(blank=True, null=True)
    day_or_hour = models.IntegerField(blank=True, null=True)
    duration = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    use_time = models.IntegerField(blank=True, null=True)
    trail_type = models.IntegerField(blank=True, null=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_operator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_operator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snow_ticket_type'


class UseTime(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    duration = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_time'
