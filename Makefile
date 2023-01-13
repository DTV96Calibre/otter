all: venv
venv:
	python3 -m venv .venv
	@echo "To activate the virtual environment on bash use 'source .venv/bin/activate'"
	@echo "NOTICE: .venv uses absolute paths in it's scripts and must be recreated if this project's root is moved."
