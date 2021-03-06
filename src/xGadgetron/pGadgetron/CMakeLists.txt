#========================================================================
# Author: Kris Thielemans
# Copyright 2016 - 2019 University College London
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#=========================================================================

if(BUILD_PYTHON)

  if(${CMAKE_VERSION} VERSION_GREATER_EQUAL "3.13") 
    # policy introduced in CMake 3.13
    cmake_policy(SET CMP0078 OLD)
  endif()
  FIND_PACKAGE(SWIG REQUIRED)
  INCLUDE("${SWIG_USE_FILE}")

  set(cGadgetron_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../cGadgetron/include")

  SET_SOURCE_FILES_PROPERTIES(pygadgetron.i PROPERTIES CPLUSPLUS ON)  
  SET_SOURCE_FILES_PROPERTIES(pygadgetron.i PROPERTIES SWIG_FLAGS "-I${cGadgetron_INCLUDE_DIR}")
  # find libraries and include files
  # TODO would be better to use target_include_directories

  FIND_PACKAGE(PythonLibs REQUIRED)
  # Tell CMake it needs to re-run SWIG when .h file changes
  set(SWIG_MODULE_pygadgetron_EXTRA_DEPS "${cGadgetron_INCLUDE_DIR}/sirf/Gadgetron/cgadgetron.h")
  SWIG_ADD_LIBRARY(pygadgetron LANGUAGE python TYPE MODULE SOURCES pygadgetron.i)
  TARGET_INCLUDE_DIRECTORIES(${SWIG_MODULE_pygadgetron_REAL_NAME} PUBLIC ${PYTHON_INCLUDE_PATH})
  SWIG_LINK_LIBRARIES(pygadgetron cgadgetron iutilities "${PYTHON_LIBRARIES}")

  INSTALL(TARGETS ${SWIG_MODULE_pygadgetron_REAL_NAME} DESTINATION "${PYTHON_DEST}/sirf")
  INSTALL(FILES "${CMAKE_CURRENT_BINARY_DIR}/pygadgetron.py" Gadgetron.py DESTINATION "${PYTHON_DEST}/sirf")
  INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/Gadgetron_params.py" DESTINATION "${PYTHON_DEST}/sirf")

ADD_SUBDIRECTORY(tests)
endif(BUILD_PYTHON)

