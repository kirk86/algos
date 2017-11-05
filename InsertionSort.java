/*
 * InsertionSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything. So there.
 *
 */

/**
 * An insertion sort demonstration algorithm
 * InsertionSortAlgorithm.java
 *
 * @author Patrick Morin
 */
class InsertionSortAlgorithm extends SortAlgorithm {
  void sort (int a[]) throws Exception {
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
