#include <stdio.h>
int main(){
	int off, on, number = 0, max = 0;
	for(int i = 0; i < 10; i++){
		scanf("%d %d", &off, &on);
		if(max < number) max = number;
		number = number + on - off;
	}
	printf("%d", max);
}