#include <iostream>
#include "string_fifo.h"

using namespace std;

int main() {
    fifo_t myFifo;

    myFifo.init_fifo();
    myFifo.put_fifo("hello");
    string rez(myFifo.get_fifo());
    //cout << rez << endl;
    return 0;
}