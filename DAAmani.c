#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* parent;
};

struct Node* makeSet(int x) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = x;
    node->parent = node; // root node is its own parent
    return node;
}

struct Node* findSet(struct Node* node) {
    if (node != node->parent) {
        node->parent = findSet(node->parent); // path compression
    }
    return node->parent;
}

void unionSet(struct Node* x, struct Node* y) {
    struct Node* rx = findSet(x);
    struct Node* ry = findSet(y);
    if (rx != ry) {
        ry->parent = rx;
    }
}

int main() {
    int n;
    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    // create an array of nodes
    struct Node* nodes[n];
    for (int i = 0; i < n; i++) {
        int data;
        printf("Enter data for node %d: ", i);
        scanf("%d", &data);
        nodes[i] = makeSet(data);
    }

    // perform union operations
    int m;
    printf("Enter the number of union operations: ");
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        int x, y;
        printf("Enter two nodes to union: ");
        scanf("%d %d", &x, &y);
        unionSet(nodes[x], nodes[y]);
    }

    // print the sets
    for (int i = 0; i < n; i++) {
        printf("%d belongs to set %d\n", nodes[i]->data, findSet(nodes[i])->data);
    }

    return 0;
}
