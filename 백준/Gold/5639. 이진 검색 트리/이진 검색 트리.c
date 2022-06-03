#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int value;
	struct Node* left;
	struct Node* right;
}Node;

void insertNode(Node* headNode, int value);
void rightSearch(Node* headNode);

int main() {
	int value;
	Node* headNode = (Node*)malloc(sizeof(Node));
	scanf("%d", &value);
	headNode->value = value;
	headNode->left = NULL;
	headNode->right = NULL;
	while (1){
    	if (scanf("%d", &value) == EOF) { break; }
    	insertNode(headNode, value);
	}
	rightSearch(headNode);
	return 0;
}

void insertNode(Node* headNode, int value){
	if(value > headNode->value && headNode->right == NULL){
		Node* newNode = (Node*)malloc(sizeof(Node));
		newNode->left = NULL;
		newNode->right = NULL;
		newNode->value = value;
		headNode->right = newNode;
	}
	else if(value < headNode->value && headNode->left == NULL){
		Node* newNode = (Node*)malloc(sizeof(Node));
		newNode->left = NULL;
		newNode->right = NULL;
		newNode->value = value;
		headNode->left = newNode;
	}
	else if(value > headNode->value){
		insertNode(headNode->right, value);
	}
	else{
		insertNode(headNode->left, value);
	}
}

void rightSearch(Node* headNode){
	if(headNode->left != NULL) rightSearch(headNode->left);
	if(headNode->right != NULL)rightSearch(headNode->right);
	printf("%d\n", headNode->value);
}