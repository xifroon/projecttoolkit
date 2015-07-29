cmake_minimum_required (VERSION 2.6)
project (ProjectToolkit)
set (PACKAGE_NAME "Project Toolkit")
set (PACKAGE_LONGNAME "X0 Project Toolkit")
set (PACKAGE_SHORTNAME "projecttoolkit")

# Version
set (ProjectToolkit_VERSION_MAJOR 0)
set (ProjectToolkit_VERSION_MINOR 1)
set (ProjectToolkit_VERSION_PATCH 0)
set (ProjectToolkit_VERSION_TWEAK "alpha.9")
set (ProjectToolkit_VERSION_CORE
     "${ProjectToolkit_VERSION_MAJOR}.${ProjectToolkit_VERSION_MINOR}.${ProjectToolkit_VERSION_PATCH}")
set (ProjectToolkit_VERSION
"${ProjectToolkit_VERSION_CORE}-${ProjectToolkit_VERSION_TWEAK}")

add_subdirectory (data)
add_subdirectory (python)
add_subdirectory (src)

# uninstall target
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/CMakeModule/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/CMakeModule/cmake_uninstall.cmake"
    IMMEDIATE @ONLY)

add_custom_target(uninstall
                  COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/CMakeModule/cmake_uninstall.cmake)
