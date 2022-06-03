#include <stdio.h>
int main(){
	int n, k, count = 0;
	scanf("%d %d", &n, &k);
	for(int i = 1; i <= n; i++){
		if(n%i==0){
			count++;
		}
		if(count==k){
			printf("%d", i);
			break;
		}
	}
	if(count<k){
		printf("0");
	}
}