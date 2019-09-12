from django.contrib import admin
from HappyStore.models import POST
class POSTAdmin(admin.ModelAdmin):
    #inlines =['قیمت']
    list_display = ('oonvan', 'writer', 'updateDateTime',)
    list_editable = ('oonvan',)
    list_display_links = ('updateDateTime', 'writer')
    list_filter = ('updateDateTime','createDateTime')
    search_fields = ('oonvan', 'img', 'matn', 'createDateTime')


admin.site.register(POST,POSTAdmin)
# Register your models here.
