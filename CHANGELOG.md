# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [11.2.1] - 2025-11-12

### Added

- Added a dedicated test Dockerfile (`docker/Dockerfile_test`) to run automated tests.
- Added startup script to execute `make test` when the test container starts.
- Added new `test` service in `docker-compose.yml` to run tests via `docker-compose up test`.
- Added test nad push workflow in github action (CD).

### Changed

- Updated Docker setup validation with `make validate-docker`.
- Configured container to mount `app` and `tests` directories as volumes instead of copying files.

### Notes

- The test container installs dependencies from `requirements/test.txt`.
- Tests automatically execute on container startup and the container stops afterward.

## [11.1.1] - 2025-11-12

### Added

- Added a Dockerfile for the Microblog app in the `docker/` directory.
- Added a `docker-compose.yml` configuration to run Microblog with a MySQL container.
- Validated Docker setup with `make validate-docker`.

## [11.0.1] - 2025-11-12

### Added

- Added a commit message template to standardize commit messages.
- Added a `CHANGELOG.md` file to document all notable changes.

## [11.0.0] - 2025-11-10

### Initial Release

- First version of the project with basic structure set up.
