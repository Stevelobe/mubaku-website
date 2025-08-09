from django.contrib import admin
from .models import Enrollment
from .models import IncubatorApplication
from .models import Workshops

admin.site.register(Enrollment)
admin.site.register(IncubatorApplication)
admin.site.register(Workshops)
