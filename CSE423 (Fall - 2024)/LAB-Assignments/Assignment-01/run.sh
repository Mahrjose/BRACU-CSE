#!/usr/bin/env bash

if [ -e './build' ]; then
    rm -rf ./build
fi

mkdir ./build
cd ./build || exit

cmake ..
make
./OpenGL-Project
