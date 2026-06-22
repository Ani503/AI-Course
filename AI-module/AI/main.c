#include <stdio.h>
#include <stdlib.h>

/* ---------- Structure for a node in adjacency list ---------- */
struct Node {
    int vertex;
    struct Node* next;
};

/* ---------- Structure for the graph ---------- */
struct Graph {
    int numVertices;
    int isDirected;
    struct Node** adjList;
};

/* ---------- Create a new node ---------- */
struct Node* createNode(int v) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

/* ---------- Create a new graph ---------- */
struct Graph* createGraph(int vertices, int directed) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;
    graph->isDirected = directed;
    
    /* Create array of adjacency lists */
    graph->adjList = (struct Node**)malloc(vertices * sizeof(struct Node*));
    
    /* Initialize each adjacency list to NULL */
    for (int i = 0; i < vertices; i++) {
        graph->adjList[i] = NULL;
    }
    
    return graph;
}

/* ---------- Add an edge to the graph ---------- */
void addEdge(struct Graph* graph, int u, int v) {
    /* u and v are 0-based, adjust if using 1-based input */
    
    /* Add edge from u to v */
    struct Node* newNode = createNode(v);
    newNode->next = graph->adjList[u];
    graph->adjList[u] = newNode;
    
    /* If undirected, add edge from v to u */
    if (!graph->isDirected) {
        newNode = createNode(u);
        newNode->next = graph->adjList[v];
        graph->adjList[v] = newNode;
    }
}

/* ---------- Display the graph as adjacency list ---------- */
void displayGraph(struct Graph* graph) {
    for (int i = 0; i < graph->numVertices; i++) {
        printf("Vertex %d -> ", i);
        
        struct Node* temp = graph->adjList[i];
        if (temp == NULL) {
            printf("NULL");
        } else {
            while (temp != NULL) {
                printf("%d ", temp->vertex);
                if (temp->next != NULL) {
                    printf("-> ");
                }
                temp = temp->next;
            }
        }
        printf("\n");
    }
}

/* ---------- Free the graph memory ---------- */
void freeGraph(struct Graph* graph) {
    for (int i = 0; i < graph->numVertices; i++) {
        struct Node* temp = graph->adjList[i];
        while (temp != NULL) {
            struct Node* prev = temp;
            temp = temp->next;
            free(prev);
        }
    }
    free(graph->adjList);
    free(graph);
}

/* ---------- Main function ---------- */
int main() {
    int vertices, directed, edges, u, v;
    struct Graph* graph;
    
    /* Get number of vertices from user */
    printf("Enter number of vertices: ");
    scanf("%d", &vertices);
    
    /* Get graph type from user */
    printf("Enter 1 for DIRECTED graph or 0 for UNDIRECTED graph: ");
    scanf("%d", &directed);
    
    /* Create the graph */
    graph = createGraph(vertices, directed);
    
    /* Get number of edges from user */
    printf("Enter number of edges: ");
    scanf("%d", &edges);
    
    /* Get each edge from user */
    for (int i = 0; i < edges; i++) {
        printf("Enter edge %d (u v): ", i + 1);
        scanf("%d %d", &u, &v);
        addEdge(graph, u, v);
    }
    
    /* Display the graph */
    printf("\n===== ADJACENCY LIST =====\n");
    displayGraph(graph);
    
    /* Free memory */
    freeGraph(graph);
    
    return 0;
}
