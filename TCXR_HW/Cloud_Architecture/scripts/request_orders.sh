# This script automates pulling order CSV data from a partner API and loading it into Cloud Storage.

#!/usr/bin/env bash

# Exit immediately on errors, fail on unset variables, and make pipelines fail
# if any command inside them fails. This is a common "safe Bash" baseline.
set -euo pipefail

# Use environment overrides when provided, otherwise fall back to example values.
# This makes the script reusable across environments without editing the file.
API_BASE_URL="${API_BASE_URL:-https://partner.example.com/api/v1/orders}"
API_TOKEN="${API_TOKEN:-replace_me}"
BUCKET="${BUCKET:-gs://xyz-inventory-landing/raw/orders}"

# Build a UTC timestamp so each downloaded file gets a unique name.
# Example: 20260327T081530Z
RUN_TS="$(date -u +%Y%m%dT%H%M%SZ)"

# Store the API response in a local temporary file before uploading it to GCS.
LOCAL_FILE="/tmp/orders_${RUN_TS}.csv"

# Call the partner API and ask for CSV output.
# -sS keeps normal output quiet but still shows errors.
# The Authorization header sends the bearer token.
# The Accept header tells the API that CSV is expected.
# -o writes the response body into the local file instead of printing it.
curl -sS \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -H "Accept: text/csv" \
  "${API_BASE_URL}?since=1hour" \
  -o "${LOCAL_FILE}"

# Validate that the downloaded file exists and is not empty.
# "-s" means "file exists and has a size greater than zero".
# If this check fails, we stop immediately to avoid uploading a bad file.
if [[ ! -s "${LOCAL_FILE}" ]]; then
  echo "Downloaded file is empty. Exiting."
  exit 1
fi

# Copy the validated file into the target Google Cloud Storage location.
# We use "cp" here so the local temp file remains available for inspection
# if needed after upload.
gsutil cp "${LOCAL_FILE}" "${BUCKET}/orders_${RUN_TS}.csv"

# Print the final destination so the operator can confirm where the file went.
echo "Order file uploaded to ${BUCKET}/orders_${RUN_TS}.csv"
