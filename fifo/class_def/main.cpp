#include <iostream>
#include "string_fifo.h"

using namespace std;

int main() {
    fifo_t myFifo;

    myFifo.init_fifo();
    myFifo.put_fifo("hello");
    cout << myFifo.get_fifo() << endl;
    return 0;
}