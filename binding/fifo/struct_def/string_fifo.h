// 
//  Project : Fifo Queue for Strings 
//  Author  : Connor McCann 
//  Date    : 17 Jun 2017
//
#ifndef STRING_FIFO_H
#define STRING_FIFO_H

#define MAXINFO 100
#define none 0 

#define bool int
#define true 1
#define false 0

// First in first out priority queue
typedef struct {
    int capacity;
    int size;
    char **messages;
    unsigned wptr;
    unsigned rptr;
    bool autoScale;
} fifo_t;

// Queue methods
void init_fifo(fifo_t *F, int queueSize, bool allowedToGrow);
void put_fifo(fifo_t *F, char *msg);
char* get_fifo(fifo_t *F);
unsigned fifo_size(fifo_t *F);

#endif
