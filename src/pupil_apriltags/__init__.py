try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("pupil-apriltags")
except PackageNotFoundError:
    # package is not installed
    pass

from .bindings import Detection, Detector

__all__ = ["Detector", "Detection"]
