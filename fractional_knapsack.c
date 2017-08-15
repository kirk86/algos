#include<stdio.h>
/* Given the weight of items along with its value and also the maximum weight that we can to take,
   we have to maximise the value we can get. Unlike 0-1 knapsack, here we are allowed to take fractional 
   items. Hence this problem is called fractional knapsack */
typedef struct item
{
        int weight;
        int value;
}item;
int compare(const void *x, const void *y)
{
        item *i1 = (item *)x, *i2 = (item *)y;
        double ratio1 = (*i1).value*1.0 / (*i1).weight;
        double ratio2 = (*i2).value*1.0 / (*i2).weight;
        if(ratio1 < ratio2) return 1;
        else if(ratio1 > ratio2) return -1;
        else return 0;
}
int main()
{
        int items;
        scanf("%d",&items);
        item I[items];
        int iter;
        for(iter=0;iter<items;iter++)
        {
                scanf("%d%d",&I[iter].weight,&I[iter].value);
        }
        qsort(I,items,sizeof(item),compare);
        int maxWeight;
        scanf("%d",&maxWeight);
        double value = 0.0;
        int presentWeight = 0;
        for(iter=0;iter<items;iter++)
        {
                if(presentWeight + I[iter].weight <maxWeight)
                {
                        presentWeight = presentWeight + I[iter].weight ;
                        value += I[iter].value;
                }
                else
                {
                        int remaining  = maxWeight - presentWeight;
                        value += I[iter].value*remaining *1.0/I[iter].weight; 
                        break;
                }

        }       
        printf("Maximum value that can be attained is %.6lf\n",value);
}
