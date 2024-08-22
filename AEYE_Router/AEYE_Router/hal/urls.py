from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views.AEYE_Inference import aeye_inference_Viewswets

from .views.AEYE_DataBase_WP    import aeye_database_patient_ViewSet
from .views.AEYE_DataBase_WC    import aeye_database_checkup_ViewSet
from .views.AEYE_DataBase_RD    import aeye_database_read_detail_ViewSet
from .views.AEYE_DataBase_RL    import aeye_database_read_list_ViewSet

router = DefaultRouter()


router.register(r'ai-inference', aeye_inference_Viewswets)

router.register(r'database-write-patient', aeye_database_patient_ViewSet)
router.register(r'database-write-checkup', aeye_database_checkup_ViewSet)
router.register(r'database-read-detail/<int:id>', aeye_database_read_detail_ViewSet)
router.register(r'database-read-list', aeye_database_read_list_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

