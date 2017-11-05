/*
 * SelectionSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything. So there.
 *        
 */

/**
 * A selection sort demonstration algorithm
 * InsertionSortAlgorithm.java
 *
 * @author Patrick Morin
 */
class SelectionSortAlgorithm extends SortAlgorithm {
  void sort(int a[]) throws Exception {
    for (int i = a.length-1; i > 0; i--) {
      int T = 0;
      for (int j = 1; j <= i; j++) {
    if(stopRequested) {
      return;
    }
    if(a[j] > a[T]) {
      T = j;
    }
    compex(j, T);
    pause(i);
      }
      int temp = a[i];
      a[i] = a[T];
      a[T] = temp;
    }
  }
}
