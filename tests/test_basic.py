"""Basic tests for your package."""

import kpipe


def test_version():
    """Test that the package version is defined."""
    assert hasattr(kpipe, "__version__")
    assert isinstance(kpipe.__version__, str)


def test_info():
    """Test the info function."""
    result = kpipe.info()
    assert result == "Hello World"
    assert isinstance(result, str)
