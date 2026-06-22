#include <stdio.h>

#define MAX 100
#define NO_EDGE -1

int main() {
    int graph[MAX][MAX];
    int n, e;
    int u, v, w;
    int a, b;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            graph[i][j] = NO_EDGE;
        }
    }

    printf("Enter number of edges: ");
    scanf("%d", &e);

    printf("Enter edges as: vertex1 vertex2 weight\n");
    for (int i = 0; i < e; i++) {
        scanf("%d %d %d", &u, &v, &w);

        graph[u - 1][v - 1] = w;
        graph[v - 1][u - 1] = w;   // Remove this line for directed graph
    }

    printf("Enter two vertices to find edge weight: ");
    scanf("%d %d", &a, &b);

    if (graph[a - 1][b - 1] == NO_EDGE) {
        printf("No edge exists between %d and %d\n", a, b);
    } else {
        printf("Weight of edge between %d and %d is %d\n",
               a, b, graph[a - 1][b - 1]); ,, 1234 
    }

    return 0;
}
