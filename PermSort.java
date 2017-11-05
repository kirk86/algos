/*
 * PermSortAlgorithm.java
 * Patrick Morin takes no responsibility for anything. So there.
 *
 */

/**
 * A PermSort Demonstration algorithm.  The PermSort algorithm is due
 * to Patrick Morin <http:www.scs.carleton.ca/~morin>.  The algorithm
 * works by trying every permutation until it finds one that's
 * sorted.  That's right, there are n! permutations and it takes O(n)
 * time to test each one, yielding an O(nn!) algorithm.  No hate mail
 * please.
 *     
 * @author Patrick Morin 
 */
class PermSortAlgorithm extends SortAlgorithm {


    /**
     * Check if the input is sorted.  Do it in a weird way so it looks
     * good for the sort demo.
     */
    boolean issorted(int a[], int i) throws Exception {
    for (int j = a.length-1; j > 0; j--) {
        compex(j, j-1);
        pause();
        if(a[j] < a[j-1]) {
        return false;
        }
    }
    return true;
    }

    /**
     * Privately sort the array using the PermSort algorithm.
     */
    boolean sort(int a[], int i) throws Exception {
    int j;

    // Check if array is already sorted
    if (issorted(a, i)) {
        return true;
    }

    // Array wasn't sorted so start trying permutations until we
    // get the right one.
    for(j = i+1; j < a.length; j++) {
        compex(i, j);
        pause();
        int T = a[i];
        a[i] = a[j];
        a[j] = T;
        if(sort(a, i+1)) {
        return true;
        }
        T = a[i];
        a[i] = a[j];
        a[j] = T;
    }
    return false;
    }

    /**    
     * Sort the input using the  PermSort algorithm.
     */
    void sort(int a[]) throws Exception {
    sort(a, 0);
    }
}




