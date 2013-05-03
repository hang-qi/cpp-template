cmake_minimum_required (VERSION 2.6)

#------------------------------
# Project
#------------------------------
project (MY_PROJECT)
set(TARGET my_project)

set(PROJECT_VERSION "0.5")
set(ARCHIVE_NAME ${CMAKE_PROJECT_NAME}-${PROJECT_VERSION})

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# External libraries
include_directories(include)
link_directories(${PROJECT_SOURCE_DIR}/lib)


#------------------------------
# Compiler flags
#------------------------------
# Set default built type to DEBUG.
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE DEBUG CACHE STRING "Build types: DEBUG, RELEASE" FORCE)
endif(NOT CMAKE_BUILD_TYPE)

set(CMAKE_CXX_FLAGS                "-Wall")
set(CMAKE_CXX_FLAGS_DEBUG          "-O0 -g")
set(CMAKE_CXX_FLAGS_MINSIZEREL     "-Os -DNDEBUG")
set(CMAKE_CXX_FLAGS_RELEASE        "-O4 -DNDEBUG")
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g")

add_definitions("-std=c++11 -Wall -Wextra")
#-Wall -Wextra -Wshadow -Wpointer-arith -Wcast-qual

# Compiler-specific C++11 activation.
if ("${CMAKE_CXX_COMPILER_ID}" MATCHES "GNU")
    execute_process(
        COMMAND ${CMAKE_CXX_COMPILER} -dumpversion OUTPUT_VARIABLE GCC_VERSION)
    if (NOT (GCC_VERSION VERSION_GREATER 4.6 OR GCC_VERSION VERSION_EQUAL 4.6))
        message(FATAL_ERROR "${PROJECT_NAME} requires g++ 4.6 or greater.")
    endif ()
elseif ("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
else ()
    message(FATAL_ERROR "Your C++ compiler may be obsoleted.")
endif ()


#------------------------------
# Sub Directories
#------------------------------
add_subdirectory (src/component)
add_subdirectory (src/main)


#------------------------------
# Static libraries
#------------------------------
#add_library(lib src)