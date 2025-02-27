#include <stdio.h>

int heap[100001] = {};
int heap_size = 0;
int a;

void insert(){
    int i = ++heap_size;

    while((i!=1)&&heap[i/2]>a){
        heap[i] = heap[i/2];
        i = i/2;
    }
    heap[i] = a;
}

void pop(){
    int parent, child, root, tmp; 

    if (heap_size == 0) {
        printf("0\n");
        return;
    }

    root = heap[1];
    tmp = heap[heap_size--]; // 후위연산자 

    // Heapify-Down
    parent = 1;
    child = 2;

    while (child <= heap_size) {
        if (child < heap_size && heap[child] > heap[child + 1]) {
            child++;
        }

        if (tmp <= heap[child]) break;

        heap[parent] = heap[child];
        parent = child;
        child *= 2; 
    }
    heap[parent] = tmp;

    printf("%d\n", root);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i=0; i<n; i++){
        scanf("%d", &a);

        if(a == 0){
            pop();  
        }
        else{
            insert();  
        }
    }
}
