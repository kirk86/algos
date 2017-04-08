#include <stdio.h>
#include <stdlib.h>

typedef struct treeNode
{
    int data;
    struct treeNode* left;
    struct treeNode* right;
} treeNode;

treeNode* find_min(treeNode* node)
{
    if(node == NULL)
    {
        /* There is no element in the tree */
        return NULL;
    }
    if (node->left)  /* Go to the left sub-tree to find teh min element */
    {
        return find_min(node->left);
    }
    else
    {
        return node;
    }
}

treeNode* find_max(treeNode* node)
{
    if(node == NULL)
    {
        /* There is no element in the tree */
        return NULL;
    }
    if(node->right)
    {
        find_max(node->right);
    }
    else
    {
        return node;
    }
}

treeNode* insert(treeNode* node, int data)
{
    if(node == NULL)
    {
        treeNode* temp;
        temp = (treeNode* )malloc(sizeof(treeNode));
        temp->data = data;
        temp->left = temp->right = NULL;
        return temp;
    }
    if(data > (node->data))
    {
        node->right = insert(node->right, data);
    }
    else if(data < (node->data))
    {
        node->left = insert(node->left, data);
    }
    /* Else there is nothing to do as the data is already in the tree */
    return node;
}

int main(int argc, char** argv)
{
    treeNode *node, *result;
    node->data = 34;
    result = insert(node, 23);
    return 0;
}
