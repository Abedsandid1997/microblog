# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Add

- Updated Security Groups to allow only necessary IP addresses for each port.
- Security Groups role now runs after VM creation.
- Added gather_instances task between VM creation and Security Groups to get dynamic IPs.
- Ports 22, 80, and 443 are open to all IPs; other ports restricted to relevant VMs.
- Updated the Ansible role 10-first-minute so that all servers now use the recommended and hardened SSH configuration. This ensures consistent security setting across the entire infrastructure and aligns with internal best practices.

## [11.4.4] - 2025-11-30

### Fixed

feat(site): Add database and microblog playbooks, store DATABASE_URL in .env

- Created new playbooks for setting up database and microblog services.
- Update site.yml to include database and microblog deployment tasks.
- Automatically generate .env file with DATABASE_URL so it can be reused when updating the Microblog image.

### Add

- Added playbook to deploy MySQL in Docker with persistent volume
- Added playbook to deploy Microblog container linked to the MySQL host
- Updated load balancer configuration to dynamically include all appservers
  via upstream generation.
- Added a new Ansible playbook `deploy_update` that performs rolling updates
- on application servers. This ensures minimal downtime during deployments
- and updates the servers in a controlled sequence
- pass microblog tag as argument to deploy_update.yml

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
