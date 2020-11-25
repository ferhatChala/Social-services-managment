from django.contrib import admin
from App.models import Prime,Article
from import_export.admin import ImportExportModelAdmin


# Register your models here.

#admin.site.register(Prime)
#admin.site.register(Article)

@admin.register(Prime)
class PrimeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','employer','article','created_date','justif','state')
   # list_display = ('id','employer','article','created_date','justif','state','combine_employer_article')
    list_editable = ('state',)
    list_filter = ('state','article')
    search_fields = ('state','article__name','employer__username')

    def combine_employer_article(self,obj):
        return "{} - {}".format(obj.employer,obj.article)

#admin.site.register(Prime,PrimeAdmin)

#@admin.register(Prime)
#class PrimeImportExport(ImportExportModelAdmin):
 #   pass

@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','montant')
    list_editable = ('montant',)
    search_fields = ('name','montant')





