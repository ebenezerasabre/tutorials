#include <stdio.h>
#include <string.h>

void count(const char * a_string){
	int a_dict[256] = {0}; // init all elements to zero
	
	// iterate through the string and count each character
	for(int i=0; i < strlen(a_string); i++){
		unsigned char char_index = (unsigned char)a_string[i];
		a_dict[char_index] += 1;
	}

	// print the character countss
	printf("{");
	for(int i=0; i < 256; i++){
		if(a_dict[i] > 0){
			printf("'%c': %d, ", i, a_dict[i]);
		}
	}
	printf("}\n");


}


int main(){

	const char * test_string = "hello world";
	count(test_string);

	

	return 0;
}


