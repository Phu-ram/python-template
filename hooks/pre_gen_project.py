"""Pre-generation hook.

See https://cookiecutter.readthedocs.io/en/1.7.0/advanced/hooks.html#example-validating-template-variables
"""

import sys


python_version = "{{ cookiecutter.python_version }}"
supported_python_versions = [
    "3.10",
    "3.11",
]
if python_version not in supported_python_versions:
    print(f"ERROR: Unsupported Python version {python_version}. Supported versions: {supported_python_versions}")
    sys.exit(1)
