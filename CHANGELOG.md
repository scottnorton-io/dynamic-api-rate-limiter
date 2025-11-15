# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- TBD

## [0.1.0] - Initial public release

### Added

- Dynamic AIMD-based `DynamicRateLimiter` with token-bucket implementation.
- `DynamicAPIClient` that respects 429 responses and `Retry-After` headers.
- Central `ApiRateConfig` registry with initial configs for Notion, Vanta, and Fieldguide.
- `make_client_for()` factory for one-line client creation.
- Logging integration and `snapshot()` for metrics/observability.
- Examples for Notion, Vanta, Fieldguide, logging/metrics, and multi-status backoff.
- CI workflow (lint + tests) and basic test suite.
- Documentation: `README.md`, `USAGE.md`, `background.md`, `METRICS.md`, `CONTRIBUTING.md`.
- MIT license.
