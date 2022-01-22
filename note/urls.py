from django.urls import path
from .views import (
    note_create_form,
    note_list,
    note_edit_form,
    note_edit,
    note_delete
)

urlpatterns = [
    path('note_create_form/', note_create_form),
    path('note_list/', note_list),
    path('note_edit_form/<int:id>', note_edit_form),
    path('note_edit/<int:id>', note_edit),
    path('note_delete/<int:id>', note_delete)
]
