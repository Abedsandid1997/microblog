# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [11.3.4] - 2025-11-14

### Fixed

- Fixed the follow bugs

## [11.3.3] - 2025-11-14

### Added

- Added followers association table (`app/models.py`).
- Added `follow()`, `unfollow()`, and `is_following()` methods to User mode (`app.user`).
- Added `followed_posts()` method to retrieve posts from followed users.
- Added `follow()` and `unfollow()` routes (`app/main/routes.py`).
- Added follow/unfollow links to user profile te,plate (`app/templates/user.html`).
- Added unit tests for follow functionality (`tests/unit/models/test_follow.py`)

### Changed

- Updated database schema with followers table via Flask-Migrate.
- Modified User model to include follower relationships.
- Updated index route to display posts from followed users.
- Enhanced user profile template with follower statistics.

## [11.2.3] - 2025-11-12

### Changed

-Updated test gworkflow

## [11.2.2] - 2025-11-12

### Added

- Added test and validate workflow in github action (CD).

## [11.2.1] - 2025-11-12

### Added

- Added a dedicated test Dockerfile (`docker/Dockerfile_test`) to run automated tests.
- Added startup script to execute `make test` when the test container starts.
- Added new `test` service in `docker-compose.yml` to run tests via `docker-compose up test`.

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
