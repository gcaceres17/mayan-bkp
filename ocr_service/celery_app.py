from celery import Celery

app = Celery('ocr_service')
app.config_from_object('ocr_service.celery_config', namespace='CELERY')
