.. image:: https://img.shields.io/pypi/v/pupil-apriltags.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/pupil-apriltags.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/pupil-apriltags

.. image:: https://github.com/pupil-labs/apriltags/workflows/tests/badge.svg
   :target: https://github.com/pupil-labs/apriltags/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://readthedocs.org/projects/pupil-apriltags/badge/?version=latest
   :target: https://pupil-apriltags.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2022-informational
   :target: https://blog.jaraco.com/skeleton

pupil-apriltags: Python bindings for the apriltags3 library
===========================================================

These are Python bindings for the
`Apriltags3 <https://github.com/AprilRobotics/apriltags>`__ library
developed by `AprilRobotics <https://april.eecs.umich.edu/>`__,
specifically adjusted to work with the pupil-labs software. The original
bindings were provided by
`duckietown <https://github.com/duckietown/apriltags3-py>`__ and were
inspired by the `Apriltags2
bindings <https://github.com/swatbotics/apriltag>`__ by `Matt
Zucker <https://github.com/mzucker>`__.

Install from PyPI
~~~~~~~~~~~~~~~~~

This is the recommended and easiest way to install pupil-apriltags.

.. code:: sh

   pip install pupil-apriltags

We offer pre-built binary wheels for common operating systems. To install from source,
see below.

Usage
~~~~~

Some examples of usage can be seen in the
``src/pupil_apriltags/bindings.py`` file.

The ``Detector`` class is a wrapper around the Apriltags functionality.
You can initialize it as following:

.. code:: python

   from pupil_apriltags import Detector

   at_detector = Detector(
      families="tag36h11",
      nthreads=1,
      quad_decimate=1.0,
      quad_sigma=0.0,
      refine_edges=1,
      decode_sharpening=0.25,
      debug=0
   )

   at_detector.detect(img)

See the `API reference documentation <https://pupil-apriltags.readthedocs.io/en/stable/api.html>`__
for details.

Manual installation from source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can of course clone the repository and build from there. For
development you should install the development requirements as well.
This project uses the new python build system configuration from `PEP
517 <https://www.python.org/dev/peps/pep-0517/>`__ and `PEP
518 <https://www.python.org/dev/peps/pep-0518/>`__.

.. code:: sh

   # clone the repository
   git clone --recursive https://github.com/pupil-labs/apriltags.git
   cd apriltags

   # install apriltags in editable mode with development requirements
   pip install -e .[testing]

   # run tests
   pytest tests/
