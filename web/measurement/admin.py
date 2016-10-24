from django.contrib import admin

# Register your models here.
from .models import Target, Countries
from .models import Probes
from .models import Specification
from .models import Countries
from .models import Traceroutemeasurement12
from .models import *
#from .models import Traceroute1
#from .forms import specificationForm
# Register your models here.

#admin.site.register(target)
#admin.site.register(probes)


#class specificationAdmin(admin.ModelAdmin):
#    form=specificationForm


#admin.site.register(specification,specificationAdmin)

admin.site.register(Target)
admin.site.register(Probes)
admin.site.register(Specification)
admin.site.register(Countries)
admin.site.register(Traceroutemeasurement12)
admin.site.register(Relation12)
admin.site.register(Traceroutemeasurement1)
admin.site.register(Relation1)
admin.site.register(Traceroutemeasurement2)
admin.site.register(Relation2)
admin.site.register(Traceroutemeasurement3)
admin.site.register(Relation3)
admin.site.register(Traceroutemeasurement4)
admin.site.register(Relation4)
admin.site.register(Traceroutemeasurement5)
admin.site.register(Relation5)
admin.site.register(Traceroutemeasurement6)
admin.site.register(Relation6)
admin.site.register(Traceroutemeasurement7)
admin.site.register(Relation7)
admin.site.register(Traceroutemeasurement8)
admin.site.register(Relation8)
admin.site.register(Traceroutemeasurement9)
admin.site.register(Relation9)
admin.site.register(Traceroutemeasurement10)
admin.site.register(Relation10)
admin.site.register(Traceroutemeasurement11)
admin.site.register(Relation11)
admin.site.register(Traceroutemeasurement13)
admin.site.register(Relation13)
admin.site.register(Traceroutemeasurement14)
admin.site.register(Relation14)



#admin.site.register(Traceroute1)