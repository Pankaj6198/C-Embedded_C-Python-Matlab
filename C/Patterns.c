#include<stdio.h>
#include<stdlib.h>

void upper_tri();
void lower_tri();
void right_upperhalf();
void right_lowerhalf();
void pyramid();
void rev_pyramid();
void pyramid_numtype1();
void pyramid_numtype2();
void pyramid_numtype3();
void pyramid_char_type1();


void main()
{int ch;
 while(1)
{ printf("\n"); 
  printf("Choose pattern\n1.Upper triangular\n2.Lower triangular\n3.Right Upper triangular\n4.Right Lower triangular\n5.Pyramid\n6. Reverse Pyramid\n7.Numeric Pyramid type-1\n8.Numeric Pyramid type-2\n9.Numeric Pyramid type-3\n10.Character Pyramid type-1\t");
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
			break;
	case 6: rev_pyramid();
			break;
	case 7:pyramid_numtype1();
			break;
	case 8:pyramid_numtype2();
			break;
	case 9:pyramid_numtype3();
			break;
	case 10:pyramid_char_type1();
			break;
	
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
{int i,j,k,space=40;
printf("\n");
 for(i=1;i<=5;i++)//Rows
 {   
    for(j=1;j<=space-i;j++)// Spaces
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

/*

*********
 *******
  *****
   ***
    *
*/

void rev_pyramid()
{int i,j,k;
	for(int i=5;i>=1;i--)
    { 
         for(int j=1;j<=5-i;j++)
            printf(" ");

        for(int k=1;k<=(2*i)-1;k++)
        printf("*");

        printf("\n");

    }
	
}




 /*
    1
   212
  32123
 4321234
543212345

*/

void pyramid_numtype1()
{ int i,j,k,l;
 for( i=1;i<=5;i++)
{     for( k=1;k<=5-i;k++)
      printf(" ");
    
      for( j=i;j>=1;j--)
       printf("%d",j);

      for ( l=2;l<=i;l++)
         printf("%d",l);
	
	printf("\n");
}

}


/*
    1
   121
  12321
 1234321
123454321

*/
void pyramid_numtype2()
{ int i,j,k,l;
for( i=1;i<=5;i++)
{
	for(k=1;k<=5-i;k++)
        printf(" ");
    for(l=1;l<=i;l++)
        printf("%d",l); 

    for(j= i-1 ; j>=1;j--)
        printf("%d",j);
          
      
      printf("\n");  
}

}

/*
     0
    101
   21012
  3210123
 432101234

*/
void pyramid_numtype3()
{ 
   for(int i=0;i<5;i++)
    { for(int k=1;k<=5-i;k++)
      printf(" ");
    
      for(int j=i;j>=0;j--)
       printf("%d",j);

      for (int l=1;l<=i;l++)
         printf("%d",l);
	
	printf("\n");
	}	 
}


/*
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

*/

void pyramid_char_type1()
{char ch;
    for(int i=1;i<=5;i++)
    {
        for(int k=1;k<=5-i;k++)
        printf(" ");
         //ch=64;
         ch=65;
        for(int j=1;j<=i;j++)
        {  // ch++;
            printf("%c",ch);
            ch++;
        }
       //ch=ch-1;
      
       for(int l=ch-2;l>=65;l--)
        printf("%c",l);
         
        
        printf("\n");
	}
}



