/*
 * ShakerSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything ever. So there.
 *    
 */

/**
 * A shaker sort demonstration algorithm
 * @author Patrick Morin
 */
class ShakerSortAlgorithm extends SortAlgorithm {
  void sort(int a[]) throws Exception {
    for(int m = a.length/2; m > 0; m /= 2) {
      for(int i = 0; i < a.length - m; i++) {
    if(a[i] > a[i+m]) {
      int T = a[i];
      a[i] = a[i+m];
      a[i+m] = T;
    }
    compex(i, i+m);
    pause();
      }
    }
    boolean change;
    do {
      change = false;
      for (int j = 0; j < a.length-1; j++) {
    if (stopRequested) {
      return;
    }
    if (a[j] > a[j+1]) {
      int T = a[j];
      a[j] = a[j+1];
      a[j+1] = T;
      change = true;
    }
    compex(j, j+1);
    pause();
      } 
    } while(change);
  }
}

