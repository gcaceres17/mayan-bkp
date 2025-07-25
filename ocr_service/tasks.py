import os
from celery import chord
from celery import shared_task
from subprocess import check_output, CalledProcessError

from .celery_app import app

@shared_task(bind=True, max_retries=3)
def process_page(self, page_path, language='eng'):
    try:
        output = check_output(['tesseract', page_path, 'stdout', '-l', language])
        return output.decode('utf-8')
    except CalledProcessError as exc:
        raise self.retry(exc=exc, countdown=10)

@shared_task(bind=True)
def process_document(self, document_dir, language='eng'):
    pages = sorted([
        os.path.join(document_dir, f) for f in os.listdir(document_dir)
        if f.lower().endswith('.png')
    ])
    callback = document_finished.s()
    header = [process_page.s(page, language=language) for page in pages]
    return chord(header)(callback)

@shared_task
def document_finished(pages_results):
    return '\n'.join(pages_results)
