# Tool demos

Each file in this folder breaks the rules of one tool on purpose. The default
runs of the tools skip this folder, so the project checks stay green. Run the
commands below from the project root to see each tool report a problem.

| Tool | Demo | Command |
|------|------|---------|
| basedpyright | `basedpyright_demo.py` | `uv run basedpyright examples/basedpyright_demo.py` |
| ruff lint | `ruff_lint_demo.py` | `uv run ruff check examples/ruff_lint_demo.py` |
| ruff format | `ruff_format_demo.py` | `uv run ruff format --diff examples/ruff_format_demo.py` |
| import-linter | `import_linter_demo/` | `cd examples/import_linter_demo && uv run lint-imports` |
| test coverage | `coverage_demo/` | `uv run pytest -c examples/coverage_demo/pytest.ini --cov=examples/coverage_demo examples/coverage_demo` |

## Expected results

- **basedpyright**: 3 errors. An `int` goes into a `str` parameter, a `str`
  goes into an `int` variable, and the code calls `.upper()` on an `int`.
- **ruff lint**: 12 errors, for example `unused-import` (F401),
  `mutable-argument-default` (B006), `none-comparison` (E711) and
  `undocumented-public-module` (D100). Add `--fix` to repair the 5 errors
  that ruff can fix.
- **ruff format**: a diff that adds blank lines, spaces and double quotes.
  Drop `--diff` to write the change.
- **import-linter**: 1 broken contract. `shop.domain` imports `shop.web`, but
  the layers contract in `.importlinter` lets only `web` import `domain`.
- **test coverage**: lines 7 and 10 of `discount.py` are missing, and the run
  fails because 69 % is below `fail_under = 80` from `pyproject.toml`.

