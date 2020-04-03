from django.contrib import admin


from .models import (
    Cellmethods,
    Cmorvar,
    Experiment,
    Exptgroup,
    Grids,
    Mip,
    Miptable,
    Modelconfig,
    Objective,
    Objectivelink,
    Places,
    Qcranges,
    Remarks,
    Requestitem,
    Requestitemtarget,
    Requestlink,
    Requestvar,
    Requestvargroup,
    Spatialshape,
    Standardname,
    Structure,
    Tablesection,
    Tags,
    Temporalshape,
    Timeslice,
    Transfers,
    Uids,
    Units,
    Var,
    Varchoice,
    Varchoicelinkc,
    Varchoicelinkr,
    Varrelations,
    Varrellnk,
)

# Register your models here.

admin.site.register(Cellmethods)
admin.site.register(Cmorvar)
admin.site.register(Experiment)
admin.site.register(Exptgroup)
admin.site.register(Grids)
admin.site.register(Mip)
admin.site.register(Miptable)
admin.site.register(Modelconfig)
admin.site.register(Objective)
admin.site.register(Objectivelink)
admin.site.register(Places)
admin.site.register(Qcranges)
admin.site.register(Remarks)
admin.site.register(Requestitem)
admin.site.register(Requestitemtarget)
admin.site.register(Requestlink)
admin.site.register(Requestvar)
admin.site.register(Requestvargroup)
admin.site.register(Spatialshape)
admin.site.register(Standardname)
admin.site.register(Structure)
admin.site.register(Tablesection)
admin.site.register(Tags)
admin.site.register(Temporalshape)
admin.site.register(Timeslice)
admin.site.register(Transfers)
admin.site.register(Uids)
admin.site.register(Units)
admin.site.register(Var)
admin.site.register(Varchoice)
admin.site.register(Varchoicelinkc)
admin.site.register(Varchoicelinkr)
admin.site.register(Varrelations)
admin.site.register(Varrellnk)
