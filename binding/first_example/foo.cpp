// 
// Product  : Binding C -> Python
// Author   : Connor McCann
// Date     : 30 Jun 2017
// Source   : https://stackoverflow.com/questions/145270/calling-c-c-from-python
//
#include <iostream>


class Foo {
    public:
        void bar(void) {
            std::cout << "Hello World!" << std::endl;
        }    
};

extern "C" {
    Foo* Foo_new(void) {
        return new Foo();
    }

    void Foo_bar(Foo* foo) {
        foo->bar();
    }
}
