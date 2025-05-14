# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-05-14

This release brings important fixes and modernizes the project's infrastructure.

### Fixed
- **Hourly Data Parsing:** Correctly parses hourly data from KNMI following a change in their CSV output (column `H` became `HH`). This resolves errors when fetching recent hourly data (Fixes Issue #23, addressed in PR #18).
- **Outdated Stations:** Updated the internal list of KNMI stations, removing inactive ones that caused errors (Fixes Issue #15, addressed in PR #19).
- **Pandas Warnings:** Resolved `FutureWarning` related to `parse_dates` in pandas (Addressed in PR #18).
- **Readme Example:** Updated the example in the README to ensure it's functional.

### Changed
- **Project Packaging:** Migrated from `setup.py` to `pyproject.toml`, adopting modern Python packaging standards.
- **Dependency Management:** The project now uses `uv` for faster dependency management in development.
- **Supported Python Versions:** Officially updated to support modern Python versions (Python 3.9+).

### Added
- This `CHANGELOG.md` file to track changes.

---