"""Basic tests for your package."""

import pipelinestep


def test_version():
    """Test that the package version is defined."""
    assert hasattr(pipelinestep, "__version__")
    assert isinstance(pipelinestep.__version__, str)


def test_info():
    """Test the info function."""
    result = pipelinestep.info()
    assert result == "Hello World"
    assert isinstance(result, str)
