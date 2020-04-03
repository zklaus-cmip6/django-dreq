# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cmorvar(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    stid = models.ForeignKey('Structure', models.DO_NOTHING, db_column='stid', blank=True, null=True)
    vid = models.ForeignKey('Var', models.DO_NOTHING, db_column='vid', blank=True, null=True)
    deflate = models.TextField(blank=True, null=True)
    deflate_level = models.TextField(blank=True, null=True)
    shuffle = models.TextField(blank=True, null=True)
    defaultpriority = models.IntegerField(db_column='defaultPriority', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(blank=True, null=True)
    modeling_realm = models.TextField(blank=True, null=True)
    positive = models.TextField(blank=True, null=True)
    miptablesection = models.TextField(db_column='mipTableSection', blank=True, null=True)  # Field name made lowercase.
    mtid = models.ForeignKey('Miptable', models.DO_NOTHING, db_column='mtid', blank=True, null=True)
    miptable = models.TextField(db_column='mipTable', blank=True, null=True)  # Field name made lowercase.
    prov = models.TextField(blank=True, null=True)
    processing = models.TextField(blank=True, null=True)
    provnote = models.TextField(db_column='provNote', blank=True, null=True)  # Field name made lowercase.
    frequency = models.TextField(blank=True, null=True)
    rowindex = models.IntegerField(db_column='rowIndex', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    subgroup = models.TextField(db_column='subGroup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMORvar'


class Cellmethods(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    cell_methods = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cellMethods'


class Experiment(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    egid = models.ForeignKey('Exptgroup', models.DO_NOTHING, db_column='egid', blank=True, null=True)
    mip = models.ForeignKey('Mip', models.DO_NOTHING, db_column='mip', blank=True, null=True)
    mcfg = models.TextField(blank=True, null=True)
    tier = models.TextField(blank=True, null=True)
    nstart = models.IntegerField(blank=True, null=True)
    starty = models.TextField(blank=True, null=True)
    endy = models.TextField(blank=True, null=True)
    yps = models.IntegerField(blank=True, null=True)
    ensz = models.TextField(blank=True, null=True)
    ntot = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment'


class Exptgroup(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    tiermin = models.IntegerField(db_column='tierMin', blank=True, null=True)  # Field name made lowercase.
    ntot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exptgroup'


class Grids(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    tables = models.TextField(blank=True, null=True)
    altlabel = models.TextField(db_column='altLabel', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    standardname = models.ForeignKey('Standardname', models.DO_NOTHING, db_column='standardName', blank=True, null=True)  # Field name made lowercase.
    axis = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    isindex = models.TextField(db_column='isIndex', blank=True, null=True)  # Field name made lowercase.
    coords = models.TextField(blank=True, null=True)
    bounds = models.TextField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    valid_min = models.TextField(blank=True, null=True)  # This field type is a guess.
    valid_max = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)
    positive = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    boundsvalues = models.TextField(db_column='boundsValues', blank=True, null=True)  # Field name made lowercase.
    requested = models.TextField(blank=True, null=True)
    boundsrequested = models.TextField(db_column='boundsRequested', blank=True, null=True)  # Field name made lowercase.
    tolrequested = models.TextField(db_column='tolRequested', blank=True, null=True)  # Field name made lowercase.
    isgrid = models.TextField(db_column='isGrid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grids'


class Mip(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mip'


class Miptable(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    frequency = models.TextField(blank=True, null=True)
    altlabel = models.TextField(db_column='altLabel', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'miptable'


class Modelconfig(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    mips = models.TextField(db_column='MIPs', blank=True, null=True)  # Field name made lowercase.
    usage = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    range = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelConfig'


class Objective(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='mip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objective'


class Objectivelink(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    oid = models.ForeignKey(Objective, models.DO_NOTHING, db_column='oid', blank=True, null=True)
    rid = models.ForeignKey('Requestlink', models.DO_NOTHING, db_column='rid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objectiveLink'


class Places(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    mip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='mip', blank=True, null=True)
    vid = models.ForeignKey(Cmorvar, models.DO_NOTHING, db_column='vid', blank=True, null=True)
    pid = models.ForeignKey('self', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'


class Qcranges(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    prov = models.TextField(blank=True, null=True)
    vid = models.ForeignKey(Cmorvar, models.DO_NOTHING, db_column='vid', blank=True, null=True)
    valid_min = models.TextField(blank=True, null=True)  # This field type is a guess.
    valid_max = models.TextField(blank=True, null=True)  # This field type is a guess.
    ok_min_mean_abs = models.TextField(blank=True, null=True)  # This field type is a guess.
    ok_max_mean_abs = models.TextField(blank=True, null=True)  # This field type is a guess.
    valid_min_status = models.TextField(blank=True, null=True)
    valid_max_status = models.TextField(blank=True, null=True)
    ok_min_mean_abs_status = models.TextField(blank=True, null=True)
    ok_max_mean_abs_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qcranges'


class Remarks(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    tid = models.TextField(blank=True, null=True)
    tattr = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    qid = models.TextField(blank=True, null=True)
    technote = models.TextField(db_column='techNote', blank=True, null=True)  # Field name made lowercase.
    prov = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remarks'


class Requestitem(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    mip = models.TextField(blank=True, null=True)
    tab = models.TextField(blank=True, null=True)
    expt = models.TextField(blank=True, null=True)
    rlid = models.ForeignKey('Requestlink', models.DO_NOTHING, db_column='rlid', blank=True, null=True)
    esid = models.ForeignKey('Requestitemtarget', models.DO_NOTHING, db_column='esid', blank=True, null=True)
    esidcomment = models.TextField(db_column='esidComment', blank=True, null=True)  # Field name made lowercase.
    preset = models.IntegerField(blank=True, null=True)
    treset = models.IntegerField(blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nexmax = models.IntegerField(blank=True, null=True)
    nenmax = models.IntegerField(blank=True, null=True)
    nymax = models.TextField(blank=True, null=True)  # This field type is a guess.
    tslice = models.ForeignKey('Timeslice', models.DO_NOTHING, db_column='tslice', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestItem'


class Requestitemtarget(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    kind = models.TextField(blank=True, null=True)
    experiment = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='experiment', blank=True, null=True)
    exptgroup = models.ForeignKey(Exptgroup, models.DO_NOTHING, db_column='exptgroup', blank=True, null=True)
    mip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='mip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestItemTarget'


class Requestlink(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    mip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='mip', blank=True, null=True)
    tab = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    grid = models.TextField(blank=True, null=True)
    gridreq = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    refnote = models.TextField(db_column='refNote', blank=True, null=True)  # Field name made lowercase.
    refid = models.ForeignKey('Requestvargroup', models.DO_NOTHING, db_column='refid', blank=True, null=True)
    opt = models.TextField(blank=True, null=True)
    opar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestLink'


class Requestvar(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    vid = models.ForeignKey(Cmorvar, models.DO_NOTHING, db_column='vid', blank=True, null=True)
    vgid = models.ForeignKey('Requestvargroup', models.DO_NOTHING, db_column='vgid', blank=True, null=True)
    mip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestVar'


class Requestvargroup(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    mip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='mip', blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    refnote = models.TextField(db_column='refNote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requestVarGroup'


class Spatialshape(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    dimensions = models.TextField(blank=True, null=True)
    dimids = models.TextField(blank=True, null=True)
    levels = models.IntegerField(blank=True, null=True)
    levelflag = models.BooleanField(db_column='levelFlag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spatialShape'


class Standardname(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    first_version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standardname'


class Structure(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    spid = models.ForeignKey(Spatialshape, models.DO_NOTHING, db_column='spid', blank=True, null=True)
    tmid = models.ForeignKey('Temporalshape', models.DO_NOTHING, db_column='tmid', blank=True, null=True)
    odims = models.TextField(blank=True, null=True)
    dids = models.TextField(blank=True, null=True)
    coords = models.TextField(blank=True, null=True)
    cids = models.TextField(blank=True, null=True)
    cell_methods = models.TextField(blank=True, null=True)
    cell_measures = models.TextField(blank=True, null=True)
    flag_values = models.TextField(blank=True, null=True)
    flag_meanings = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    procnote = models.TextField(db_column='procNote', blank=True, null=True)  # Field name made lowercase.
    prov = models.TextField(blank=True, null=True)
    cmid = models.ForeignKey(Cellmethods, models.DO_NOTHING, db_column='cmid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'structure'


class Tablesection(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    gpid = models.ForeignKey(Miptable, models.DO_NOTHING, db_column='gpid', blank=True, null=True)
    mip = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    refnote = models.TextField(db_column='refNote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tableSection'


class Tags(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Temporalshape(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    dimid = models.ForeignKey(Grids, models.DO_NOTHING, db_column='dimid', blank=True, null=True)
    dimensions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporalShape'


class Timeslice(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    step = models.TextField(blank=True, null=True)  # This field type is a guess.
    slicelen = models.IntegerField(db_column='sliceLen', blank=True, null=True)  # Field name made lowercase.
    nyears = models.TextField(blank=True, null=True)  # This field type is a guess.
    startlist = models.TextField(db_column='startList', blank=True, null=True)  # Field name made lowercase.
    slicelenunit = models.TextField(db_column='sliceLenUnit', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    child = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeSlice'


class Transfers(models.Model):
    uid = models.OneToOneField('Uids', models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    frid = models.ForeignKey(Places, models.DO_NOTHING, db_column='frid', blank=True, null=True)
    toid = models.ForeignKey(Places, models.DO_NOTHING, db_column='toid', blank=True, null=True)
    isoneway = models.BooleanField(db_column='isOneWay', blank=True, null=True)  # Field name made lowercase.
    signinverted = models.BooleanField(db_column='signInverted', blank=True, null=True)  # Field name made lowercase.
    mip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='mip', blank=True, null=True)
    vid = models.ForeignKey(Cmorvar, models.DO_NOTHING, db_column='vid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfers'


class Uids(models.Model):
    uid = models.TextField(primary_key=True)
    table_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uids'


class Units(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    group = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


class Var(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    sn = models.ForeignKey(Standardname, models.DO_NOTHING, db_column='sn', blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    procnote = models.TextField(blank=True, null=True)
    proccomment = models.TextField(db_column='procComment', blank=True, null=True)  # Field name made lowercase.
    prov = models.TextField(blank=True, null=True)
    provmip = models.ForeignKey(Mip, models.DO_NOTHING, db_column='provmip', blank=True, null=True)
    unid = models.ForeignKey(Units, models.DO_NOTHING, db_column='unid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'var'


class Varchoice(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    choiceclass = models.TextField(db_column='choiceClass', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    varlist = models.TextField(db_column='varList', blank=True, null=True)  # Field name made lowercase.
    optionlist = models.TextField(db_column='optionList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'varChoice'


class Varchoicelinkc(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    vid = models.ForeignKey(Cmorvar, models.DO_NOTHING, db_column='vid', blank=True, null=True)
    cfgid = models.ForeignKey(Modelconfig, models.DO_NOTHING, db_column='cfgid', blank=True, null=True)
    cfg = models.BooleanField(blank=True, null=True)
    cid = models.ForeignKey(Varchoice, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'varChoiceLinkC'


class Varchoicelinkr(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    vid = models.ForeignKey(Cmorvar, models.DO_NOTHING, db_column='vid', blank=True, null=True)
    cid = models.ForeignKey(Varchoice, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'varChoiceLinkR'


class Varrellnk(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    rlid = models.TextField(blank=True, null=True)
    rid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'varRelLnk'


class Varrelations(models.Model):
    uid = models.OneToOneField(Uids, models.DO_NOTHING, db_column='uid', primary_key=True)
    label = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    relation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'varRelations'
