
# configure a header file to pass some of the CMake settings
# to the source code
configure_file ("${PROJECT_SOURCE_DIR}/src/project-new.py.in"
                "${PROJECT_BINARY_DIR}/src/project-new")

configure_file ("${PROJECT_SOURCE_DIR}/src/project.py.in"
                "${PROJECT_BINARY_DIR}/src/project")

install (FILES "${PROJECT_BINARY_DIR}/src/project" DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/src/project-new" DESTINATION bin)
