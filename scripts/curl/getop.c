#include <stdio.h>

int main(int argc, char** argv){
	if(argc < 2){
		printf("error with arguments, please supply more than 1\n");
		return 4;
	}
	printf("%s",argv[1]);
	return 0;
}
