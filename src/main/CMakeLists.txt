# Executables.
add_executable (${TARGET} main.cpp) 

# Link the executable to depended libraries.
target_link_libraries (${TARGET} component) 