/*
 * MergeSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything. So there.
 *
 */

/**
 * A MergeSort demonstration algorithm
 * MergeSortAlgorithm.java
 *
 * @author Patrick Morin
 */

class MergeSortAlgorithm extends SortAlgorithm {

  void sort(int a[], int lo, int hi) throws Exception {
    // Base case
    if(lo == hi) {
      return;
    }

    // Recurse
    int length = hi-lo+1;
    int pivot = (lo+hi) / 2;
    sort(a, lo, pivot);
    sort(a, pivot+1, hi);

    // Merge
    int working[] = new int[length];
    for(int i = 0; i < length; i++)
      working[i] = a[lo+i];
    int m1 = 0;
    int m2 = pivot-lo+1;
    for(int i = 0; i < length; i++) {
      if(m2 <= hi-lo) {
    if(m1 <= pivot-lo) {
      if(working[m1] > working[m2]) {
        a[i+lo] = working[m2++];
      }
      else {
        a[i+lo] = working[m1++];
      }
    }
    else {
      a[i+lo] = working[m2++];
    }
      }
      else {
    a[i+lo] = working[m1++];
      }
      pause();
    }
  }

  void sort(int a[]) throws Exception {
    sort(a, 0, a.length-1);
  }
}






