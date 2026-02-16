# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in this project, please report it responsibly and do not publicly disclose it until a patch is available.

### Report a Vulnerability

Please email security concerns to: [your-security-email@example.com]

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if applicable)

We will respond within 48 hours and work towards a fix.

### Disclosure Timeline

1. Vulnerability reported
2. Confirmation and assessment (48 hours)
3. Development of fix
4. Release of patched version
5. Public disclosure (after patch release)

## Supported Versions

| Version | Status | Security Updates |
|---------|--------|------------------|
| 1.0.x   | Active | Yes              |

## Security Best Practices

When using this software:

1. **Keep Dependencies Updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Use in Secure Environment**
   - Run on trusted networks only
   - Restrict access to input devices
   - Validate all input data

3. **Secure Configuration**
   - Store API keys securely
   - Use environment variables for sensitive data
   - Restrict file permissions

4. **Data Protection**
   - Ensure video input is from trusted sources
   - Sanitize any user-provided data
   - Protect trained models from unauthorized access

## Known Issues

None currently known. Please report any security concerns.

## Dependencies Security

We regularly monitor dependencies for known vulnerabilities:
- PyTorch
- YOLOv8 (Ultralytics)
- OpenCV
- Tesseract OCR
- Qt6

## Security Updates

Security patches will be released as soon as possible after discovery and validation.

## Contact

**Security Contact**: anas.bitta@usmba.ac.ma

**Maintainer LinkedIn**: https://www.linkedin.com/in/bitta-anas/

**GitHub**: https://github.com/BITTA-Anas

---

**Last Updated**: February 2026
**Policy Version**: 1.0
