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
    traceroutemeasurement12=models.ForeignKey(Traceroutemeasurement12)



#class Traceroute1(models.Model):
 #   timestamp1 = models.DateTimeField(editable=True)
  #  countries = models.ManyToManyField(Countries)

#class Traceroute2(models.Model):
 #   timestamp = models.DateTimeField(editable=True)
  #  countries = models.ManyToManyField(Countries)
