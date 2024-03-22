#include<stdio.h>
#include<stdlib.h>

struct node {
int data;
struct node *left;
struct node *right;
};

struct node *newNode(int data)
{
struct node *temp = (struct node *)malloc(sizeof(struct node));
temp->data = data;
temp->left = NULL;
temp->right = NULL;
return temp;
}
struct node *insert(struct node *node, int data) {
    if (node == NULL)
        return newNode(data);
    if (data < node->data)
        node->left = insert(node->left, data);
    else if (data > node->data)
        node->right = insert(node->right, data);
    return node;
}
void inorder(struct node *root)
{
if (root == NULL)
return;
inorder(root->left);
printf("%d\n", root->data);
inorder(root->right);
}

void kthLargest(struct node *root, int k)
{
static int count = 0;
if (root == NULL)
return;
kthLargest(root->right, k);
count++;
if (count == k) {
printf("%d\n", root->data);
return;
}
kthLargest(root->left, k);
}

int main()
{
struct node *root = NULL;
    root = insert(root, 15);
    insert(root, 20);
    insert(root, 10);
    insert(root, 8);
    insert(root, 12);
    insert(root, 16);
    insert(root, 25);
    //insert(root, 3);
    //insert(root, 5);
inorder(root);
//printf("\n");
int k;
printf("enter k value to get kthlargest node :");
scanf("%d",&k);
kthLargest(root, k);
return 0;
}