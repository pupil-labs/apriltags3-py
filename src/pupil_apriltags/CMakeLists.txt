project(apriltag-python-bindings)
cmake_minimum_required(VERSION 3.3)

add_subdirectory(../../apriltags-source skbuild-lib)

# set(CYTHON_ANNOTATE TRUE)
# add_cython_target(uvc_bindings C PY3) # CXX does not generate a corretc module

add_library(pyapriltag MODULE)
python_extension_module(pyapriltag)
target_link_libraries(pyapriltag apriltag)

# install here
install(TARGETS apriltags LIBRARY DESTINATION ".")