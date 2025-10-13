# Your Package Name

A short description of what your package does.

## Installation

```bash
pip install your-package-name
```

## Usage

```python
import your_package_name

# Add usage examples here
```

## Development

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/your-package-name.git
cd your-package-name
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/ tests/
```

### Type Checking

```bash
mypy src/
```

## Publishing

This package is automatically published to PyPI when a new release is created on GitHub.

To create a new release:
1. Update the version in `pyproject.toml`
2. Create a new git tag: `git tag v0.1.0`
3. Push the tag: `git push origin v0.1.0`
4. Create a release on GitHub with the same tag

The GitHub Action will automatically build and publish the package to PyPI.

## License

MIT License - see LICENSE file for details.
