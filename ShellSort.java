/*
 * BubbleSortAlgorithm.java
 *
 */

/**
 * A Shell's sort demonstration algorithm
 * ShellSortAlgorithm.java
 *
 * @author Patrick Morin
 */
class ShellSortAlgorithm extends SortAlgorithm {
  void sort(int a[]) throws Exception {
    for (int incr = a.length / 2; incr > 0; incr /= 2) {
      for(int i = incr; i < a.length; i++) {
    int j = i - incr;
    while(j >= 0) {
      compex(j, j+incr);
      pause();
      if (a[j] > a[j+incr]) {
        int T = a[j];
        a[j] = a[j+incr];
        a[j+incr] = T;
        j -= incr;
      }
      else {
        j = -1;
      }
    }
    pause();
      }
    }
  }
}

