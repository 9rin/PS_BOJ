//구조체, 포인터, 선형큐 활용

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int element;
typedef struct{
    int front;
    int rear;
    element data[2000000];
} QueueType;

void init_queue(QueueType* q){
    q -> rear = -1;
    q -> front = -1;
}

int is_empty(QueueType* q){
    if(q->front == q-> rear)
        return 1;
    else
        return 0;
}

//push X: 정수 X를 큐에 넣는 연산이다.
void push(QueueType* q, int X){
    q-> data[++(q->rear)] = X;
}

//pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
int pop(QueueType* q){
    if(is_empty(q)){
        return -1;
    }
    int x = q->data[++(q->front)];
    return x;
}

//size: 큐에 들어있는 정수의 개수를 출력한다.
int size(QueueType* q){
    return q->rear-q->front;
}

//front: 큐의 가장 앞에 있는 정수를 출력한다. 
//front는 항상 "마지막으로 제거된 요소"의 위치를 가리킵니다.
//따라서 front + 1을 해줘야 현재 큐의 첫번째 원소를 출력 가능. 
int front(QueueType* q){
    if(is_empty(q)){
        return -1;
    }
    return q->data[q->front+1];
}

//back: 큐의 가장 뒤에 있는 정수를 출력한다.
int back(QueueType* q){
    if(is_empty(q)){
        return -1;
    }
    return q->data[q->rear];
}


int main(void){
    QueueType q;
    init_queue(&q);
    
    int n;
    scanf("%d", &n); 

    for (int i = 0; i < n; i++) {
        char s[10];  
        scanf("%s", s);  

        if (strcmp(s, "push") == 0) {
            int X;
            scanf("%d", &X);  
            push(&q, X);
        }
        else if (strcmp(s, "pop") == 0) {
            printf("%d\n",pop(&q));
        }
        else if (strcmp(s, "front") == 0) {
            printf("%d\n",front(&q));
        }
        else if (strcmp(s, "back") == 0) {
            printf("%d\n",back(&q));
        }
        else if (strcmp(s, "size") == 0) {
            printf("%d\n",size(&q));
        }
        else if (strcmp(s, "empty") == 0) {
            printf("%d\n",is_empty(&q));
        }
    }//for 끝
}//main 함수 끝 

