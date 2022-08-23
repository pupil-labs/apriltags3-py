.. image:: https://img.shields.io/pypi/v/pupil-apriltags.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/pupil-apriltags.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/pupil-apriltags

.. image:: https://github.com/pupil-labs/pupil-apriltags/workflows/tests/badge.svg
   :target: https://github.com/pupil-labs/pupil-apriltags/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/pupil-apriltags/badge/?version=latest
..    :target: https://pupil-apriltags.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2021-informational
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

How to get started:
-------------------

Requirements
~~~~~~~~~~~~

Note that **pupil-apriltags** currently only runs on Python 3.6 or
higher.

Also we are using a newer python build system, which can fail for older
versions of pip with potentially misleading errors. Please make sure you
are using pip > 19 or consider upgrading pip to the latest version to be
on the safe side:

.. code:: bash

   python -m pip install --upgrade pip

Install from PyPI
~~~~~~~~~~~~~~~~~

This is the recommended and easiest way to install pupil-apriltags.

.. code:: sh

   pip install pupil-apriltags

We offer pre-built binary wheels for common operating systems. In case
your system does not match, the installation might take some time, since
the native library (apriltags-source) will be compiled first.

Manual installation from source (for development)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
   pip install -e .[dev]

   # run tests
   tox

Usage
-----

Some examples of usage can be seen in the
``src/pupil_apriltags/bindings.py`` file.

The ``Detector`` class is a wrapper around the Apriltags functionality.
You can initialize it as following:

.. code:: python

   from pupil_apriltags import Detector

   at_detector = Detector(families='tag36h11',
                          nthreads=1,
                          quad_decimate=1.0,
                          quad_sigma=0.0,
                          refine_edges=1,
                          decode_sharpening=0.25,
                          debug=0)

The options are:

+---+---+----------------------------------------------------------------+
| * | * | **Explanation**                                                |
| * | * |                                                                |
| O | D |                                                                |
| p | e |                                                                |
| t | f |                                                                |
| i | a |                                                                |
| o | u |                                                                |
| n | l |                                                                |
| * | t |                                                                |
| * | * |                                                                |
|   | * |                                                                |
+===+===+================================================================+
| f | ‘ | Tag families, separated with a space                           |
| a | t |                                                                |
| m | a |                                                                |
| i | g |                                                                |
| l | 3 |                                                                |
| i | 6 |                                                                |
| e | h |                                                                |
| s | 1 |                                                                |
|   | 1 |                                                                |
|   | ’ |                                                                |
+---+---+----------------------------------------------------------------+
| n | 1 | Number of threads                                              |
| t |   |                                                                |
| h |   |                                                                |
| r |   |                                                                |
| e |   |                                                                |
| a |   |                                                                |
| d |   |                                                                |
| s |   |                                                                |
+---+---+----------------------------------------------------------------+
| q | 2 | Detection of quads can be done on a lower-resolution image,    |
| u | . | improving speed at a cost of pose accuracy and a slight        |
| a | 0 | decrease in detection rate. Decoding the binary payload is     |
| d |   | still done at full resolution. Set this to 1.0 to use the full |
| _ |   | resolution.                                                    |
| d |   |                                                                |
| e |   |                                                                |
| c |   |                                                                |
| i |   |                                                                |
| m |   |                                                                |
| a |   |                                                                |
| t |   |                                                                |
| e |   |                                                                |
+---+---+----------------------------------------------------------------+
| q | 0 | What Gaussian blur should be applied to the segmented image.   |
| u | . | Parameter is the standard deviation in pixels. Very noisy      |
| a | 0 | images benefit from non-zero values (e.g. 0.8)                 |
| d |   |                                                                |
| _ |   |                                                                |
| s |   |                                                                |
| i |   |                                                                |
| g |   |                                                                |
| m |   |                                                                |
| a |   |                                                                |
+---+---+----------------------------------------------------------------+
| r | 1 | When non-zero, the edges of the each quad are adjusted to      |
| e |   | “snap to” strong gradients nearby. This is useful when         |
| f |   | decimation is employed, as it can increase the quality of the  |
| i |   | initial quad estimate substantially. Generally recommended to  |
| n |   | be on (1). Very computationally inexpensive. Option is ignored |
| e |   | if quad_decimate = 1                                           |
| _ |   |                                                                |
| e |   |                                                                |
| d |   |                                                                |
| g |   |                                                                |
| e |   |                                                                |
| s |   |                                                                |
+---+---+----------------------------------------------------------------+
| d | 0 | How much sharpening should be done to decoded images? This can |
| e | . | help decode small tags but may or may not help in odd lighting |
| c | 2 | conditions or low light conditions                             |
| o | 5 |                                                                |
| d |   |                                                                |
| e |   |                                                                |
| _ |   |                                                                |
| s |   |                                                                |
| h |   |                                                                |
| a |   |                                                                |
| r |   |                                                                |
| p |   |                                                                |
| e |   |                                                                |
| n |   |                                                                |
| i |   |                                                                |
| n |   |                                                                |
| g |   |                                                                |
+---+---+----------------------------------------------------------------+
| d | 0 | If 1, will save debug images. Runs very slow                   |
| e |   |                                                                |
| b |   |                                                                |
| u |   |                                                                |
| g |   |                                                                |
+---+---+----------------------------------------------------------------+

Detection of tags in images is done by running the ``detect`` method of
the detector:

.. code:: python

   tags = at_detector.detect(img, estimate_tag_pose=False, camera_params=None, tag_size=None)

If you also want to extract the tag pose, ``estimate_tag_pose`` should
be set to ``True`` and ``camera_params`` (``[fx, fy, cx, cy]``) and
``tag_size`` (in meters) should be supplied. The ``detect`` method
returns a list of ``Detection`` objects each having the following
attributes (note that the ones with an asterisks are computed only if
``estimate_tag_pose=True``):

+---+--------------------------------------------------------------------+
| * | **Explanation**                                                    |
| * |                                                                    |
| A |                                                                    |
| t |                                                                    |
| t |                                                                    |
| r |                                                                    |
| i |                                                                    |
| b |                                                                    |
| u |                                                                    |
| t |                                                                    |
| e |                                                                    |
| * |                                                                    |
| * |                                                                    |
+===+====================================================================+
| t | The family of the tag.                                             |
| a |                                                                    |
| g |                                                                    |
| _ |                                                                    |
| f |                                                                    |
| a |                                                                    |
| m |                                                                    |
| i |                                                                    |
| l |                                                                    |
| y |                                                                    |
+---+--------------------------------------------------------------------+
| t | The decoded ID of the tag.                                         |
| a |                                                                    |
| g |                                                                    |
| _ |                                                                    |
| i |                                                                    |
| d |                                                                    |
+---+--------------------------------------------------------------------+
| h | How many error bits were corrected? Note: accepting large numbers  |
| a | of corrected errors leads to greatly increased false positive      |
| m | rates. NOTE: As of this implementation, the detector cannot detect |
| m | tags with a Hamming distance greater than 2.                       |
| i |                                                                    |
| n |                                                                    |
| g |                                                                    |
+---+--------------------------------------------------------------------+
| d | A measure of the quality of the binary decoding process: the       |
| e | average difference between the intensity of a data bit versus the  |
| c | decision threshold. Higher numbers roughly indicate better         |
| i | decodes. This is a reasonable measure of detection accuracy only   |
| s | for very small tags– not effective for larger tags (where we could |
| i | have sampled anywhere within a bit cell and still gotten a good    |
| o | detection.)                                                        |
| n |                                                                    |
| _ |                                                                    |
| m |                                                                    |
| a |                                                                    |
| r |                                                                    |
| g |                                                                    |
| i |                                                                    |
| n |                                                                    |
+---+--------------------------------------------------------------------+
| h | The 3x3 homography matrix describing the projection from an        |
| o | “ideal” tag (with corners at (-1,1), (1,1), (1,-1), and (-1, -1))  |
| m | to pixels in the image.                                            |
| o |                                                                    |
| g |                                                                    |
| r |                                                                    |
| a |                                                                    |
| p |                                                                    |
| h |                                                                    |
| y |                                                                    |
+---+--------------------------------------------------------------------+
| c | The center of the detection in image pixel coordinates.            |
| e |                                                                    |
| n |                                                                    |
| t |                                                                    |
| e |                                                                    |
| r |                                                                    |
+---+--------------------------------------------------------------------+
| c | The corners of the tag in image pixel coordinates. These always    |
| o | wrap counter-clock wise around the tag.                            |
| r |                                                                    |
| n |                                                                    |
| e |                                                                    |
| r |                                                                    |
| s |                                                                    |
+---+--------------------------------------------------------------------+
| p | Rotation matrix of the pose estimate.                              |
| o |                                                                    |
| s |                                                                    |
| e |                                                                    |
| _ |                                                                    |
| R |                                                                    |
| \ |                                                                    |
| * |                                                                    |
+---+--------------------------------------------------------------------+
| p | Translation of the pose estimate.                                  |
| o |                                                                    |
| s |                                                                    |
| e |                                                                    |
| _ |                                                                    |
| t |                                                                    |
| \ |                                                                    |
| * |                                                                    |
+---+--------------------------------------------------------------------+
| p | Object-space error of the estimation.                              |
| o |                                                                    |
| s |                                                                    |
| e |                                                                    |
| _ |                                                                    |
| e |                                                                    |
| r |                                                                    |
| r |                                                                    |
| \ |                                                                    |
| * |                                                                    |
+---+--------------------------------------------------------------------+
