#!/bin/sh
# Create a standalone git repository for the OCR microservice.
set -e
TARGET_DIR="${1:-../ocr_microservice_repo}"
mkdir -p "$TARGET_DIR"
cp -r "$(dirname "$0")"/* "$TARGET_DIR"
cd "$TARGET_DIR"
rm -f export_repo.sh
if [ ! -d .git ]; then
    git init .
    git add .
    git commit -m "Initial commit of OCR microservice"
fi
printf 'Repository created at %s\n' "$TARGET_DIR"

