test:
	coverage run test.py

test-verbose:
	coverage run test.py -v
coverage:
	coverage report -m

lint:
	pylint primenumber test

.PHONY: test
all: test coverage lint
