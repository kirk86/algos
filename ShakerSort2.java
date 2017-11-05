/*
 * ShakerSortTwoAlgorithm.java
 * Disclaimer: I am not responsible for anything. Ever. So there.
 */

/**
 * A shaker sort 2 demonstration algorithm. O(nlg^2n)
 * @author Patrick Morin
 */
class ShakerSortTwoAlgorithm extends SortAlgorithm {
  void sort(int a[]) throws Exception {
    for(int n = a.length/2; n > 0; n /= 2) {
      for(int m = n; m > 0; m /= 2) {
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
 
