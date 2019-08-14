#include <stdio.h>
#include <stdlib.h>
#define N 5
int main (){
	int Vetor[3][3]={1,2,3,4,5,6,7,8,9};
	int Vector[2][2];
	int i,j;
	foŕ(i=0;i<=2;i++){
		for(j=0;j<=2;j++){
			Vector[i][j]=Vetor[i][j];
		}
	}
	printf("o vetor 1 tem sequencia: %d e o vetor 2 tem sequencia %d\n",Vetor,Vector);
	return 0;
}