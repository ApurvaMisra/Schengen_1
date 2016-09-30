from django.contrib import admin

# Register your models here.
from .models import Target, Countries
from .models import Probes
from .models import Specification
from .models import Countries
from .models import Traceroutemeasurement12
from .models import Relation12
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
#admin.site.register(Traceroute1)