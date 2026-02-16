# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-16

### Added
- Initial release of AI Speed Limit Detection with Python Qt Dashboard
- Real-time speed limit sign detection using YOLOv8
- Tesseract OCR integration for digit extraction
- Qt6/QML graphical interface with dynamic gauge
- GPU acceleration support (CUDA)
- JSON-based inter-process communication
- Data logging to CSV files
- Support for French standard speed limits (20, 30, 40, 50, 60, 80, 100, 120 km/h)
- Comprehensive documentation and guides
- Code examples and troubleshooting section

### Features
- YOLOv8 real-time object detection
- OpenCV video capture and preprocessing
- Advanced image processing pipeline
- Multi-threaded frame processing
- GPU acceleration with CUDA support
- Dynamic UI with real-time updates
- Persistent data storage
- Professional error handling

### Documentation
- Detailed README with installation instructions
- API reference for C++ components
- Configuration guide
- Performance optimization tips
- Troubleshooting section
- CONTRIBUTING guide
- CODE_OF_CONDUCT
- SECURITY policy
- COPYRIGHT notice

### Project Files
- LICENSE (MIT License)
- COPYRIGHT (Intellectual Property Rights)
- CODE_OF_CONDUCT (Community Standards)
- CONTRIBUTING (Contribution Guidelines)
- SECURITY (Security Policy)
- CHANGELOG (This file)

---

## Planned Features

### Version 1.1.0 (Planned)
- [ ] Multi-camera support
- [ ] Improved OCR accuracy with advanced filters
- [ ] Performance optimization
- [ ] Additional language support

### Version 1.2.0 (Planned)
- [ ] Real-time speed limit enforcement
- [ ] Network communication capability
- [ ] REST API interface
- [ ] Mobile app integration

### Version 2.0.0 (Planned)
- [ ] Kalman filtering for tracking
- [ ] Machine learning-based validation
- [ ] Docker containerization
- [ ] Kubernetes deployment support
- [ ] Cloud integration options

---

## Version Guidelines

### Semantic Versioning

- **MAJOR** (X.0.0): Breaking changes, major features
- **MINOR** (0.X.0): New features, non-breaking changes
- **PATCH** (0.0.X): Bug fixes, minor improvements

---

## Release Notes Archive

### Release Process

1. Update version in all relevant files
2. Update CHANGELOG with changes
3. Create git tag: `git tag v1.0.0`
4. Push to GitHub: `git push origin v1.0.0`
5. Create GitHub Release with changelog

### Maintenance Policy

- Security patches: Released within 48 hours
- Bug fixes: Released in next minor version
- Feature releases: Following semantic versioning
- LTS versions: Supported for 2 years

---

## Deprecations

None currently deprecated.

---

## Known Issues

### Current Version (1.0.0)
- Single camera input only
- OCR accuracy depends on sign image quality
- Real-time performance varies by hardware

---

## Migration Guides

### Upgrading from 0.x to 1.0.0

This is the initial release. No migration needed.

---

## Contributors

- BITTA Anas (@BITTA-Anas)

---

## License

All changes and new code are licensed under the MIT License.

---

## Reporting Issues

Found a bug? Please report it on GitHub:
https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard/issues

---

**Last Updated**: February 16, 2026
**Current Version**: 1.0.0
**Maintained By**: BITTA Anas

For more information, visit:
https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard
