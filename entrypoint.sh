#!/usr/bin/env bash
set -e

# Default to dev settings locally
export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-project32.settings.dev}"

# Apply DB migrations every start (idempotent)
python manage.py migrate --noinput

# Collect static only if explicitly enabled
if [ "${DJANGO_COLLECTSTATIC:-0}" = "1" ]; then
  python manage.py collectstatic --noinput
fi

# Hand off to the main process
exec "$@"
