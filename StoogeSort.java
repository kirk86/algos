/*
 * StoogeSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything ever. So there.
 *
 */

/**
 * A Stooge sort demonstration algorithm
 *
 * @author Patrick Morin
 */
class StoogeSortAlgorithm extends SortAlgorithm {
  void sort(int a[], int lo, int hi) throws Exception {
    if(a[lo] > a[hi]) {
      int T = a[lo];
      a[lo] = a[hi];
      a[hi] = T;
    }
    compex(lo,hi);
    pause();
    if(lo + 1 >= hi)
      return;
    int third = (hi - lo + 1) / 3;
    sort(a, lo, hi-third);
    sort(a, lo+third, hi);
    sort(a, lo, hi-third);
  }

  void sort(int a[]) throws Exception {
    sort(a, 0, a.length-1);
  }
}

