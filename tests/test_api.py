import pytest

import pupil_apriltags as this_project


def test_package_metadata() -> None:
    assert hasattr(this_project, "__version__")


@pytest.fixture
def detector():
    return this_project.Detector()


def test_detector_init(detector):
    print(detector)
