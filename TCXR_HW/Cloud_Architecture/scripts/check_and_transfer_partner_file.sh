# This script automates checking for a daily file on partner SFTP, downloading it, validating it, and transferring it to Cloud Storage.

#!/usr/bin/env bash

# Exit immediately on errors, fail on unset variables, and make pipelines fail
# if any command inside them fails. This reduces the chance of silently
# continuing after a bad download or transfer step.
set -euo pipefail

# Use environment variables when available so the same script can be reused
# across environments. The values on the right are example defaults.
SFTP_HOST="${SFTP_HOST:-sftp.partner-example.com}"
SFTP_USER="${SFTP_USER:-partner_user}"
SFTP_REMOTE_DIR="${SFTP_REMOTE_DIR:-/exports/inventory}"
LOCAL_DIR="${LOCAL_DIR:-/tmp/partner_inventory}"
BUCKET="${BUCKET:-gs://xyz-inventory-landing/raw/partner}"

# Generate today's UTC date and use it to build the expected filename.
# Example: inventory_20260327.csv
DATE_UTC="$(date -u +%Y%m%d)"
EXPECTED_FILE="inventory_${DATE_UTC}.csv"

# Ensure the local download directory exists before trying to fetch the file.
mkdir -p "${LOCAL_DIR}"

# Print the expected filename so the operator knows what the script is checking.
echo "Checking for ${EXPECTED_FILE} on partner SFTP..."

# Open an SFTP session and feed a short command script into it:
# 1. cd  -> change the remote directory on the partner server
# 2. lcd -> change the local directory on this machine
# 3. get -> download the expected file
# 4. bye -> close the session
# The heredoc (<<EOF ... EOF) is how we pass multiple commands to sftp.
sftp "${SFTP_USER}@${SFTP_HOST}" <<EOF
cd ${SFTP_REMOTE_DIR}
lcd ${LOCAL_DIR}
get ${EXPECTED_FILE}
bye
EOF

# Build the full local path of the downloaded file so we can validate it.
LOCAL_FILE="${LOCAL_DIR}/${EXPECTED_FILE}"

# Check that the file actually exists after the SFTP download attempt.
# "-f" means "a regular file exists at this path".
if [[ ! -f "${LOCAL_FILE}" ]]; then
  echo "Expected file not found: ${EXPECTED_FILE}"
  exit 1
fi

# Check that the file is not empty.
# "-s" means "file exists and has a size greater than zero".
# This protects us from transferring empty placeholder files into the pipeline.
if [[ ! -s "${LOCAL_FILE}" ]]; then
  echo "File exists but is empty: ${EXPECTED_FILE}"
  exit 1
fi

# Move the validated file into the target Google Cloud Storage location.
# We use "mv" instead of "cp" so the local temporary copy is removed after
# a successful transfer.
gsutil mv "${LOCAL_FILE}" "${BUCKET}/${EXPECTED_FILE}"

# Print the final destination so it is easy to confirm the transfer result.
echo "Transferred ${EXPECTED_FILE} to ${BUCKET}/${EXPECTED_FILE}"
