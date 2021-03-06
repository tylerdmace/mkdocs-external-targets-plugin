from setuptools import setup

setup(
    name="mkdocs-external-targets-plugin",
    version="0.1.0",
    packages=["mkdocs_external_targets_plugin"],
    url="https://github.com/tylerdmace/mkdocs-external-targets-plugin",
    license="BSD 2-Clause",
    author="Tyler Mace",
    author_email="tylerdmace@gmail.com",
    description="Mkdocs plugin to convert absolute paths to Webcontext aware paths.",
    entry_points={
        "mkdocs.plugins": [
            "external-targets = mkdocs_external_targets_plugin:ExternalTargets"
        ]
    }
)