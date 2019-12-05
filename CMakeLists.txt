cmake_minimum_required(VERSION 3.5.0)

project(guitool_cython_extensions)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(guitool_ibeis)
