# CHANGE-ME

A minimal Python project template.

## Layout

```text
src/change_me/   package source code
tests/           pytest tests
examples/        demo files that break each tool on purpose
```

## Quick start

1. Install [uv](https://docs.astral.sh/uv/).

2. Rename the template. The template name is `change-me` (package
   `change_me`). The commands below use `my-project` (package `my_project`)
   as the new name. Replace both with your own name:

   ```sh
   mv src/change_me src/my_project
   grep -rlE 'change_me|change-me|CHANGE-ME' --exclude=uv.lock . \
     | xargs sed -i '' -e 's/change_me/my_project/g' \
         -e 's/change-me/my-project/g' -e 's/CHANGE-ME/my-project/g'
   ```

   On Linux, use `sed -i` instead of `sed -i ''`.

3. Install the dependencies:

   ```sh
   uv sync
   ```

4. Run all the checks:

   ```sh
   make check
   ```

5. Add code:
   - Put modules in `src/my_project/`, for example `src/my_project/greet.py`.
   - Import with the full package path: `from my_project.greet import hello`.
   - Put tests in `tests/`, in files that start with `test_`.
   - Add a runtime dependency with `uv add <package>`.
   - Add a dev tool with `uv add --dev <package>`.

6. Run the code:

   ```sh
   make run ARGS="2 3"     # prints 5
   uv run my-project 2 3   # the same without make
   ```

   To change the command, edit `[project.scripts]` in `pyproject.toml`.

## Develop

Run `make` to list the targets. Each target runs one of these commands:

```sh
uv run ruff check .            # lint
uv run ruff format .           # format
uv run basedpyright            # type check
uv run lint-imports            # check the import contracts
uv run pytest                  # tests + coverage report (coverage.xml)
```

`uv run pytest` fails when the coverage of `change_me` drops below 80 %
(`[tool.coverage.report]` in `pyproject.toml`).

## Examples

`examples/README.md` shows each tool on a file with planted problems.
