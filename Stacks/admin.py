from django.contrib import admin
from Stacks.models import DjangoModel, Laravel, Node,React, Ui_ux

# Register your models here.
admin.site.register(DjangoModel),
admin.site.register(React),
admin.site.register(Node),
admin.site.register(Ui_ux),
admin.site.register(Laravel),
