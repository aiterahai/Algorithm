#include <stdio.h>
int main(){
	int t, arr[10], temp;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		for(int j = 0; j < 10; j++){
			scanf("%d", &arr[j]);
		}
		for(int k = 0; k < 10; k++){
			for(int l = 0; l < 10-k-1; l++){
				if(arr[l] > arr[l+1]){
					temp = arr[l];
					arr[l] = arr[l+1];
					arr[l+1] = temp;
				}
			}
		}
		printf("%d\n", arr[7]);
	}
}