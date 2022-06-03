#include <stdio.h>
int main(){
	int t, n, count;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		scanf("%d", &n);
		count = 0;
		while(0 < n){
			if(n%2 == 1) printf("%d ", count);
			n = (n-(n%2))/2;
			count++;
		}
		printf("\n");
	} 
}