/* The stack: Last In-First Out (LIFO) */

#include <stdio.h>
#include <stdlib.h>

/* Stack has 3 properties. Capacity stands for the maximum number of
elements stack. Size stands for the current size of the stack and elements
is the array of elements */

typedef struct Stack
{
    int capacity;
    int size;
    int* elements;
} Stack;

/* create_stack fcn takes arguement the maximum number of elements the */
/* stack can hold and a stack according to it and returns a pointer to the stack */
Stack* create_stack(int maxElements)
{
    /* Create a Stack */
    Stack* S;
    S = (Stack *) malloc(sizeof(Stack));
    /* Initialize its properties */
    S->elements = (int *) malloc(sizeof(int) * maxElements);
    S->size = 0;
    S->capacity = maxElements;
    /* Return the pointer  */
    return S;
}

void pop(Stack* S)
{
    /* If stack size is zero then it is empty. So we cannot pop */
    if(S->size == 0)
    {
        printf("Stack is empty.\n");
        return;
    }
    /* Removing an element if equivalent to reducing its size by one */
    else
    {
        S->size--;
    }
    return;
}

int top(Stack* S)
{
    if (S->size == 0)
    {
        printf("Stack is empty.\n");
        exit(0);
    }
    /* Return the top most element */
    return S->elements[S->size - 1];
}

void push(Stack* S, int element)
{
    /* If the stack if full, we cannot push an element into it as there */
    /* is no space free */
    if (S->size == S->capacity)
    {
        printf("Stack is full.\n");
    }
    else
    {
        /* Push an element on top of it and increase its size by one */
        S->elements[S->size++] = element;
    }
    return;
}

int main(int argc, char* argv)
{
    Stack* S = create_stack(5);
    push(S, 4);
    push(S, 3);
    push(S, 8);
    push(S, -1);
    printf("Top element is %d\n", top(S));
    pop(S);
    printf("Top element is %d\n", top(S));
    pop(S);
    printf("Top element is %d\n", top(S));
    pop(S);
    printf("Top element is %d\n", top(S));
}
