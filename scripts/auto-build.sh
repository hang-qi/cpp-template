#!/bin/sh

# This is an auto-build script. It contains the following steps.
# (1) the latest code is pulled from the remote repository.
# (2) a version is to be build.
# (3) check if build succeed.

##-------------------------
## Configurations
##-------------------------
CHECK_TARGET="my_project"
BUILD_DIR="builds"
LOG_DIR="logs"
TODAY_DIR=$(date +%Y-%m-%d)
LOG_FILE="../$LOG_DIR/build_$(date +%Y-%m-%d_%H%M%S).log"


echo "Auto-build started."
date

##-------------------------
## Pull latest code.
##-------------------------
#cd ..
#git pull

##-------------------------
## Build nightly version.
##-------------------------
cd ..
if [ ! -d $BUILD_DIR ]; then
    mkdir $BUILD_DIR
fi 
cd $BUILD_DIR

if [ ! -d $LOG_DIR ]; then
    mkdir $LOG_DIR
fi 

if [ ! -d $TODAY_DIR ]; then
    echo "Creating directory..."
    mkdir $TODAY_DIR
fi
cd $TODAY_DIR

cmake -DCMAKE_BUILD_TYPE=Release ../..
make | tee $LOG_FILE

##-------------------------
## Check if succeed.
##-------------------------
echo "-----------"
if [ -f bin/$CHECK_TARGET ]
then
    echo "[BUILD SUCCESS] - $(date +%Y-%m-%d\ %H:%M:%S)" >> $LOG_FILE
else
    echo "[BUILD FAILED] - $(date +%Y-%m-%d\ %H:%M:%S)" >> $LOG_FILE
fi
date