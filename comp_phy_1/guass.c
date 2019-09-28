#include <stdio.h>
#include <math.h>  // AS I AM USING FABS()

int main()
{

printf("\nPlease enter dimension mxn\t");
int m,n,i,j,k,l,t,x,y;
scanf("%d %d",&m,&n);
double matt[m][n];
double mat[m][1], sol[m][1];
double c;

if (m<n)	// CHECKING IF SOLVABLE
{
	printf("You have screwed up big time");
}

else
{
	printf("Please enter matrix\t");
	
	for(i=0; i<m; i++) // taking input
	{
		for(j=0; j<n; j++)
		{
			scanf("%lf", &matt[i][j]);  	// NOW WE HAVE THE MATRIX
		}
	}


	printf("Please enter sol\t"); 	
	
	for(i=0; i<m; i++)
	{
		scanf("%lf", &mat[i][0]);	
	}



	int temp;

	for(i=0; i<n; i++) // TRACKING THE DIAGONAL ELEMENT WITH i
	{

		l=i;
			
		if(matt[i][i]==0)	// PIVOTING
		{
			while(matt[l][i]==0)
			{
				l++;	
				printf("\nChecking l value %d", l);	
				if (l>m) break;
			}
		}
		
		if(i!=l)	// INSTEAD OF SWAPPING I MAKE DIAG ELEMENT ZERO WITH ADDING EQN
		{
			mat[i][0]=mat[i][0]+mat[l][0];		
	
			for(t=i; t<n; t++)
			{
				matt[i][t]=matt[i][t]+matt[l][t];				
			}
		}

				
		temp = i;			

		for(j=0; j<m; j++)    // PARTIAL PIVOTING
		{
			if(matt[j][i]!=0)
			{
				if(fabs(matt[temp][i])>fabs(matt[j][i]))
				{
					temp=j;		
				}
			}
		}
		
		
		if(i!=temp)
		{
			c=matt[temp][i]/matt[i][i];
			mat[i][0]=mat[i][0]*c;		
	
			for(t=i; t<n; t++)
			{
				matt[i][t]=matt[i][t]*c;				
			}
		}



		for(k=i; k<m; k++) // ROW OPERATIONS
		{
			if((k!=i)&&(matt[k][i]!=0))
			{
			
			c=matt[i][i]/matt[k][i];

			mat[k][0]=c*mat[k][0];
			mat[k][0]=mat[k][0]-mat[i][0];

			for(t=0; t<n; t++)
			{
				matt[k][t]=c*matt[k][t];				
			}

			for(t=i; t<n; t++)
			{
				matt[k][t]=matt[k][t]-matt[i][t];				
			}

			}

//..................Output_viewer.........................................
	printf("\n\n");
	for(x=0; x<m; x++) 
	{
		for(y=0; y<n; y++)
		{
			printf(" %lf ", matt[x][y]);
		}
	
	printf("      %lf\n", mat[x][0]);
	
	}
 	 
	
	printf("\n\n");
//........................................................................

		}
	}


//back substitution.............\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

double temp1;

sol[m-1][0]=mat[m-1][0]/matt[m-1][n-1];   // FINISHING WITH THE LAST VARIABLE AND USING IT TO SOLVE REST

for(x=m-2; x>=0; x--) 
{
	temp1=mat[x][0];
	for(y=n-1; y>x; y--)
	{
		temp1=temp1-matt[x][y]*sol[y][0];
	}

	sol[x][0]=temp1/matt[x][x];		
}
}

y=0;
	for(x=0; x<m; x++)
	{
		if(matt[x][x]!=0){y++;}		// COUNTING NUMBER OF ZERO IN DIAG	
	}
	

	if(y==m)
	{
		printf("\nThe solutions are");

		for(t=0; t<m; t++)
		{
			printf("\n%lf\n", sol[t][0]);
		}	
	}
	else 
	{
		printf("\nNo sloution exists\n");
	}

printf("\n");
return 0;
}
