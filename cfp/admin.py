from django.contrib import admin

from cfp.models import Call, Conference, Track, Profile, Talk, Format


class CallInline(admin.StackedInline):
    model = Call
    extra = 0
    readonly_fields = ('state',)


class TrackInline(admin.StackedInline):
    model = Track


class FormatInline(admin.StackedInline):
    model = Format


def make_all_approved(modeladmin, request, queryset):
    for conf in queryset.all():
        for call in conf.call_set.all():
            call.approve()
            call.save()
make_all_approved.short_description = "Mark selected calls as approved"


def make_all_rejected(modeladmin, request, queryset):
    for conf in queryset.all():
        for call in conf.call_set.all():
            call.reject()
            call.save()
make_all_rejected.short_description = "Mark selected calls as rejected"


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    inlines = [
        CallInline,
        TrackInline,
        FormatInline,
    ]
    list_filter = ('call__state', 'created')
    list_display = ('name', 'start', 'end', 'created')
    readonly_fields = ('maps_url',)
    search_fields = ['name']
    actions = [make_all_approved, make_all_rejected]


def make_approved(modeladmin, request, queryset):
    for call in queryset.all():
        call.approve()
        call.save()
make_approved.short_description = "Mark selected calls as approved"


def make_spam(modeladmin, request, queryset):
    for call in queryset.all():
        call.quarantine()
        call.save()
make_approved.short_description = "Mark selected calls as spam"


def make_rejected(modeladmin, request, queryset):
    for call in queryset.all():
        call.reject()
        call.save()
make_rejected.short_description = "Mark selected calls as rejected"


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('conference', 'start', 'end', 'created', 'state')
    list_filter = ('state', 'created', 'hosted')
    readonly_fields = ('state',)
    search_fields = ['conference__name']
    actions = [make_approved, make_rejected, make_spam]


def make_submitted(modeladmin, request, queryset):
    for talk in queryset.all():
        talk.submit()
        talk.save()
make_submitted.short_description = "Mark selected talks as submitted"


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    readonly_fields = ('call', 'state', 'token',)
    list_filter = ('state', 'created')
    list_display = ('title', 'call', 'profile', 'created', 'state')
    actions = [make_submitted]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address',
                    'owner', 'created')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    pass


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    pass
