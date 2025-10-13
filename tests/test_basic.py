"""Basic tests for your package."""

import kpipe


def test_version():
    """Test that the package version is defined."""
    assert hasattr(kpipe, "__version__")
    assert isinstance(kpipe.__version__, str)
