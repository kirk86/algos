/* Queue data structure: */
/* 2 basic implementations */
/* 1. Array-based implementation - Simple and efficient but the maximum */
/* number of queue is fixed */
/* 2. Singly linked list - based implementation - It's complicated but */
/* there is no limit on hte queue size, it's subjectve to the available memory */

#include <stdio.h>
#include <stdlib.h>

/* Queue has five properties. Capacity stands for the maximum number of */
/* elements Queue can have. */
/* Size stands for the current size of the Queue and elements is the array */
/* elements. Front, is the index of first element (the index at which we */
/*                                                 remove the element) */
/*     and rear is the index of back element (the index at which we insert */
/*                                            the element) */

typedef struct Queue
{
    int capacity;
    int size;
    int front;
    int rear;
    int* elements;
} Queue;

/* create_queue fcn takes arguement the maximum number of elements the Queue */
/* can hold and a Queue according to it, and returns a poiinter to the Queue. */
Queue* create_queue(int maxElements)
{
    /* Create a Queue */
    Queue* Q;
    Q = (Queue* )malloc(sizeof(Queue));
    /* Initialize its properties */
    Q->elements = (int* )malloc(sizeof(int) * maxElements);
    Q->size = 0;
    Q->capacity = maxElements;
    Q->front = 0;
    Q->rear = -1;
    /* Return the pointer */
    return Q;
}

void dequeue(Queue* Q)
{
    /* if Queue size is zero then it's empty. So we cannot pop */
    if (Q->size == 0)
    {
        printf("Queue is empty.\n");
        return;
    }
    /* Removing an element is equivalent ot incrementing index of front by one */
    else
    {
        Q->size--;
        Q->front++;
        /* As we fill elements in circular fashion */
        if (Q->front == Q->capacity)
        {
            Q->front = 0;
        }
    }
    return;
}

int front(Queue* Q)
{
    if (Q->size == 0)
    {
        printf("Queue is empty.\n");
        exit(Q);
    }
    /* Return the element which is at the front */
    return Q->elements[Q->front];
}

void enqueue(Queue* Q, int element)
{
    /* If the Queue is full, we cannot push an element into it as there is */
    /* no space free. */
    if (Q->size == Q->capacity)
    {
        printf("Queue is full.\n");
    }
    else
    {
        Q->size++;
        Q->rear = Q->rear + 1;
        /* As we fill the queue in circular fashion */
        if (Q->rear == Q->capacity)
        {
            Q->rear = 0;
        }
        /* Insert the element in its rear side */
        Q->elements[Q->rear] = element;
    }
    return;
}

int main(int argc, char* argv)
{
    Queue* Q = create_queue(5);
    enqueue(Q, 1);
    enqueue(Q, 2);
    enqueue(Q, 3);
    enqueue(Q, 4);
    printf("Front element is %d\n", front(Q));
    enqueue(Q, 5);
    dequeue(Q);
    enqueue(Q, 6);
    printf("Front element is %d\n", front(Q));
}
