#include <stdio.h>
int main(){
	int arr[1001],count,inp;
	scanf("%d",&count);
	for(int i=0;i<count;i++){
		scanf("%d",&inp);
		arr[1] = 1;
		arr[2] = 2;
		arr[3] = 4; 
		for(int i=4;i<=inp;i++){
			arr[i]=arr[i-1]+arr[i-2]+arr[i-3];
		}
		printf("%d\n",arr[inp]);	
	}
}