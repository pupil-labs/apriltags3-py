import platform

from setuptools import find_packages
from skbuild import setup

package_dir = "src"
package = "pupil_apriltags"

cmake_args = []
if platform.system() == "Windows":
    import pupil_pthreads_win as ptw

    cmake_args.append(f"-DPTHREADS_WIN_INCLUDE_DIR='{ptw.include_path}'")
    cmake_args.append(f"-DPTHREADS_WIN_IMPORT_LIB_PATH='{ptw.import_lib_path}'")
    # The Ninja cmake generator will use mingw (gcc) on windows travis instances, but we
    # need to use msvc for compatibility. The easiest solution I found was to just use
    # the vs cmake generator as it defaults to msvc.
    cmake_args.append("-GVisual Studio 17 2022")
    cmake_args.append("-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=True")

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=False,
    cmake_args=cmake_args,
    cmake_source_dir="src/pupil_apriltags",
    cmake_install_dir="src/pupil_apriltags",
)
