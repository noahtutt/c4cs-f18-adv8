test: test_rpn.py
	python3 -m unittest
covrun: test_rpn.py
	coverage run -m unittest
	coverage report -m 

.PHONY: test covrun
