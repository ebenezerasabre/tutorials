#include <stdio.h>
#include <string.h>
#include <stdbool.h>


#define CHAR_COUNT 256 // Assuming ASCII character set

// function to check if two strings are anagrams
int isAnagram(char * str1, char * str2){

	// check if the strings have the same length
	int len1 = strlen(str1);
	int len2 = strlen(str2);
	if(len1 != len2) return false;
	
	// step 2: create count array and and init to zero
	int count[CHAR_COUNT] = {0};
	int * ptr = &count[0];
	
	// count the frequency of each character in both strings
 // Step 3: Count the frequency of each character in both strings
    for (int i = 0; i < len1; i++) {
        count[(int)str1[i]]++; // increment count for characters in s
        count[(int)str2[i]]--;  // decrement count for characters in s
    }
 
	
	// check if all counts are 0
	for(int i = 0; i < CHAR_COUNT; i++)
		if(count[i] != 0) 
			return false;
	
	

	return true; // if all counts are zero, strings are anagram
}

int main(){

	char msg[] = "abcc ";
	char new[] = "abcc";
	
	printf("%d\n", isAnagram(msg, new));

	return 0;
}
