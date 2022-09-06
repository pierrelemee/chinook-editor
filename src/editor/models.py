from django.db import models


class Album(models.Model):
    id = models.AutoField(db_column='AlbumId', primary_key=True)
    title = models.CharField(db_column='Title', max_length=160)
    artist = models.ForeignKey('Artist', models.CASCADE, related_name='albums', db_column='ArtistId')

    class Meta:
        managed = False
        db_table = 'Album'


class Artist(models.Model):
    id = models.AutoField(db_column='ArtistId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Artist'


class Customer(models.Model):
    id = models.AutoField(db_column='CustomerId', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=40)
    lastname = models.CharField(db_column='LastName', max_length=20)
    company = models.CharField(db_column='Company', max_length=80, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=70, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=40, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=40, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=40, blank=True, null=True)
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=60)
    sales = models.ForeignKey('Employee', models.SET_NULL, db_column='SupportRepId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'


class Employee(models.Model):
    id = models.AutoField(db_column='EmployeeId', primary_key=True)
    lastname = models.CharField(db_column='LastName', max_length=20)
    firstname = models.CharField(db_column='FirstName', max_length=20)
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)
    manager = models.ForeignKey('self', models.SET_NULL, db_column='ReportsTo', blank=True, null=True)
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=70, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=40, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=40, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=40, blank=True, null=True)
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employee'


class Genre(models.Model):
    id = models.AutoField(db_column='GenreId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Genre'


class Invoice(models.Model):
    id = models.AutoField(db_column='InvoiceId', primary_key=True)
    customer = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerId')
    invoicedate = models.DateTimeField(db_column='InvoiceDate')
    billingaddress = models.CharField(db_column='BillingAddress', max_length=70, blank=True, null=True)
    billingcity = models.CharField(db_column='BillingCity', max_length=40, blank=True, null=True)
    billingstate = models.CharField(db_column='BillingState', max_length=40, blank=True, null=True)
    billingcountry = models.CharField(db_column='BillingCountry', max_length=40, blank=True, null=True)
    billingpostalcode = models.CharField(db_column='BillingPostalCode', max_length=10, blank=True, null=True)
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Invoice'


class Invoiceline(models.Model):
    id = models.AutoField(db_column='InvoiceLineId', primary_key=True)
    invoice = models.ForeignKey(Invoice, models.CASCADE, db_column='InvoiceId')
    track = models.ForeignKey('Track', models.CASCADE, db_column='TrackId')
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)
    quantity = models.IntegerField(db_column='Quantity')

    class Meta:
        managed = False
        db_table = 'InvoiceLine'


class Mediatype(models.Model):
    id = models.AutoField(db_column='MediaTypeId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MediaType'


class Playlist(models.Model):
    id = models.AutoField(db_column='PlaylistId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Playlist'


class PlaylistTrack(models.Model):
    playlist = models.OneToOneField(Playlist, models.CASCADE, db_column='PlaylistId', primary_key=True)
    track = models.ForeignKey('Track', models.CASCADE, db_column='TrackId')

    class Meta:
        managed = False
        db_table = 'PlaylistTrack'
        unique_together = (('playlist', 'track'),)


class Track(models.Model):
    id = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=200)
    album = models.ForeignKey(Album, models.SET_NULL, related_name='tracks', db_column='AlbumId', blank=True, null=True)
    mediatype = models.ForeignKey(Mediatype, models.CASCADE, db_column='MediaTypeId')
    genre = models.ForeignKey(Genre, models.SET_NULL, db_column='GenreId', blank=True, null=True)
    composer = models.CharField(db_column='Composer', max_length=220, blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unit_price = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Track'
