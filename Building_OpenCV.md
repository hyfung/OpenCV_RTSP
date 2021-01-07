# Building Opencv

This is a guide on how to (cross) compile OpenCV on x86_64 for arm-gnueabihf and aarch64

## Installing Dependencies
```bash
sudo apt update && sudo apt install -y cmake g++ wget unzip -y
```

## Building for x86_64

```bash
cd /dev/shm

git clone https://github.com/opencv/opencv.git

mkdir -p build && cd build

cmake  ../opencv

make -j$(nproc)

# sudo make install
```

## Building for gnueabihf (E.g. Raspberry Pi 2b)

```bash
# Installing dependencies
sudo apt install cpp-9-arm-linux-gnueabihf \
gcc-9-arm-linux-gnueabihf g++-9-arm-linux-gnueabihf -y
```

```bash
cd ~/opencv/platforms/linux
mkdir -p build && cd build

cmake -DCMAKE_TOOLCHAIN_FILE=../arm-gnueabi.toolchain.cmake \
-DGNU_MACHINE=arm-linux \
-DFLOAT_ABI_SUFFIX=hf \
-DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-9 \
-DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-9 \
-DCMAKE_LINKER=arm-linux-gnueabihf-ld \
-DCMAKE_AR=arm-linux-gnueabihf-gcc-ar-9 \
../../..
```

Open `opencv/platforms/linux/build/CMakeFiles/3.19.2/CMakeCCompiler.cmake`

Locate `set(CMAKE_AR "/dev/shm/opencv/platforms/linux/build/arm-linux-gnueabihf-gcc-ar-9")`

Change to `set(CMAKE_AR "/usr/bin/arm-linux-gnueabihf-gcc-ar-9")`

```bash
make
```

## Building for aarch64 (Raspberry Pi 3B or later, Jetson Nano)

```bash
# Installing dependencies
sudo apt install cpp-9-aarch64-linux-gnu \
gcc-9-aarch64-linux-gnu g++-9-aarch64-linux-gnu -y
```

```bash
# Taken from https://docs.opencv.org/master/d0/d76/tutorial_arm_crosscompile_with_cmake.html , might not work
cd ~/opencv/platforms/linux
mkdir -p build_hardfp
cd build_hardfp
cmake -DCMAKE_TOOLCHAIN_FILE=../aarch64-gnu.toolchain.cmake ../../..
make
```

## Installing

By default OpenCV will be installed to the /usr/local directory, all files will be copied to following locations:
```bash
/usr/local/bin              executable files
/usr/local/lib              libraries (.so)
/usr/local/cmake/opencv4    cmake package
/usr/local/include/opencv4  headers
/usr/local/share/opencv4    other files (e.g. trained cascades in XML format)
```
Since /usr/local is owned by the root user, the installation should be performed with elevated privileges (sudo):
`sudo make install`

Reference:
https://docs.opencv.org/master/d0/d76/tutorial_arm_crosscompile_with_cmake.html
