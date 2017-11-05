
class BozoSortAlgorithm extends SortAlgorithm {

    void sort(int a[]) throws Exception {
    
    boolean sorted = false;
    
    while (!sorted) {
        int index1 = Randomize(a.length);
        int index2 = Randomize(a.length);  
     
        int temp = a[index2];
        a[index2] = a[index1];
        a[index1] = temp;
        compex(index1, index2);
        pause();
        // Is a[] sorted?
        sorted = true;
        for (int i = 1; i < a.length; i++)  {
        if (a[i-1] > a[i]) {
            compex(i, i-1);
            pause();
            sorted = false;
            break;
        }  // end if
        }  // end for
    } // end while
    }  // end sort 
    
    private int Randomize( int range )  {
    
    double  rawResult;
  
    rawResult = Math.random();
    return (int) (rawResult * range);
    }
  
}  // end BozoSortAlgorithm
