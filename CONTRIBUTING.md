# Contributing to AI Speed Limit Detection with Python Qt Dashboard

Thank you for your interest in contributing to this project! Here are some guidelines to help you get started.

## Getting Started

### Prerequisites

- Python 3.8+
- Qt6 development tools
- Tesseract OCR
- CUDA toolkit (optional, for GPU acceleration)
- Git

### Fork & Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR-USERNAME/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard.git
cd AI-Speed-Limit-Detection-with-Python-Qt-Dashboard

# Add upstream remote
git remote add upstream https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard.git
```

### Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Additional dev tools
```

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Use clear, descriptive branch names:
- `feature/add-multi-camera-support`
- `bugfix/fix-ocr-accuracy`
- `docs/update-installation-guide`

### 2. Make Your Changes

- Write clean, well-documented code
- Follow PEP 8 style guide for Python
- Use meaningful variable names
- Add comments for complex logic
- Ensure backward compatibility when possible

### 3. Test Your Changes

```bash
# Run tests
python -m pytest tests/

# Check code style
pylint *.py
flake8 *.py

# Type checking
mypy *.py
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "Clear description of your changes"
```

**Commit message format:**
```
[TYPE] Brief description (50 chars max)

Detailed explanation of the changes (if needed)
- Point 1
- Point 2

Closes #issue-number (if applicable)
```

**Commit types:**
- `[FEAT]` - New feature
- `[FIX]` - Bug fix
- `[DOCS]` - Documentation update
- `[REFACTOR]` - Code refactoring
- `[TEST]` - Test additions
- `[PERF]` - Performance improvements
- `[CI]` - CI/CD changes

### 5. Push & Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Detailed description of what was changed and why
- Reference to related issues (#123)
- Screenshots (for UI changes)
- Testing instructions

## Reporting Issues

### Bug Reports

Include:
- System information (OS, Python version, Qt version)
- Detailed steps to reproduce
- Expected vs actual behavior
- Error messages and logs
- Screenshots if applicable

### Feature Requests

Describe:
- Use case and motivation
- Proposed implementation (if any)
- Potential impact on existing features
- Examples or mockups

## Code Standards

### Python

```python
# Follow PEP 8
# Use type hints
def process_frame(frame: cv2.Mat) -> np.ndarray:
    """Process video frame for YOLO detection.
    
    Args:
        frame: Input video frame
        
    Returns:
        Processed frame ready for detection
    """
    pass

# Use docstrings
class SpeedLimitReader(QObject):
    """Monitors speed limit file changes."""
    pass
```

### C++

```cpp
// Follow Qt coding style
// Use meaningful names
// Document public APIs

class SpeedLimitReader : public QObject {
    Q_OBJECT
    
public:
    /**
     * @brief Constructor
     * @param parent Qt parent object
     */
    explicit SpeedLimitReader(QObject *parent = nullptr);
};
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all functions
- Include code examples for new features
- Update CHANGELOG.md

## Review Process

1. Code review by maintainers
2. Automated tests must pass
3. Documentation must be updated
4. Changes are merged to main branch

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to:
- Open an issue on GitHub
- Email: anas.bitta@usmba.ac.ma
- Contact the maintainer on LinkedIn: https://www.linkedin.com/in/bitta-anas/

---

**Last Updated**: February 2026
**Maintained By**: BITTA Anas
