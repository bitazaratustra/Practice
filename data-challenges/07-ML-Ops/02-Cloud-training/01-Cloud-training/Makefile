#################### PACKAGE ACTIONS ###################

reinstall_package:
	@pip uninstall -y taxifare || :
	@pip install -e .

run_preprocess:
	python -c 'from taxifare.interface.main import preprocess; preprocess(); preprocess(source_type="val")'

run_train:
	python -c 'from taxifare.interface.main import train; train()'

run_pred:
	python -c 'from taxifare.interface.main import pred; pred()'

run_evaluate:
	python -c 'from taxifare.interface.main import evaluate; evaluate()'

run_all: run_preprocess run_train run_pred run_evaluate

# legacy directive
run_model: run_all

##################### TESTS #####################
default:
	@echo 'tests are only executed locally for this challenge'

test_cloud_training: test_gcp_setup test_gcp_project test_gcp_bucket test_big_query test_cloud_data

test_gcp_setup:
	@TEST_ENV=development pytest \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_key_env \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_key_path \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_code_get_project

test_gcp_project:
	@TEST_ENV=development pytest \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_project_id

test_gcp_bucket:
	@TEST_ENV=development pytest \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_bucket_exists \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_bucket_name

test_big_query:
	@TEST_ENV=development pytest \
	tests/cloud_data/test_cloud_data.py::TestCloudData::test_big_query_dataset_variable_exists \
	tests/cloud_data/test_cloud_data.py::TestCloudData::test_cloud_data_create_dataset \
	tests/cloud_data/test_cloud_data.py::TestCloudData::test_cloud_data_create_table \
	tests/cloud_data/test_cloud_data.py::TestCloudData::test_cloud_data_table_content

test_cloud_data:
	@TEST_ENV=development pytest tests/cloud_data/test_cloud_data.py::TestCloudData::test_cloud_data_bq_chunks

##################### DEBUGGING HELPERS ####################
fbold=$(shell echo "\033[1m")
fnormal=$(shell echo "\033[0m")
ccgreen=$(shell echo "\033[0;32m")
ccblue=$(shell echo "\033[0;34m")
ccreset=$(shell echo "\033[0;39m")

show_env:
	@echo "\nEnvironment variables used by the \`taxifare\` package loaded by \`direnv\` from your \`.env\` located at:"
	@echo ${DIRENV_DIR}

	@echo "\n$(ccgreen)local storage:$(ccreset)"
	@env | grep -E "LOCAL_DATA_PATH|LOCAL_REGISTRY_PATH" || :
	@echo "\n$(ccgreen)dataset:$(ccreset)"
	@env | grep -E "DATASET_SIZE|VALIDATION_DATASET_SIZE|CHUNK_SIZE" || :
	@echo "\n$(ccgreen)package behavior:$(ccreset)"
	@env | grep -E "DATA_SOURCE|MODEL_TARGET" || :

	@echo "\n$(ccgreen)GCP:$(ccreset)"
	@env | grep -E "PROJECT|REGION" || :

	@echo "\n$(ccgreen)Big Query:$(ccreset)"
	@env | grep -E "DATASET" | grep -Ev "DATASET_SIZE|VALIDATION_DATASET_SIZE" || :\

	@echo "\n$(ccgreen)Compute Engine:$(ccreset)"
	@env | grep -E "INSTANCE" || :

list:
	@echo "\nHelp for the \`taxifare\` package \`Makefile\`"

	@echo "\n$(ccgreen)$(fbold)PACKAGE$(ccreset)"

	@echo "\n    $(ccgreen)$(fbold)environment rules:$(ccreset)"
	@echo "\n        $(fbold)show_env$(ccreset)"
	@echo "            Show the environment variables used by the package by category."

	@echo "\n    $(ccgreen)$(fbold)run rules:$(ccreset)"
	@echo "\n        $(fbold)run_all$(ccreset)"
	@echo "            Run the package (\`taxifare.interface.main\` module)."

	@echo "\n$(ccgreen)$(fbold)TESTS$(ccreset)"

	@echo "\n    $(ccgreen)$(fbold)student rules:$(ccreset)"
	@echo "\n        $(fbold)reinstall_package$(ccreset)"
	@echo "            Install the version of the package corresponding to the challenge."
	@echo "\n        $(fbold)test_cloud_training$(ccreset)"
	@echo "            Run the tests."
