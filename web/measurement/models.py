from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django import forms
from datetime import date


class Specification(models.Model):
    Prototype = (
        ('ICMP', 'ICMP'),
        ('UDP', 'UDP'),
        ('TCP', 'TCP'),
    )
    protocol = models.CharField(max_length=5, choices=Prototype, default='TCP', )
    interval = models.IntegerField(default=0)
    one_off = models.BooleanField(default=True)
    start_time = models.DateField(auto_now_add=True)
    stop_time = models.DateField(null=True)

    def __str__(self):
        return 'Protocol-%s , Interval-%s' % (self.protocol, self.interval)


class Probes(models.Model):
    country = models.CharField(max_length=2)
    number = models.IntegerField(default=0)

    def __str__(self):
        return '%s-%s' % (self.country, self.number)


class Target(models.Model):
    target = models.CharField(max_length=100)
    specification = models.ForeignKey(Specification)
    probes = models.ManyToManyField(Probes)
    description = models.CharField(max_length=100)
    msm_id = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default='Running')


class SpecificationForm(ModelForm):
    stop_time = forms.DateField(required=False)

    class Meta:
        model = Specification
        fields = ['protocol', 'interval', 'one_off', 'stop_time']

    def __init__(self, *args, **kwargs):
        super(SpecificationForm, self).__init__(*args, **kwargs)
        self.fields["stop_time"].widget = forms.widgets.SelectDateWidget()
        self.fields["interval"].help_text = "In seconds"


class ProbesForm(ModelForm):
    class Meta:
        model = Probes
        fields = ['country', 'number']


def __init__(self, *args, **kwargs):
    super(SpecificationForm, self).__init__(*args, **kwargs)
    self.fields["country"].help_text = "Two letter code"


class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = ['target', 'description', 'specification', 'probes']

    def __init__(self, *args, **kwargs):
        super(TargetForm, self).__init__(*args, **kwargs)
        self.fields["probes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["probes"].help_text = "Can't be more than 1000 in number"
        self.fields["probes"].queryset = Probes.objects.all()
        # self.fields["specification"].widget = forms.widgets.CheckboxSelectMultiple()
        # self.fields["specification"].help_text = ""
        # self.fields["specification"].queryset = Specification.objects.all()


class Countries(models.Model):
    country = models.CharField(max_length=4)

    def __str__(self):
        return '%s' % (self.country)


class Traceroutemeasurement12(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation12')


    def __str__(self):
        return '%s' % (self.id)


class Relation12(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement12)


class Traceroutemeasurement1(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation1')


    def __str__(self):
        return '%s' % (self.id)


class Relation1(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement1)


class Traceroutemeasurement2(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation2')


    def __str__(self):
        return '%s' % (self.id)


class Relation2(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement2)


class Traceroutemeasurement3(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation3')


    def __str__(self):
        return '%s' % (self.id)


class Relation3(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement3)


class Traceroutemeasurement4(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation4')


    def __str__(self):
        return '%s' % (self.id)


class Relation4(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement4)

class Traceroutemeasurement5(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation5')


    def __str__(self):
        return '%s' % (self.id)


class Relation5(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement5)

class Traceroutemeasurement6(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation6')


    def __str__(self):
        return '%s' % (self.id)


class Relation6(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement6)


class Traceroutemeasurement7(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation7')


    def __str__(self):
        return '%s' % (self.id)


class Relation7(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement7)

class Traceroutemeasurement8(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation8')


    def __str__(self):
        return '%s' % (self.id)


class Relation8(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement8)




class Traceroutemeasurement9(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation9')


    def __str__(self):
        return '%s' % (self.id)


class Relation9(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement9)



class Traceroutemeasurement10(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation10')


    def __str__(self):
        return '%s' % (self.id)


class Relation10(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement10)




class Traceroutemeasurement11(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation11')


    def __str__(self):
        return '%s' % (self.id)


class Relation11(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement11)



class Traceroutemeasurement13(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation13')


    def __str__(self):
        return '%s' % (self.id)


class Relation13(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement13)





class Traceroutemeasurement14(models.Model):
    timestamp = models.DateTimeField(editable=True)
    countries= models.ManyToManyField(Countries, through='relation14')


    def __str__(self):
        return '%s' % (self.id)


class Relation14(models.Model):
    countries=models.ForeignKey(Countries)
    traceroutemeasurement=models.ForeignKey(Traceroutemeasurement14)





#class Traceroute1(models.Model):
 #   timestamp1 = models.DateTimeField(editable=True)
  #  countries = models.ManyToManyField(Countries)

#class Traceroute2(models.Model):
 #   timestamp = models.DateTimeField(editable=True)
  #  countries = models.ManyToManyField(Countries)
