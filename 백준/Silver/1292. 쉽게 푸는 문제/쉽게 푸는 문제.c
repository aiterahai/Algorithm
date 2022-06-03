#include <stdio.h>
int main(){
	int a, b, arr[1000] = {0,}, sum = 0, count = 1, idx = 0;
	scanf("%d %d", &a, &b);
    while(idx != 1000){
    	for(int i = 0; i < count && idx != 1000; i++) arr[idx++] = count;
    	count++;
	}
	for(int i = a - 1; i < b; i++){
		sum += arr[i];
	}
	printf("%d", sum);
}