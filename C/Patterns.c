#include<stdio.h>
#include<stdlib.h>

void upper_tri();
void lower_tri();
void right_upperhalf();
void right_lowerhalf();
void pyramid();

void main()
{int ch;
 while(1)
{ printf("\n"); 
  printf("Choose pattern\n1.Upper triangular\n2.Lower triangular\n3.Right Upper triangular\n4.Right Lower triangular\n5.Pyramid \t\t");
  scanf("%d",&ch);
	 switch(ch)
 {
	case 1:upper_tri();
			break;
	case 2:lower_tri();
			break;
	case 3:right_upperhalf();
			break;
	case 4:right_lowerhalf();
			break;
	case 5:pyramid();
    default:exit(0);			
 }
} 
}


/*  upper

12345
1234
123
12
1

*/
void upper_tri()   
{ int i,j;
printf("\n");
 for(i=5;i>=1;i--)// Rows
 {
	 for(j=1;j<=i;j++)//Col.
	 {
		 printf("%d",j);
		 
	 }
	 printf("\n");
 }
	
}


/* Lower

1
12
123
1234
12345

*/
void lower_tri()
{int i,j;
printf("\n");
 for(i=1;i<=5;i++)
 {
	 for(j=1;j<=i;j++)
	 {
		 printf("%d",j);
		 
	 }
	 printf("\n");
 }
	
}


/* right upperhalf

12345
 1234
  123
   12
    1

*/
void right_upperhalf()
{ int i,j,k;
printf("\n");
 for(i=5;i>=1;i--)//rows
 {  
    for(j=i;j<5;j++)// Spaces
	 {
		 printf(" ");
		 
	 }
	for(k=1;k<=i;k++)//cols
	 {
		 printf("%d",k);
		 
	 }
	printf("\n");
 }
		
}

/*  right lowerhalf

    1
   12
  123
 1234
12345


*/

void right_lowerhalf()
{int i,j,k;
printf("\n");
 for(i=1;i<=5;i++)//Rows
 {   
    for(j=i;j<5;j++)// Spaces
	 {
		 printf(" ");
		 
	 }
	for(k=1;k<=i;k++)//Cols.
	 {
		 printf("%d",k);
		 
	 }
	printf("\n");
 }
}

/* Pyramid
            *
		   ***
		  *****
		 *******
		*********
*/

void pyramid()
{int i,j,k,l=40;
printf("\n");
 for(i=1;i<=5;i++)//Rows
 {   
    for(j=1;j<=l-i;j++)// Spaces
	 {
		 printf(" ");
		 
	 }
	for(k=1;k<=2*i-1;k++)//Cols.
	 {
		 printf("*");
		 
	 }
	printf("\n");
 }
	
}