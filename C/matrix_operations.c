#include<stdio.h>

void main()
{
   int a[3][3]= {1,1,1,1,1,1,1,1,1} ,b[3][3]={1,1,1,1,1,1,1,1,1},c[3][3],i,j, srow,scol,smajor_diag,sminor_diag;
    
   srow=scol=smajor_diag=sminor_diag=0;
   
   printf("\nMatrix A : \n");
   for(i=0;i<3;i++)
   {   for(j=0;j<3;j++)
      printf("%d\t",a[i][j]);
      printf("\n");
   }

   printf("\nMatrix B : \n");
   for(i=0;i<3;i++)
   {   for(j=0;j<3;j++)
      printf("%d\t",b[i][j]);
      printf("\n");
   }

 printf("\n Matrix Addition : \n");
    for(i=0;i<3;i++)
   {   for(j=0;j<3;j++)
      printf("%d\t",a[i][j]+b[i][j]);
      printf("\n");
   }

  printf("\n Matrix Subtraction : \n");
    for(i=0;i<3;i++)
   {   for(j=0;j<3;j++)
      printf("%d\t",a[i][j]-b[i][j]);
      printf("\n");
   }



    printf("\n Matrix Multiplication : \n");
   for(i=0;i<3;i++)
   {  for(j=0;j<3;j++)
    {  c[i][j]=0;
     for(int k=0;k<3;k++)
     {
        c[i][j]=c[i][j]+a[i][k]*b[k][j];
        
     }
     printf("%d\t",c[i][j]);
    }
    printf("\n");
   }

    printf("\n Matrix Addition Row , Col wise , major and minor diagonal sum : \n");
   for(i=0;i<3;i++)
   {   srow=scol=0;
       for(j=0;j<3;j++)
    { if(i==j)
        smajor_diag=smajor_diag+a[i][j];
      if(i+j==2)// when 3x3 matrix i+j = (anything(row/col)) - 1
        sminor_diag=sminor_diag+a[i][j];
      srow=srow + a[i][j];
      scol=scol + a[j][i];
    }
    printf("\n Row %d sum :%d , Col %d sum :%d",i+1,srow,i+1,scol);
   }
   printf("\n Major Diagonal sum = %d \n",smajor_diag);
   printf(" Minor Diagonal sum = %d \n",sminor_diag);
  printf("\n Transpose of Matrix A  : \n");
  for(i=0;i<3;i++)
   {   for(j=0;j<3;j++)
       printf("%d\t",a[j][i]);
      printf("\n");
   }


}