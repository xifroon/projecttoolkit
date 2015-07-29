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

# Cross platform sub-install folder
if (WIN32)
    set (PACKAGE_DIR "${CMAKE_INSTALL_PREFIX}/${PACKAGE_NAME}")
    set (PACKAGE_DATA_DIR "${PACKAGE_DIR}/data")
    set (PACKAGE_DOC_DIR "${PACKAGE_DIR}/doc")
Elseif (UNIX)
    set (DATA_DIR "${CMAKE_INSTALL_PREFIX}/share")
    set (PACKAGE_DATA_DIR "${DATA_DIR}/${PACKAGE_SHORTNAME}")
    set (PACKAGE_DOC_DIR "${DATA_DIR}/doc/${PACKAGE_SHORTNAME}")
    set (PACKAGE_ICON_16PX_DIR "${DATA_DIR}/icons/hicolor/16x16")
    set (PACKAGE_ICON_24PX_DIR "${DATA_DIR}/icons/hicolor/24x24")
    set (PACKAGE_ICON_32PX_DIR "${DATA_DIR}/icons/hicolor/32x32")
    set (PACKAGE_ICON_64PX_DIR "${DATA_DIR}/icons/hicolor/64x64")
    set (PACKAGE_ICON_128PX_DIR "${DATA_DIR}/icons/hicolor/128x128")
    set (PACKAGE_ICON_256PX_DIR "${DATA_DIR}/icons/hicolor/256x256")
    set (PACKAGE_THEME_DIR "${DATA_DIR}/themes")
endif()

add_subdirectory (data)
add_subdirectory (python)
add_subdirectory (src)

# uninstall target
configure_file (
    "${CMAKE_CURRENT_SOURCE_DIR}/CMakeModule/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/CMakeModule/cmake_uninstall.cmake"
    IMMEDIATE @ONLY)

add_custom_target (uninstall
                   COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/CMakeModule/cmake_uninstall.cmake)
