#include <stdio.h>
int min(int a,int b){
	return (a<b)?a:b;
}
int main(){
	int arr[1000001],count;
	scanf("%d",&count);
	arr[1]=0;
	for(int i=2;i<=count;i++){
		arr[i]=arr[i-1]+1;
		if(i%2==0){
			arr[i] = min(arr[i],arr[i/2]+1);
		}
		if(i%3==0){
			arr[i] = min(arr[i],arr[i/3]+1);
		}
	}
	printf("%d",arr[count]);
}