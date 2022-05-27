#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{

	int N,i;
	N=10000;
	int r[N];
	float a[N],b[N],e[N];
	for (i=0;i<N;i++){
		r[i] = rand();
		a[i] = (r[i]%32767);
		b[i] = (a[i]/32767.0f-0.5)*10;
		e[i] = exp(b[i]);
		printf("%d \t %f \t %f \t %f \n",r[i],a[i],b[i],e[i]);
	}
	
	printf("\n\nHistogram of Float data\n");
	int j,count;
	for (i = 1; i <= 50; i++)
	{
	    count = e[i];
	    printf("0.%d |", i - 1);
	    for (j = 0; j < 50; j++)
	    {
	        printf("%c", (char)254u);
	    }
	    printf("\n");
	}
	
	return 0;
}

