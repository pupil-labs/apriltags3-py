#!/usr/bin/env python3
try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

extensions = ["sphinx.ext.autodoc", "jaraco.packaging.sphinx", "rst.linker"]

master_doc = "index"

link_files = {
    "../CHANGES.rst": dict(
        using=dict(GH="https://github.com"),
        replace=[
            dict(
                pattern=r"(Issue #|\B#)(?P<issue>\d+)",
                url="{package_url}/issues/{issue}",
            ),
            dict(
                pattern=r"(?m:^((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n)",
                with_scm="{text}\n{rev[timestamp]:%d %b %Y}\n",
            ),
            dict(
                pattern=r"PEP[- ](?P<pep_number>\d+)",
                url="https://peps.python.org/pep-{pep_number:0>4}/",
            ),
        ],
    )
}

# Be strict about any broken references:
nitpicky = True
nitpick_ignore = [
    ("py:class", "numpy.uint8"),
    ("py:class", "numpy._typing._generic_alias.ScalarType"),
]
# Include Python intersphinx mapping to prevent failures
# jaraco/skeleton#51
extensions += ["sphinx.ext.intersphinx"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}
html_theme = "furo"

project = "pupil-apriltags"
release = version(project)
version = ".".join(release.split(".")[:2])
html_title = f"{project} {release}"
