// 
//  Project : Fifo Queue for Strings 
//  Author  : Connor McCann 
//  Date    : 17 Jun 2017
//
#include <stdlib.h>
#include "string_fifo.h"


void init_fifo(fifo_t *F, int queueSize, bool allowedToGrow) {
    // Set the capacity of the string array
    F->autoScale = (allowedToGrow == true) ? true : false;
    F->capacity = (queueSize != 0) ? queueSize : MAXINFO;
    F->messages = (char**) malloc(sizeof(char*) * F->capacity);
    // Put both pointers at 0th position
    F->wptr = 0;
    F->rptr = 0;
    // Set the size to be zero 
    F->size = 0;

    return;
}

void put_fifo(fifo_t *F, char *msg) {
    if (((F->wptr + 1) % F->capacity) != F->rptr) {
        // Add the message
        F->messages[F->wptr] = (char*) malloc(sizeof(msg));
        F->messages[F->wptr] = msg;
        // Adjust the pointer
        F->wptr = (F->wptr + 1) % F->capacity; 
    }
    else if (F->autoScale) {
        // Expand the size of the array by 10 string pointers
        F->messages = (char**) realloc(F->messages, sizeof(char*) * (F->size + 10));
        F->capacity += 10;
        // Add the message
        F->messages[F->wptr] = (char*) malloc(sizeof(msg));
        F->messages[F->wptr] = msg;
        // Adjust the pointer
        F->wptr = (F->wptr + 1) % F->capacity; 
    }
    // Adjust the size
    F->size++;

    return;
}

char* get_fifo(fifo_t *F) {
    char *msg;
    if (F->rptr != F->wptr) {
        // Get the message from the queue
        msg = F->messages[F->rptr];
        // Reduce the size
        F->size--;
        // Adjust the read pointer
        F->rptr = (F->rptr + 1) % F->capacity;

        return msg;
    }
    else {
        return "None";
    }
}

unsigned fifo_size(fifo_t *F) {
    if (F->wptr >= F->rptr) {
        return F->wptr - F->rptr;
    }
    else {
        return F->capacity - (F->rptr - F->wptr);
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
