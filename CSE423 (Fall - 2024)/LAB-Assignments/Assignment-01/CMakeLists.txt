cmake_minimum_required(VERSION 3.10)
project(OpenGL-Project)

set(CMAKE_CXX_STANDARD 17)

add_executable(OpenGL-Project src/Task-02.cpp)
# file(GLOB SOURCES "src/*.cpp")
# add_executable(OpenGL-Project ${SOURCES})

set(OpenGL_GL_PREFERENCE "GLVND")

# Find and link OpenGL libraries
find_package(OpenGL REQUIRED)
find_package(GLUT REQUIRED)
find_package(GLEW REQUIRED)
find_package(glfw3 REQUIRED)

# Link the libraries to the executable
target_link_libraries(OpenGL-Project OpenGL::GL GLUT::GLUT GLEW::GLEW glfw)
