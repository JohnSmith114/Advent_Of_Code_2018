#define NPLAYERS 425
#define LASTP 7084800

#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int val;
	struct Node* next;
	struct Node* prec;
}mNode;

typedef mNode* pMarble;

void insert(pMarble headPointer, int value, int position){
	int currPos = 0;
	pMarble currP = headPointer;
	while(currPos != position && currP != NULL){
		currP = currP->next;
		currPos++;
	}
	
	pMarble newNode = malloc(sizeof(mNode));
	newNode->next = currP->next;
	currP->next = newNode;
}

int pop(pMarble headPointer, int position){
	int currPos = 0;
	pMarble currP = headPointer;
	while(currPos != position-1){
		currP = currP->next;
		currPos++;
	}
	pMarble temp = currP->next->next;
	int val = currP->next->val;
	free(currP->next);
	currP->next = temp;
	return val;
}

void printList(pMarble headPointer){
	pMarble currP = headPointer;
	while(currP != NULL){
		printf("%d -> ",currP->val);
		currP = currP->next;
	}
	printf("FINE LISTA\n");
}

int main(){
	int pPoints[NPLAYERS];
	pMarble headPointer = malloc(sizeof(mNode));
	headPointer->val = 0;
	headPointer->next = NULL;
	printList(headPointer);
	insert(headPointer, 5, 1);
	printList(headPointer);
	pop(headPointer,1);
	printList(headPointer);
	
	int currMarble = 0;
	int currPlayer = 0;


}
