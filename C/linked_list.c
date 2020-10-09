#include<stdio.h>
#include<stdlib.h>

struct node
{ int data;
  struct node *link; 
};
struct node *head,*current; //current for : Making append O(1)
int len;
void append();
void add_at_beg();
void add_after();
void delete();
int length();
void display();
void reverse();

void main()
{ int choice;
  while(1)
  { 
      printf("\n\n ****Singly Linked List Operations****\n1.Append \n2.Insertion_at_Begining \n3.Insertion_After_Certain_position \n4.Deletion \n5.Length \n6.Display \n7.Reverse \n8.Exit \n\n");
      scanf("%d",&choice);
      switch(choice)
      {case 1: append();
                break;
       case 2: add_at_beg();
               break;
        case 3:add_after();
               break;
        case 4: delete();
               break;
        case 5:len=length();
			 printf("\nLength : %d\n",len);
               break;
        case 6: display();
               break;
        case 7:reverse();
               break;
        case 8: exit(0);
        default: printf("Invalid choice\n");        

      }
      
  }

}

void append()
{  struct node *newnode;
   newnode=(struct node*) malloc(sizeof(struct node));
   printf("Enter node Data \n");
   scanf("%d",&newnode->data);
   newnode->link=NULL;
    if(head==NULL)
    {   head=current=newnode;

    }
    else
    {  current->link=newnode;  // O(1)
	   current=newnode;
       /* while(ptr->link!=NULL)  //O(n) 
		                          //ptr moves to last Node 
        { ptr=ptr->link;

        }
         ptr->link=temp;   		// address of last node in ptr
      */
	}  
}

void add_at_beg()
{  struct node *temp;
   temp=(struct node*) malloc(sizeof(struct node));
   printf("Enter node Data");
   scanf("%d",&temp->data);
   temp->link=NULL;
   if(head==NULL)
   { head=temp;
   }
   else
   {   temp->link=head;
       head=temp;
   }

}

void add_after()
{ struct node *temp,*ptr;
  int pos,count=0;
   temp=(struct node*) malloc(sizeof(struct node));
   printf("Enter node Data \n");
   scanf("%d",&temp->data);
   printf("Enter the position ");
   scanf("%d",&pos);
   temp->link=NULL;
   len=length();
    if(pos>len)
   { printf("Invalid position");

   }
   else
   { ptr=head; 
	while(count<pos-1) //current node
   {  ptr=ptr->link;
      count++;
   }
       temp->link=ptr->link;
       ptr->link=temp;

   }
}

 void delete()
 {int loc,i=1;
  struct node *p,*temp;
  printf("Enter Location :\t");
  scanf("%d",&loc);
  len=length();
	 if(loc>len)
	 {
		 printf("Invalid position");
	 }
	 else
	 {   p=head;
		 if(loc==1)
		 {  head=p->link;
			p->link=NULL;
			free(p);
		 }
		 else
		 {
			 while(i<loc-1)    //previous node
			 {p=p->link;
				i++;	 
			 }
			 temp=p->link;
			 p->link=temp->link;
			 temp->link=NULL;
			 free(temp);
			 
		 }
		 
	 }
 }

 
 void display()
{ struct node *temp;
  temp=head;
  while(temp!=NULL)
  {
       printf("%d->",temp->data);
       temp=temp->link;

  }
        
}

 int length()
 { len=0;
  struct node *temp;
  temp=head;
  while(temp!=NULL)
  { len++;
    temp=temp->link;
  }
    return(len);  
 }

 void reverse()
 {   
	 struct node *start,*end;
	 int i,j,k,temp;
	 start=end=head;
	 length();
	 i=0;
	 j=len-1;
	 while(i<j)
	 {  k=0;
		while(k<j)
		{
			end=end->link;
			k++;
		}
		temp=start->data;
		start->data=end->data;
		end->data=temp;
		i++;
		j--;
		start=start->link;
		end=head;
		
	 }
       
 }
