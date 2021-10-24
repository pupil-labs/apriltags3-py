import platform

from skbuild import setup

package_dir = "src"
package = "pupil_apriltags"

install_requires = ["numpy"]
if platform.system() == "Windows":
    install_requires.append("pupil-pthreads-win")

cmake_args = []
if platform.system() == "Windows":
    import pupil_pthreads_win as ptw

    cmake_args.append(f"-DPTHREADS_WIN_INCLUDE_DIR='{ptw.include_path}'")
    cmake_args.append(f"-DPTHREADS_WIN_IMPORT_LIB_PATH='{ptw.import_lib_path}'")
    # The Ninja cmake generator will use mingw (gcc) on windows travis instances, but we
    # need to use msvc for compatibility. The easiest solution I found was to just use
    # the vs cmake generator as it defaults to msvc.
    cmake_args.append("-GVisual Studio 16 2019 Win64")
    cmake_args.append("-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=True")

with open("README.md") as f:
    readme = f.read()

with open("CHANGELOG.md") as f:
    changelog = f.read()

long_description = f"{readme}\n\n{changelog}"

setup(
    author="Pupil Labs GmbH",
    author_email="pypi@pupil-labs.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    cmake_args=cmake_args,
    cmake_install_dir="src/pupil_apriltags",
    description="Python bindings for apriltags v3",
    extras_require={"dev": ["pytest", "tox", "bump2version"]},
    install_requires=install_requires,
    license="MIT license",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="apriltags",
    name="pupil-apriltags",
    packages=[package],
    package_dir={"": package_dir},
    test_suite="tests",
    url="https://github.com/pupil-labs/apriltags",
    version="1.0.4",
    zip_safe=False,
)
