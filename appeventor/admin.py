from django.contrib import admin
from .models import Reservation, datadesire, FakePayment, UserDocument, Feedback, user_query, inquiry

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'venue', 'typeofevent', 'dateprimary', 'datesecondary')
    search_fields = ('name', 'email', 'venue')
    list_filter = ('venue', 'typeofevent', 'dateprimary')

@admin.register(datadesire)
class DatadesireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')

@admin.register(FakePayment)
class FakePaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'transaction_id', 'status', 'timestamp')
    list_filter = ('status',)

admin.site.register(UserDocument)
admin.site.register(Feedback)
admin.site.register(user_query)
admin.site.register(inquiry)