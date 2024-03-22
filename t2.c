#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node *newNode(int data) {
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
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
void inorder(struct node* root)
{
	if (root != NULL) {
		inorder(root->left);
		printf("%d \n", root->data);
		inorder(root->right);
	}
}

struct node *lca(struct node *root, int n1, int n2) {
    if (root == NULL)
        return NULL;
    if (root->data > n1 && root->data > n2)
        return lca(root->left, n1, n2);
    if (root->data < n1 && root->data < n2)
        return lca(root->right, n1, n2);
    return root;
}

int main() {
    struct node *root = NULL;
    root = insert(root, 6);
    insert(root, 2);
    insert(root, 8);
    insert(root, 0);
    insert(root, 4);
    insert(root, 7);
    insert(root, 9);
    insert(root, 3);
    insert(root, 5);
    inorder(root);
    int n1, n2;
    scanf("%d%d",&n1,&n2);
    struct node *t = lca(root, n1, n2);
    printf("LCA of %d and %d is %d \n", n1, n2, t->data);
    scanf("%d%d",&n1,&n2);
    t = lca(root, n1, n2);
    printf("LCA of %d and %d is %d \n", n1, n2, t->data);
   scanf("%d%d",&n1,&n2);
    t = lca(root, n1, n2);
    printf("LCA of %d and %d is %d \n", n1, n2, t->data);
    return 0;
}
