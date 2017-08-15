Matrix Chain Multiplication - C Program Source Code

#include<string.h>
#include<stdio.h>
#include<limits.h>
int min(int a,int b)
{
        return a < b ? a:b;
}
/*d[i] is used to store the  dimension of the matrix ith matrix has dimension d[i-1] * d[i].
  So for no loss of generality we will put d[0] to be number of rows of the first matrix and we 
  start the index from 1
 */
int d[100100]; 

/* Cache is used to store the result of the function for specific values. If cache[i][j] = -1 then we
   do not know the result. If it is some number then that denotes the return value of multiply(i,j).
   We store it to avoid computing the same again
*/
int cache[1024][1024];
int multiply(int from,int to)
{
        if(from==to)return 0;
        if(cache[from][to]!=-1)
        {
                return cache[from][to];
        }
        int iter,result = INT_MAX;
        /*We put the paranthesis at every possible step and we take the one for which computation 
          is minimum */
        for(iter=from;iter<to;iter++)
        {
                /* Update the result every time */
                result= min(result,multiply(from,iter) + multiply(iter+1,to) + d[from-1]*d[iter]*d[to]);

        }
        return result;
}
/* Input Format: First integer must be the number of matrices. It has to be followed by 
   rows of first matrix, columns of first matrix, columns for second matrix, columns for third matrix,...
 */
int main()
{
        /*Initialising cache to -1 */
        memset(cache, -1,sizeof(cache));
        int number_of_matrices; 
        scanf("%d",&number_of_matrices);
        scanf("%d",&d[0]);
        int iter;
        for(iter=1;iter<=number_of_matrices;iter++)
        {
                scanf("%d",&d[iter]);
        }
        printf("%d\n",multiply(1,number_of_matrices));

}
