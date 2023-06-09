.PHONY: install run help
.DEFAULT_GOAL := help

install: ## Install the requirements
	@python3 -m pip install -r requirements.txt

run: clean ## Run the script
	@python3 main.py input.txt

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'