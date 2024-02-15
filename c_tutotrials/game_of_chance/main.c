#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>
#include "hacking.h"

#define DATAFILE  "/tmp/chance.data" // File to store user data

// custom user struct to store information about users
struct user {
  int uid;
  int credits;
  int highscore;
  char name[100];
  int (*current_game)();
};

// Function prototypes
int get_player_data();
void register_new_player();
void update_player_data();
void show_highscore();
void jackpot();
void input_name();
void print_cards(char *, char *, int);
int take_wager();
void play_the_game();
int pick_a_number();
int dealer_no_match();
int find_the_ace();
void fatal(char *);
void show_all_users();

// Global variables
struct user player;   // Player struct




int main() {
  int choice, last_game;

  srand(time(0)); // Seed the randomizer with the current time

  // try to read player data from file
  // if there is no data, register a new player
  if(get_player_data() == -1){
    register_new_player();
  }

  while(choice != 7){
    printf("-=[ Game of Chance Menu ]=-\n");
    printf("1 - Play the Pick a number game\n");
    printf("2 - Play the No Match Dealer game\n");
    printf("3 - Play the Find the Ace game\n");
    printf("4 - View current high score\n");
    printf("5 - Change your user name\n");
    printf("6 - Reset your account at 100 credits\n");
    printf("7 - Quit\n");

    scanf("%d", &choice);

    if((choice < 1) || choice > 7)
      printf("\n[!!]The number %d is an invalid selection.\n\n", choice);
    else if(choice < 4){
      if(choice != last_game){  // If the function pointer isn't set
        if(choice == 1)
          player.current_game = pick_a_number;
        else if (choice == 2)
            player.current_game = dealer_no_match;
        else
          player.current_game = find_the_ace;
        last_game = choice;   // and set last_game
      }
      play_the_game();
    }

    else if(choice == 4)
      show_highscore();
    else if (choice == 5){
      printf("\nChange user name\n");
      printf("Enter your new name: ");
      input_name();
      printf("Your name has been changed.\n\n");
    }
    else if (choice == 6){
      printf("\nYour account has been reset with 100 credits.\n\n");
      player.credits = 100;
    }

  }

  // show_all_users();
  // pick_a_number();

  return 0;
}

// This function reads the player data for the current uid
// from the file. It returns -1 if it is unable to find player
// data for the current uid
int get_player_data(){
  int fd, uid, read_bytes;
  struct user entry;

  uid = getuid();

  fd = open(DATAFILE, O_RDONLY);
  if(fd == -1) // can't open the file, maybe does not
    return -1;  // maybe doesn't exist

  read_bytes = read(fd, &entry, sizeof(struct user));
  while(entry.uid != uid && read_bytes > 0){  // loop until uid is found
    read_bytes = read(fd, &entry, sizeof(struct user)); // keep reading
  }
  close(fd);  //close the file
  if(read_bytes < sizeof(struct user))
    return -1;
  else
    player = entry;   // copy the ready entry into the player struct
  
  printf("Player logged in id: %d, name: %s\n", player.uid, player.name);
  printf("credits: %d, highscore: %d\n", player.credits, player.highscore);
  // printf("uid: %d, effective uid: %d\n", getuid(), geteuid());
  return 1;           // return success
}


// This is the new user registration function
// It will create a new player account and append it to the file
void register_new_player(){
  int fd;

  printf("-=-={New Player Registration}=-=-\n");
  printf("Enter your name: ");
  input_name();

  player.uid = getuid();
  player.highscore = player.credits = 100;

  fd = open(DATAFILE, O_WRONLY|O_CREAT|O_APPEND, S_IRUSR|S_IWUSR|S_IXUSR);
  if(fd == -1)
    fatal("in register_new_player() while opening file");
  write(fd, &player, sizeof(struct user));
  close(fd);

  printf("\nWelcome to the Game of Chance %s.\n", player.name);
  printf("You have been give %u credits.\n", player.credits);


}

// This function is used to input the player name, since
// scanf("%s", &whatever ) will stop input at the first space
void input_name(){
  char * name_ptr, input_char = '\n';
  while(input_char == '\n')    // Flush any leftover
      scanf("%c", &input_char); // newline chars
  
  name_ptr = (char *) &(player.name); // name_ptr = player name's address
  while(input_char != '\n'){ // loop until newline
    *name_ptr = input_char;   // put the input char into name field
    scanf("%c", &input_char); // Get the net char
    name_ptr++;               // Increment the name pointer

  }
  *name_ptr = 0; // Terminate the string
}

// This function writes the current player data to the file
// It is used primarily for updating teh credits after games
void update_player_data(){
  int fd, i, read_uid;
  char burned_byte;

  fd = open(DATAFILE, O_RDWR);
  if(fd == -1)  // if open fails here, something is really wrong
    fatal("in update_player_data() while opening file");
  read(fd, &read_uid, 4);   // Read the uid from the first struct.
  while(read_uid != player.uid){
    for(i = 0; i < sizeof(struct user) - 4; i++)   // Read through 
      read(fd, &burned_byte, 1);                    // the rest of the struct
    read(fd, &read_uid, 4);   // Read the uid from the next struct
  }
  write(fd, &(player.credits), 4);  // update credits
  write(fd, &(player.highscore), 4); // update highscore
  write(fd, &(player.name), 100);     // update name
  close(fd);
}

// This function will print all users
void show_all_users(){
  int fd, i, read_bytes;
  struct user entry;
  struct user users[5];

  fd = open(DATAFILE, O_RDONLY);
  if(fd == -1)
    fatal("in show_all_users() while opening file\n");

  i = 0;
  read_bytes = read(fd, &entry, sizeof(struct user));
  users[i++] = entry;
  while(read_bytes > 0){  
    read_bytes = read(fd, &entry, sizeof(struct user)); // keep reading
    users[i++] = entry;
  }

  for(int ndx=0; ndx < 2; ndx++){
     printf("User's name is %s, ID is %u\n", users[ndx].name, users[ndx].uid);
  }

}




// This function will display the current high score and
// the name of the person who set that high score
void show_highscore(){
  unsigned int top_score = 0;
  char top_name[100];
  struct user entry;
  int fd;

  printf("\n=======| HIGH SCORE |=======\n");
  fd = open(DATAFILE, O_RDONLY);
  if(fd == -1)
    fatal("in show_highscore() while opening file\n");
  while(read(fd, &entry, sizeof(struct user)) > 0){ // loop until the end of file
    if(entry.highscore > top_score){    // If there is a higher score
        top_score = entry.highscore;    // set top_score to that score
        strcpy(top_name, entry.name);   // and top_name to that username
    }

  }
  close(fd);
  if(top_score > player.highscore)
    printf("%s has the high score of %u credits!\n", top_name, top_score);
  else
    printf("You currently have the highscore of %u credies!\n", player.highscore);
  printf("====================\n");
}

// This function simply awards the jackpot for the Pick a Number game
void jackpot(){
  printf("*+*+*+*+*+ JACKPOT *+*+*+*+*+\n");
  printf("You have won the jackpot of 100 credits!\n");
  player.credits += 100;
}

// This function prints 3 cards for the Find the Ace game
// it expects a message to display, a pointer to the cards array
// and the card the user has picked as input. If the user_pick is
// -1, then the selection numbers are displayed
void print_cards(char * message, char * cards, int user_pick){
  int i;
  printf("\n\t*** %s ***\n", message);
  printf("\t._.\t._.\t._.\n");
  printf("Cards:\t|%c|\t|%c|\t|%c|\n\t", cards[0], cards[1], cards[2]);

  if(user_pick == -1)
    printf(" 1 \t 2 \t 3\n");
  else {
    for(i=0; i<user_pick; i++)
      printf("\t");
    printf(" ^ -- your pick\n");
  }
}

// This function inputs wagers for botyh the No Match Dealer and
// Find the Ace games. It expects the available credits and the 
// previous wager as arguments. The previous wager is only important
// for the second wager in the Find the Ace game. The function
// returns -1 if the wager is too big of too little, and it returns
// the wager amount otherwise.
int take_wager(int available_credits, int previous_wager){
  int wager, total_wager;
  printf("How many of your %d credits would you like to wager? ", available_credits);
  scanf("%d", &wager);
  if(wager < 1){  // Make sure the wager is gre`ater than 0
    printf("Nice try, but you must wager a positive number!\n");
    return -1;
  }
  total_wager = previous_wager + wager;
  if(total_wager > available_credits){  // confirm wavailable credits
    printf("Your total wager of %d is more than you have!\n", total_wager);
    printf("You only have %d available credits, try again.\n", available_credits);
    return -1;
  }
  return wager;
}

// This function contains a loop to allow the current game to be 
// played again. It also writes the new credit totals to file
// after each game is played
void  play_the_game(){
  int play_again = 1;
  int (*game)();
  char selection;
  char select[10];

  while(play_again){
    printf("\n[DEGUB] current_game pointer @ 0x%08x\n", player.current_game);
    if(player.current_game() != -1){    // If the game plays without error
      if(player.credits > player.highscore) // a new high score is set
        player.highscore = player.credits;
      printf("\nYou now have %u credits\n", player.credits);
      update_player_data();    // write the new new credit total to file
      printf("Would you like to play again? (y/n) ");
      selection = '\n';
      select[0] = '\n';
      while(select[0] == '\n'){
        scanf("%s", select);
      }
        
      printf("You chose: %s\n", select);

      if(select[0] == 'n')
        play_again = 0;

      // if(selection == 'n')
      //   play_again = 0;
    }
    else                // This means the game returned an error
      play_again = 0;   // so return to main menu
  }
}


// This function is the Pick a Number game
// It returns -1 if the player doesn't have enough credits
int pick_a_number(){
  int pick, winning_number;

  printf("\n####### Pick a Number Game #######\n");
  printf("This game costs 10 credits to play. Simply pick a number \n");
  printf("between 1 and 20, and if you pick the winning number, you\n");
  printf("will win the jackpot of 100 credits!\n\n");
  winning_number = (rand() % 20) + 1;   // Pick a number between 1 and 20
  if(player.credits < 10){
    printf("You only have %d credits. That's not enough to play!\n\n", player.credits);
    return -1;  // Not enough credits to play
  }
  player.credits -= 10; // deduct 10 credits
  printf("10 credits have been deducted from your account.\n");
  printf("Pick a number between 1 and 20: ");
  scanf("%d", &pick);
  if(pick == winning_number)
    jackpot();
  else
    printf("Sorry, you didn't win.\n");
  return 0;
}

// This is the No Match Dealer game.
// It returns -1 if the palyer has 0 credits
int dealer_no_match(){
  int i, j, numbers[16], wager = -1, match = -1;

  printf("\n::::::: No Match Dealer :::::::\n");
  printf("In this game, you can wager up to all of your credits.\n");
  printf("The dealer will deal out 16 random numbers between 0 and 99.\n");
  printf("If there are no matches among them, yhou double your money!\n\n");

  if(player.credits == 0){
    printf("You don't have any credits to wager!\n\n");
    return -1;
  }
  while(wager == -1)
    wager = take_wager(player.credits, 0); // loop while wager is -1

  printf("\n\n::: Dealing out 16 random numbers ::: ");
  for(i=0; i < 16; i++){
    numbers[i] = rand() % 100; // Pick a number between 0 and 99
    printf("%2d\t", numbers[i]);
    if(i%8 == 7)    // Print a line break every 8 numbers
      printf("\n");
  }
  for(i=0; i < 15; i++){  // Loop looking for matches
    j = i + 1;
    while(j < 16){
      if(numbers[i] == numbers[j])
        match = numbers[i];
      j++;
    }
  }
  if(match != -1){
    printf("The dealer matched the number %d!\n", match);
    printf("You lose %d credits.\n", wager);
    player.credits -= wager;
  } else {
    printf("There were no matches! You win %d credits!\n", wager);
    player.credits += wager;
  }
  return 0;
}

// This is the Find the Ace game
// It returns -1 if the player has 0 credits
int find_the_ace(){
  int i, ace, total_wager;
  int invalid_choice, pick = -1, wager_one = -1, wager_two = -1;
  char choice_two, cards[3] = {'X', 'X', 'X'};

  ace = rand() % 3; // Place the ace randomly

  printf("******* Find the Ace *******\n");
  printf("In this game, you wager up to all of your credits.\n");
  printf("Three cards will be dealt out, two queens and once ace.\n");
  printf("If you find the ace, you will win your wager.\n");
  printf("After choosing a card, one of the queens will be revealed.\n");
  printf("At this point, you may either selecte a different card or\n");
  printf("increase your wager.\n\n");

  if(player.credits == 0){
    printf("You don't have any credits to wager!\n\n");
    return -1;
  }

  while(wager_one == -1)  // loop until valid wager is made
    wager_one = take_wager(player.credits, 0);
  
  print_cards("Dealing cards", cards, -1);
  pick = -1;
  while((pick < 1) || (pick > 3)){    // Loop until valid pick is made.
    printf("Select a card: 1, 2, or 3 ");
    scanf("%d", &pick);
  }
  pick--;   // Adjust the pcik since card numbering starts at 0
  i=0;
  while(i == ace || i == pick)  // keep looping until
    i++;                        // we find a valid queen to reveal
  cards[i] = 'Q';
  print_cards("Revealing a queen", cards, pick);

  invalid_choice = 1;
  while(invalid_choice){
    printf("Would you like to: \n[c]hange your pick\tor\t[i]ncrease your wager?");
    printf("Select c or i: ");
    choice_two = '\n';

    while(choice_two == '\n')   // flush extra newlines
      scanf("%c", &choice_two);
    if(choice_two = 'i'){
      invalid_choice = 0;   // This is a valide choice
      while(wager_two == -1)  // Loop until valide second wager is made
        wager_two = take_wager(player.credits, wager_one);
    }

    if(choice_two = 'c'){     // Change pick
      i = invalid_choice = 0; // valid choice
      while(i == pick || cards[i] == 'Q') // Loop until the other card
        i++;                               // is found,
      pick = i;                            // and then swap pick
      printf("Your card pick has been changed to card %d\n", pick+1);
    }
  }

 //reveal cards
  for(i=0; i < 3; i++){
    if(ace == i)
      cards[i] = 'A';
    else
      cards[i] = 'Q';
  }
  print_cards("End result", cards, pick);

  if(pick == ace){  // Handle win
    printf("You have won %d credits from your first wager\n", wager_one);
    player.credits += wager_one;
    if(wager_two != -1){
      printf("and an additional %d credits from your second wager !\n", wager_two);
      player.credits += wager_two;
    }

  } else {
    printf("You have lost %d credis from your first wager\n", wager_one);
    player.credits -= wager_one;
    if(wager_two != -1){
      printf("and an additional %d credits from your second wager!\n", wager_two);
      player.credits -= wager_two;
    }
  }
  return 0;
}







