#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define CHAR_COUNT 26 // only lowercase letters 'a' to 'z'
#define INITIAL_GROUP_CAPACITY 10


// helper function to generate a key based on the 
// character frequency of the strings
char * generateKey(char * str){
	int freq[CHAR_COUNT] = {0}; // arr to cnt freq of each char
	int len = strlen(str);

	for(int i=0; i<len; i++){
		freq[str[i] - 'a']++;// incrmnt frqncy for each char
	
	}
	
	// create a strng repsntn of the freq count to use as key
	char * key = malloc(CHAR_COUNT * 2 + 1); //alct enough space for the key
	char * p = key;
	for (int i=0; i<CHAR_COUNT; i++){
		p += sprintf(p, "%d#", freq[i]); // append freq of each char
	}
	return key;
}

// structure for storing each group of anagram
typedef struct {
	char ** anagrams; // array of strings
	int size; 	  // number of anagrams in this group
	int capacity;	  // capacity of the anagram array
	char * key;	  ;; the frequency based key for this group
} AnagramGroup;

// function to group anagrams
char *** groupAnagrmas(char ** strs, int strSize, int * returnSize, int ** returnColumSizes){
	if(strSize == 0){
		*returnSize = 0;
		return NULL;
	}
	
	// array of anagram groups (initial capacity of 10)
	AnagramGroup* groups = malloc(INITIAL_GROUP_CAPACITY * sizeof(AnagramGroup));
	int groupCount = 0;
	int groupCapacity = INITIAL_GROUP_CAPACITY;
	
	// Process each string in strs
	for(int i=0; i<strSize; i++){
		char * originalStr = strs[i];
		
		// generate frequency-based key for the string
		char * key = generateKey(originalStr);
		
		// chekc if this key already has a group
		int found = 0;
	
	}


}











int main(){

	char msg[] = "hello, world";
	printf("%s\n", generateKey(msg));

}





