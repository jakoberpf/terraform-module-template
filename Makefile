SHELL := /bin/bash

## Lint terraform code
lint:
	@echo "TODO"

terraform-docs:
	@terraform-docs markdown table --output-file docs/terraform.md --output-mode inject .
