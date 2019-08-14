//Crie um programa que dado um vetor de inteiros, ordene-o.
#include <stdio.h>
#include <stdlib.h>
#define N 5
int main (){
	int i,j,aux=0;
	int vetor[N]={1,6,3,7,9}	
	for(i=0;i<=N-1;i++){
		for(j=1;j<=N;j++){
			if(vetor[i]>vetor[j]){
				aux=vetor[i];
				vetor[i]=vetor[j];
				vetor[j]=aux;
			}
		}
	}
	printf("o vetor inserido em ordem crescente é %d\n",vetor);
	return 0;
}