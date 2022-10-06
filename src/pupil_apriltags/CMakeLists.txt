project(apriltag-python-bindings)
cmake_minimum_required(VERSION 3.3)

set(CMAKE_JOB_POOL_COMPILE:STRING compile)
set(CMAKE_JOB_POOL_LINK:STRING link)
set(CMAKE_JOB_POOLS:STRING compile=5;link=2)

add_subdirectory(../../apriltags-source skbuild-lib)
