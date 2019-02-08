PROJECT_NAME = sam-lambda-python

include .faas

test:
	@ pytest
