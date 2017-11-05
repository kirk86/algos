/*
 * JSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything. So there.
 *
 */

/**
 * A JSort Demonstration algorithm.  The JSort algorithm is due to
 * Jason Morrison <http://www.scs.carleton.ca/~morrison>
 *     
 * JSortAlgorithm.java
 *
 * @author Patrick Morin
 */
class JSortAlgorithm extends SortAlgorithm {

    /**
     * Make the sub-array starting at position i into a a heap,
     * assuming that it's left and right children are already 
     * heaps.
     */
    void reheap (int a[], int length, int i) throws Exception {
    boolean done = false;
    int T = a[i];
    int parent = i;
    int child = 2*(i+1)-1;
    while ((child < length) && (!done)) {
        compex(parent, child);
        pause();
        if (child < length - 1) {
        if (a[child] >= a[child + 1]) {
            child += 1;
        }
        }
        if (T < a[child]) {
        done = true;
        }
        else {
        a[parent] = a[child];
        parent = child;
        child = 2*(parent+1)-1;
        }
    }
    a[parent] = T;
    }

    /**
     * Make the sub-array starting at position length-i into a a heap,
     * assuming that it's left and right children are already 
     * heaps.
     */
    void invreheap (int a[], int length, int i) throws Exception {
    boolean done = false;
    int T = a[length - 1 - i];
    int parent = i;
    int child = 2*(i+1)-1;
    while ((child < length) && (!done)) {
        compex(length - 1 - parent, i-child);
        pause();
        if (child < length - 1) {
        if (a[length - 1 - child] <= a[length - 1 - (child + 1)]) {
            child += 1;
        }
        }
        if (T > a[length - 1 - child]) {
        done = true;
        }
        else {
        a[length - 1 - parent] = a[length - 1 - child];
        parent = child;
        child = 2*(parent+1)-1;
        }
    }
    a[length - 1 - parent] = T;
    }

    /**
     * Sort the input using the heap sort algorithm.
     */
    void sort(int a[]) throws Exception {

    // Heapify bottom up
    for (int i = a.length-1; i >= 0; i--)
        reheap (a, a.length, i);

    // Heapify top down
    for (int i = a.length-1; i >= 0; i--)
        invreheap (a, a.length, i);

    // Do an insertion sort on the almost sorted array
    for (int j = 1; j < a.length; j++) {
        int T = a[j];
        int i = j - 1;
        while (i >= 0 && a[i] > T) {
        a[i+1] = a[i];
        i -= 1;
        compex(j,i);
        pause();
        }
        a[i+1] = T;
    }
    pause();
    }
}




