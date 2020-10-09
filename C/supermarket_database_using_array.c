
#include<stdio.h> 
#include<string.h>
#include<stdlib.h>

//structure type
typedef struct Product
{   int serial_no;
    char product_name[300];
    int quantity;
    float price;
}product;
product data[1000];
int n;

//function declaration
void entry();
void deletion();
void update();
void display();
int duplicate_serialno(int); // To check duplicacy in serial no 


//Driver Code
void main()
{ int choice,flag=1;
      if(flag)
   {    while (flag)
    { printf("\t\t\t\t\t\t***** MENU ***** \n\t\t\t\t\t\t 1.Data Entry \n\t\t\t\t\t\t 2. Deletion \n\t\t\t\t\t\t 3.Update \n\t\t\t\t\t\t 4. Display \n\t\t\t\t\t\t 5. Exit\n"); 
      printf("\t Enter your choice \n");
      scanf("%d",&choice);
        switch(choice)
        {case 1: entry(); 
                 break;
        case 2: if(n==0)
                {printf("\n Database Empty \n");
                  break;
                }
                 deletion(n);
                 break;
        case 3: if(n>0)
                update();
                else
                {
                  printf("/t/t Need to Enter the data first/n");
                }
                 break;
        case 4: display(n);
                break;
        case 5: exit(0);
        default:printf("\n Invaid Choice \n");

        } 
        
        printf("\n \t\t Do you want to continue with menu (yes=1,no=0) \n");
        scanf("%d",&flag);
    }
   }
   exit(0);
}


// Function Definations

void entry()
{ int i=0,flag=0;
 printf("\n No. of Entries to be enterered\t \n");
 scanf("%d",&n);
 while(i<n)
{ 
  if(flag==0)
 { 
   printf("\t \nEnter Product serial_no \t");
 scanf("%d",&data[i]);
 flag=duplicate_serialno(i);
 if(flag==1)
 {printf("\t\t Duplicate Serial No. Entered (Enter Again) \n");
    flag=0;
    continue;

 }
 printf("Enter Product Name \t");
 scanf("%s",data[i].product_name);
 printf("Enter Product Quantity \t");
 scanf("%d",&data[i].quantity);
 printf("Enter Product Price(in Rs) \t \n"); 
 scanf("%f",&data[i].price);
 
  }
  i++;
}

}

void deletion()
{ int del_serialno,del_index=0,start=0,end=n-1,mid,i;
  printf("\n\t\tEnter the Serial No. whose entry to be deleted \t");
  scanf("%d",&del_serialno);
  while (start<=end && start>=0)
  { mid=(start+end)/2;
    if(data[mid].serial_no==del_serialno)
     {
       del_index=mid;
       break;
     }
     else if(data[mid].serial_no < del_serialno)
     start=mid+1;
     else
     {
       end=mid-1;
     }
  }
    for (i = del_index; i <n-1; i++)
  {
    data[i].serial_no=data[i+1].serial_no;
    strcpy(data[i].product_name,data[i+1].product_name);
    data[i].quantity=data[i+1].quantity;
    data[i].price=data[i+1].price;
  }
  n--;
  printf("Serial No. %d Successfully Deleted \n",del_serialno);
   for(i=0;i<n;i++)
  {
     printf("\t\t Serial No. : %d \t \n Product Name : %s \t\n Product Quantity : %d  \t\n Product Price(in Rs): %.2f\n\n",data[i].serial_no,data[i].product_name,data[i].quantity,data[i].price);
     
  
  }
   
}


void update()
{ int serialno;
  char updated_name[300];
 printf("Enter the serial no. whose entry to be updated \t");
 scanf("%d",&serialno);
  printf("Enter Product Name \t ");
  scanf("%s",data[serialno-1].product_name);
  printf("Enter Product Quantity \t ");
  scanf("%d",&data[serialno-1].quantity);
  printf("Enter Product Price(in Rs) \t\n"); 
  scanf("%f",&data[serialno-1].price);
  printf("\t Data successfully updated \n");
}

void display()
{ int i=0;
  for(i=0;i<n;i++)
  {
     printf("\t\t Serial No. : %d \t \n Product Name : %s \t\n Product Quantity : %d  \t\n Product Price(in Rs): %.2f\n\n",data[i].serial_no,data[i].product_name,data[i].quantity,data[i].price);
     //printf("\n\t %d \t %s \t\t  %d \t\t\t  %.2f \n",data[i].serial_no,data[i].product_name,data[i].quantity,data[i].price);
  
  }
}

int duplicate_serialno(int i)
{ int j=0,flag=0;
  if(i==0)
    return(flag);
  else if (i>0)
  { for(j=0;j<i;j++)
    { if(data[j].serial_no==data[i].serial_no)
      { flag=1;
        break;
      }
      else
      {
        flag=0;
      }
    }
  }
  return(flag);

}
