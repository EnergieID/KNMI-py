# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-05-15

This release brings important fixes, modernizes the project's infrastructure, and improves compatibility.

### Fixed
- **Hourly Data Parsing:** Correctly parses hourly data from KNMI following a change in their CSV output (column `H` became `HH`). Resolves errors when fetching recent hourly data.
- **Outdated Stations:** Updated the internal list of KNMI stations, removing inactive ones that caused errors.
- **Pandas Warnings:** Resolved `FutureWarning` related to `parse_dates` in pandas.
- **Python 3.9 Compatibility:** Corrected type hints and function argument handling to ensure full compatibility with Python 3.9.
- **Readme Example:** Updated and corrected examples in the README.

### Changed
- **Project Packaging:** Migrated from `setup.py` to `pyproject.toml`, adopting modern Python packaging standards.
- **Dependency Management:** The project now uses `uv` for faster dependency management in development.
- **Supported Python Versions:** Officially supports Python 3.9 and newer.

### Added
- This `CHANGELOG.md` file to track changes.
- `pre-commit` hooks for automated code quality checks (Ruff, pyupgrade, etc.).
- `tox` configuration (using `tox-uv`) for testing across multiple Python versions.
---
