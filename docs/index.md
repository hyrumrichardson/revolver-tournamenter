# template-python
<!-- 
[![ci](https://github.com/br3ndonland/template-python/workflows/ci/badge.svg)](https://github.com/br3ndonland/template-python/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) -->

## Description

**Welcome!** This is a Python script for generating pairings and a scoresheet for the monthly Revolver League Magic: The Gathering constructed tournaments that take place at Austin Books & Games (formerly Outlaw Moon).

## Quickstart

[Install Hatch](https://hatch.pypa.io/latest/install/), rename the project, then install the project:

```sh
# set your names
repo_name="your-repo-name"
your_name="Your Name"
your_user="YourGitHubUsername"

# update repo for new names
git mv "src/template_python" "src/${repo_name//-/_}"
git grep -l "br3ndonland" | xargs sed -i "s|br3ndonland|$your_user|g"
git grep -l "Brendon Smith" | xargs sed -i "s|Brendon Smith|$your_name|g"
git grep -l "template_python" | xargs sed -i "s|template_python|${repo_name//-/_}|g"
git grep -l "template-python" | xargs sed -i "s|template-python|$repo_name|g"

# run tests to verify
hatch run coverage run
```

## Documentation

Documentation is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

