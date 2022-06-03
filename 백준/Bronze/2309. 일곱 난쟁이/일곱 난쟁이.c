#include <stdio.h>
int main(){
	int arr[9], num = 0, temp;
	for(int i = 0; i < 9; i++){
		scanf("%d", &arr[i]);
		num += arr[i];
	}
	num -= 100;
	for(int i = 0; i < 9; i++){
		for(int j = 0; j < 9 - i - 1; j++){
			if(arr[j] > arr[j+1]){
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	
	for(int i = 0; i < 9; i++){
		for(int j = i + 1; j < 9; j++){
			if(arr[i] + arr[j] == num){
				arr[i] = 0;
				arr[j] = 0;
				i = 8;
			}
		}
	}
	
	for(int i = 0; i < 9; i++){
		if(arr[i]) printf("%d\n", arr[i]);
	}
}