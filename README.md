# Test Python Project (PIP)

Tests component locator support for PIP package manager.

## Vulnerable Dependencies
- `Django==2.2.0` - Multiple CVEs
- `requests==2.20.0` - Known vulnerabilities
- `urllib3==1.24.1` - Security issues
- `Jinja2==2.10.0` - XSS vulnerabilities
- `Flask==1.0.0` - Old version

## Expected Behavior
When Blackduck Detect runs:
1. Detects PIP package manager
2. Finds vulnerable components in requirements.txt
3. Component locator should process (not skip) PIP manager
4. Locates components in requirements.txt file
