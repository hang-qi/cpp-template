#include <iostream>
#include <version.h>
#include <algorithm>
#include <vector>

#include "component/comp.h"

int main(int argc, char* argv[])
{
    std::cout << "Hello World" << std::endl;
    std::cout << "Version: " << VERSION_STR_FULL << std::endl;
    comp::ComponentPrint(15);

    std::vector<int> v{1, 2, 3};
    std::for_each(v.begin(), v.end(), [&] (int el) {
          std::cout << el << " ";
    });
    std::cout << std::endl;
    return 0;
}