/*
 * HeapSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything. So there.
 *
 */

/**
 * A heap sort demonstration algorithm
 *
 * @author Patrick Morin
 */
class HeapSortAlgorithm extends SortAlgorithm {

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
        if (a[child] < a[child + 1]) {
          child += 1;
        }
      }
      if (T >= a[child]) {
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
   * Sort the input using the heap sort algorithm.
   */
  void sort(int a[]) throws Exception {

    // Make the input into a heap
    for (int i = a.length-1; i >= 0; i--)
      reheap (a, a.length, i);

    // Sort the heap
    for (int i = a.length-1; i > 0; i--) {
      int T = a[i];
      a[i] = a[0];
      a[0] = T;
      pause();
      reheap (a, i, 0);
    }
  }
}




