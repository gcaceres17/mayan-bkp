# OCR Microservice

This folder contains a minimal microservice that performs OCR on images
using Celery tasks. Each document directory is expected to contain PNG
images corresponding to pages.

## Usage

1. Ensure `tesseract` and `redis` are installed and running.
2. Start the Celery worker:

```bash
celery -A ocr_service.celery_app worker -l info
```

3. Call the task from Python:

```python
from ocr_service.tasks import process_document
process_document.delay('/path/to/document')
```

The result will be a string containing the OCR text from all pages.

## Exporting as a standalone repository

Run `export_repo.sh` to copy this folder and initialize a new Git
repository. By default the new repository will be created next to this
project under `../ocr_microservice_repo`.

```bash
./export_repo.sh
```

You can pass a directory path as the first argument to place the new
repository elsewhere.

