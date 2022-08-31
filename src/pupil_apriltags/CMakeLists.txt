project(apriltag-python-bindings)
cmake_minimum_required(VERSION 3.3)

set(CMAKE_JOB_POOL_COMPILE:STRING compile)
set(CMAKE_JOB_POOL_LINK:STRING link)
set(CMAKE_JOB_POOLS:STRING compile=5;link=2)

add_subdirectory(../../apriltags-source skbuild-lib)

if(APPLE)
    set(CMAKE_INSTALL_RPATH @loader_path/${CMAKE_INSTALL_LIBDIR})
elseif(UNIX)
    set(CMAKE_INSTALL_RPATH $ORIGIN/${CMAKE_INSTALL_LIBDIR})
endif()

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_cython_target(link_helper C PY3) # CXX does not generate a corretc module
add_library(link_helper MODULE ${link_helper})
python_extension_module(link_helper)
target_link_libraries(link_helper apriltag)

# install here
install(TARGETS link_helper LIBRARY DESTINATION ".")
