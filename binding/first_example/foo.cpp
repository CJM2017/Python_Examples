// 
// Product  : Binding C -> Python
// Author   : Connor McCann
// Date     : 30 Jun 2017
// Source   : https://stackoverflow.com/questions/145270/calling-c-c-from-python
//
#include <iostream>
#include <vector>


class Foo {
    private:
        int num = 10;

    public:
        void bar(void) {
            std::cout << "Hello World!" << std::endl;
        }  
        int disp_num(void) {
            return this->num;
        }  
};

extern "C" {
    Foo* Foo_new(void) {
        return new Foo();
    }

    void Foo_bar(Foo* foo) {
        foo->bar();
    }

    int Foo_num(Foo* foo) {
        std::cout << "fuck you" << std::endl;
        int my_data = foo->disp_num();
        std::cout << "here" << std::endl;
        return my_data;
    }
}
