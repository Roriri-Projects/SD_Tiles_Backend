from rest_framework.routers import SimpleRouter
from django.urls import path
from apps.BASE.views.generic import get_upload_api_view


#Bulk-Upload-Files
from HELPERS import BulkFileUploadView, ActiveStatusChange, ArchieveStatusChange

app_name = "cms"
API_URL_PREFIX = "api/"

router = SimpleRouter()




urlpatterns = [
    
    
    #bulk upload images
    path('property/files/bulk-upload/', BulkFileUploadView.as_view(), name='bulk-upload-images'),
    
    #status change
    path('active/status/change/', ActiveStatusChange.as_view(), name='active-status'),
    path('deleted/status/change/', ArchieveStatusChange.as_view(), name='delete-status'),



] + router.urls
