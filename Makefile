.PHONY: help install lint format typecheck imports test check run clean
.DEFAULT_GOAL := help

help: ## Show the targets
	@grep -E '^[a-z]+:.*## ' $(MAKEFILE_LIST) | awk -F ':.*## ' '{printf "  %-10s %s\n", $$1, $$2}'

install: ## Install the dependencies
	uv sync

lint: ## Lint the code
	uv run ruff check .

format: ## Format the code
	uv run ruff format .

typecheck: ## Check the types
	uv run basedpyright

imports: ## Check the import contracts
	uv run lint-imports

test: ## Run the tests with the coverage report
	uv run pytest

check: ## Run all the checks
	uv run ruff check .
	uv run ruff format --check .
	uv run basedpyright
	uv run lint-imports
	uv run pytest

run: ## Run the CLI, for example: make run ARGS="2 3"
	uv run change-me $(ARGS)

clean: ## Delete the caches and the build output
	rm -rf .pytest_cache .ruff_cache .import_linter_cache .coverage coverage.xml dist
