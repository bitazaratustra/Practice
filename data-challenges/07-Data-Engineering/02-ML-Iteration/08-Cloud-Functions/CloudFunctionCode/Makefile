
# - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Cloud Functions

FUNCTION_NAME=hacker-scrap
REGION=europe-west1
CODE_SOURCE_PATH=.
CODE_ENTRY_POINT=storage_upload
RUNTIME=python39
TIMEOUT=60s

deploy_function:
	gcloud functions deploy ${FUNCTION_NAME} \
		--region ${REGION} \
		--trigger-http \
		--no-allow-unauthenticated \
		--source ${CODE_SOURCE_PATH} \
		--entry-point ${CODE_ENTRY_POINT} \
		--runtime ${RUNTIME} \
		--timeout ${TIMEOUT}

list_function:
	gcloud functions list

describe_function:
	gcloud functions describe ${FUNCTION_NAME} \
		--region ${REGION} \

# - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Cloud Scheduler

JOB_NAME=job-name
JOB_FREQUENCY="* * * * *"
FUNCTION_URI="https://europe-west1-le-wagon-data.cloudfunctions.net/hacker-scrap"
SERVICE_ACCOUNT_EMAIL=le-wagon-data@le-wagon-data.iam.gserviceaccount.com

deploy_trigger:
	gcloud scheduler jobs create http ${JOB_NAME} \
		--schedule ${JOB_FREQUENCY} \
		--uri ${FUNCTION_URI} \
		--oidc-service-account-email ${SERVICE_ACCOUNT_EMAIL}

pause_trigger:
	gcloud scheduler jobs pause ${JOB_NAME}

resume_trigger:
	gcloud scheduler jobs resume ${JOB_NAME}

delete_trigger:
	gcloud scheduler jobs delete ${JOB_NAME} --quiet

list_trigger:
	gcloud scheduler jobs list

describe_trigger:
	gcloud scheduler jobs describe ${JOB_NAME}
