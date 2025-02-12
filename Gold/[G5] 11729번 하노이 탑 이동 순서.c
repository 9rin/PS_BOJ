/*
첫째 줄에 옮긴 횟수 K를 출력한다.
두 번째 줄부터 수행 과정을 출력한다. 
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.
*/


#include <stdio.h>
int res = 0;

void hanoi(int n, char from, char tmp, char to){
    if (n == 1) {
        printf("%c %c\n", from, to);
    }
    else
    {
    hanoi(n - 1, from, to, tmp);
    printf("%c %c\n", from, to);
    hanoi(n - 1, tmp, from, to);
    }
}

int hanoi_res(int n, char from, char tmp, char to){
    if(n==1){
        res = res + 1;
    }
    else{
        hanoi_res(n-1, from, to, tmp);
        res = res + 1;
        hanoi_res(n-1, from, tmp, to);
    }
    return res;
}

int main(void){
    int n;
    scanf("%d", &n);
    printf("%d\n", hanoi_res(n, '1','2','3'));
    hanoi(n, '1', '2', '3');
    return 0;
}