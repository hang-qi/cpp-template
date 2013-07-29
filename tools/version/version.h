// Version.h
// This header file is automatically generated. Do not change manually.

#ifndef _VERSION_H_
#define _VERSION_H_

#define PROJECT_NAME    "Project Name"
#define COMPANY_NAME    "Company Name"

#define VERSION_NUM_MAJOR 1
#define VERSION_NUM_MINOR 0
#define VERSION_NUM_BUILD 0

#define VERSION_STR_FULL    "1.0.0"

class Version
{
public:
    static int GetMajor() {return VERSION_NUM_MAJOR;}
    static int GetMinor() {return VERSION_NUM_MINOR;}
    static int GetBuild() {return VERSION_NUM_BUILD;}

    static const char* GetVersion()
    {
        return VERSION_STR_FULL;
    }

    static bool IsAtLeast(int major, int minor, int build)
    {
        return (VERSION_NUM_MAJOR >= major)
            && (VERSION_NUM_MINOR >= minor)
            && (VERSION_NUM_BUILD >= build);
    }
};

#endif
