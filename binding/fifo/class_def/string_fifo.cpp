// 
//  Project : Fifo Queue for Strings 
//  Author  : Connor McCann 
//  Date    : 17 Jun 2017
//
#include <iostream>
#include <string>
#include <vector>
#include "string_fifo.h"


void fifo_t::init_fifo(void) {    
    // Put both pointers at 0th position
    this->wptr = 0;
    this->rptr = 0;
    return;
}

void fifo_t::put_fifo(std::string msg) {
    std::cout << this->wptr << std::endl;

    if (((this->wptr + 1) % this->capacity) != this->rptr) {
        // Add the message
        this->messages.insert(this->messages.begin()+this->wptr, msg);
        // Adjust the pointer
        this->wptr = (this->wptr + 1) % this->capacity; 
    }
    return;
}

std::string fifo_t::get_fifo(void) {
    std::string msg;
    if (this->rptr != this->wptr) {
        // Get the message from the queue
        msg = this->messages[this->rptr];
        // Adjust the read pointer
        this->rptr = (this->rptr + 1) % this->capacity;
    }
    else {
        msg = "None";
    }
    return msg;
}

unsigned fifo_t::fifo_size(void) {
    if (this->wptr >= this->rptr) {
        return this->wptr - this->rptr;
    }
    else {
        return this->capacity - (this->rptr - this->wptr);
    }
}

// C interface
extern "C" {
    fifo_t* new_fifo(void) {
        fifo_t* F = new fifo_t();;
        F->init_fifo();
        return F;
    }

    void put(fifo_t* F, std::string msg) {
        F->put_fifo(msg);
    }
}
//
//          **_INIT_**
//     0    1    2    3    4 
//  ---------------------------
//  | W,R |    |    |    |    |
//  ---------------------------
//
//           **_PUT_**
//
//     0    1    2    3    4 
//  --------------------------
//  | R  | W  |    |    |    |
//  --------------------------
//
//           **_PUT_**
//
//     0    1    2    3    4 
//  --------------------------
//  | R  |    | W  |    |    |
//  --------------------------
//
//           **_PUT_**
//
//     0    1    2    3    4 
//  --------------------------
//  | R  |    |    | W  |    |
//  --------------------------
//
//           **_PUT_**
//
//     0    1    2    3    4 
//  --------------------------
//  | R  |    |    |    | W  |
//  --------------------------
//
// Cannot put beyond this
