// 
//  Project : Fifo Queue for Strings C->Python
//  Author  : Connor McCann 
//  Date    : 17 Jun 2017
//
#ifndef STRING_FIFO_H
#define STRING_FIFO_H

#include <string>
#include <vector>

class fifo_t {
    private:
        std::vector<std::string> messages;
        int wptr;
        int rptr;
        int capacity = 10;

    public:
        void init_fifo(void); 
        void put_fifo(std::string msg); 
        std::string get_fifo(void); 
        unsigned fifo_size(void); 
};

// C interface
extern "C" {
    fifo_t* new_fifo(void); 
    void put(fifo_t* F, std::string msg);
}

#endif