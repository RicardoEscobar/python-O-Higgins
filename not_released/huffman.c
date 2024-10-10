/*Programa en C que implementa el algoritmo de codificación de Huffman.
Version de C usasda: C99
El objetivo es implementar un programa en C que lea un archivo de texto y lo comprima usando el algoritmo de codificación de Huffman. Luego, el programa debe descomprimirlo para restaurar el archivo original. Este ejercicio cubre estructuras de datos avanzadas, gestión de memoria dinámica, y comprensión de algoritmos de compresión.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

#define MAX_TREE_HT 100

// Estructura de un nodo de un árbol de Huffman
struct MinHeapNode {
    char data;
    unsigned freq;
    struct MinHeapNode *left, *right;
};

// Estructura de un árbol de Huffman
struct MinHeap {
    unsigned size;
    unsigned capacity;
    struct MinHeapNode **array;
};

// Estructura de un nodo de un árbol de Huffman
struct MinHeapNode *newNode(char data, unsigned freq) {
    struct MinHeapNode *temp = (struct MinHeapNode *)malloc(sizeof(struct MinHeapNode));
    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

// Estructura de un árbol de Huffman
struct MinHeap *createMinHeap(unsigned capacity) {
    struct MinHeap *minHeap = (struct MinHeap *)malloc(sizeof(struct MinHeap));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array = (struct MinHeapNode **)malloc(minHeap->capacity * sizeof(struct MinHeapNode *));
    return minHeap;
}

// Intercambia dos nodos de un árbol de Huffman
void swapMinHeapNode(struct MinHeapNode **a, struct MinHeapNode **b) {
    struct MinHeapNode *t = *a;
    *a = *b;
    *b = t;
}

// Función para min-heapify el árbol de Huffman
void minHeapify(struct MinHeap *minHeap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < minHeap->size && minHeap->array[left]->freq < minHeap->array[smallest]->freq)
        smallest = left;

    if (right < minHeap->size && minHeap->array[right]->freq < minHeap->array[smallest]->freq)
        smallest = right;

    if (smallest != idx) {
        swapMinHeapNode(&minHeap->array[smallest], &minHeap->array[idx]);
        minHeapify(minHeap, smallest);
    }
}

// Función para verificar si el tamaño del árbol de Huffman es 1
int isSizeOne(struct MinHeap *minHeap) {
    return (minHeap->size == 1);
}

// Función para extraer el nodo con la frecuencia más baja del árbol de Huffman
struct MinHeapNode *extractMin(struct MinHeap *minHeap) {
    struct MinHeapNode *temp = minHeap->array[0];
    minHeap->array[0] = minHeap->array[minHeap->size - 1];

    --minHeap->size;
    minHeapify(minHeap, 0);

    return temp;
}

// Función para insertar un nuevo nodo en el árbol de Huffman
void insertMinHeap(struct MinHeap *minHeap, struct MinHeapNode *minHeapNode) {
    ++minHeap->size;
    int i = minHeap->size - 1;

    while (i && minHeapNode->freq < minHeap->array[(i - 1) / 2]->freq) {
        minHeap->array[i] = minHeap->array[(i - 1) / 2];
        i = (i - 1) / 2;
    }

    minHeap->array[i] = minHeapNode;
}

// Función para construir un árbol de Huffman
void buildMinHeap(struct MinHeap *minHeap) {
    int n = minHeap->size - 1;
    int i;

    for (i = (n - 1) / 2; i >= 0; --i)
        minHeapify(minHeap, i);
}

// Función para imprimir un array de tamaño n
void printArr(int arr[], int n) {
    int i;
    for (i = 0; i < n; ++i)
        printf("%d", arr[i]);
    printf("\n");
}

// Función para verificar si un nodo es una hoja
int isLeaf(struct MinHeapNode *root) {
    return !(root->left) && !(root->right);
}

// Función para crear un min-heap de tamaño igual al número de nodos
struct MinHeap *createAndBuildMinHeap(char data[], int freq[], int size) {
    struct MinHeap *minHeap = createMinHeap(size);

    for (int i = 0; i < size; ++i)
        minHeap->array[i] = newNode(data[i], freq[i]);

    minHeap->size = size;
    buildMinHeap(minHeap);

    return minHeap;
}

// Función para construir un árbol de Huffman y devolver la raíz
struct MinHeapNode *buildHuffmanTree(char data[], int freq[], int size) {
    struct MinHeapNode *left, *right, *top;
    struct MinHeap *minHeap = createAndBuildMinHeap(data, freq, size);

    while (!isSizeOne(minHeap)) {
        left = extractMin(minHeap);
        right = extractMin(minHeap);

        top = newNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;

        insertMinHeap(minHeap, top);
    }

    return extractMin(minHeap);
}

// Función para imprimir códigos de Huffman desde el árbol de Huffman
void printCodes(struct MinHeapNode *root, int arr[], int top) {
    if (root->left) {
        arr[top] = 0;
        printCodes(root->left, arr, top + 1);
    }

    if (root->right) {
        arr[top] = 1;
        printCodes(root->right, arr, top + 1);
    }

    if (isLeaf(root)) {
        printf("%c: ", root->data);
        printArr(arr, top);
    }
}

// Función principal que construye y llama a las funciones anteriores
void HuffmanCodes(char data[], int freq[], int size) {
    struct MinHeapNode *root = buildHuffmanTree(data, freq, size);
    int arr[MAX_TREE_HT], top = 0;

    printCodes(root, arr, top);
}

// Función para comprimir un archivo de texto usando el algoritmo de Huffman
void compressFile(char *fileName) {
    FILE *file = fopen(fileName, "r");
    if (!file) {
        printf("No se pudo abrir el archivo %s\n", fileName);
        return;
    }

    int freq[256] = {0};
    char buffer[100], data[100];
    int i = 0;

    while (fscanf(file, "%s", buffer) != EOF) {
        for (i = 0; buffer[i]; ++i) {
            data[i] = buffer[i];
            ++freq[buffer[i]];
        }
        data[i] = '\0';
    }

    fclose(file);

    int size = i;
    HuffmanCodes(data, freq, size);
}

// Función principal
int main() {
    char fileName[] = "sample.txt";
    compressFile(fileName);
    return 0;
}
