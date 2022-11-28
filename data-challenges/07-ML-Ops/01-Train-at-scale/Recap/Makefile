#################### PACKAGE ACTIONS ###################

reinstall_package:
	@pip uninstall -y taxifare || :
	@pip install -e .

##################### TESTS #####################
default:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -v --color=yes

test_train_at_scale: test_train_at_scale_3 \
	test_train_at_scale_5 \
	test_train_at_scale_6

test_train_at_scale_3:
	@pytest \
	tests/train_at_scale/test_data.py \
	tests/train_at_scale/test_preprocessing.py \
	tests/train_at_scale/test_model.py \
	tests/train_at_scale/test_interface.py::TestInterface::test_route_preprocess_and_train \
	tests/train_at_scale/test_interface.py::TestInterface::test_route_pred

test_train_at_scale_5:
	@pytest \
	tests/train_at_scale/test_interface.py::TestInterface::test_route_preprocess

test_train_at_scale_6:
	@pytest \
	tests/train_at_scale/test_interface.py::TestInterface::test_route_train
