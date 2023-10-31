#include<stdio.h>
#include<lib.h>
struct node()
{
	int data;
	struct node *next;
}
struct node *create(int data){
	struct node *ptr=(struct node *)malloc(sizeof(struct node));
	ptr->data;
	ptr->next=NULL;
	
	return ptr;
}
void display(struct node *head){
	struct node *run=head;
	while(run!=NULL){
		printf("%d",&run->data);
		run=run->next;
	}
}
void node *insert_after(struct node* head, struct node* third,int data){
	struct node* new=create(data);
	struct node *run=head;
	while(run!=third){
		run=run->next;
	}
	new->next=run->next;
	run->next=new;
}

	
}

int main()
{
	printf("Enter 1 to create a node");	
	printf("Enter 2 to insert a node");
	printf("Enter 3 to display the singly linked list");
	scanf("%d",&a);
switch(a)
case 1:
	create();
		break;
case 2:
	insert_after();
		break;
case 3:
	display();
		break;		
}

