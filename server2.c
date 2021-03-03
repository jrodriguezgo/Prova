#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <netdb.h>

#define MAXPENDING 5
#define BUFFSIZE 5

char buffer[1024];
char board[10] = {'o','1','2','3','4','5','6','7','8','9'};
//int choice;

void show_board();
int check_win();
int cast(char pos);

void err_sys(char *mess) {
    perror(mess);
    exit(1);
}

void handle_client(int sock) {
   char buffer[BUFFSIZE];
   int recieved = -1;
   while(1);
   close(sock);
}

char recieve_movement(int client) {
   recv(client, buffer, sizeof(buffer), 0);
   printf("The client says: %d\n", buffer[0]);
   memset(buffer, 0, sizeof(buffer));
   return buffer;
}

void set_movement(int client, char message) {
   buffer[0] = message;
   send(client, buffer, sizeof(buffer), 0);
   memset(buffer, 0, sizeof(buffer));
   printf("Movement sent!\n");
}

int main(int argc, char *argv[]){
   struct sockaddr_in server, client;
   struct sockaddr *server_ptr, *client_ptr;
   unsigned int server_len, client_len;
   char buffer[1024];
   int sock, new_sock, result, player = 1, i;
   int port = atoi(argv[1]);
   int choice;

   /*Check input arguments*/
   if (argc != 2){
      fprintf(stderr, "usage: %s <n> <port>\n", argv[0]);
      exit(1);
   }

   /*Create Socket*/
   sock = socket(PF_INET , SOCK_STREAM , IPPROTO_TCP);
   if (sock < 0) {
      err_sys("Error socket.");
   }

   /* Set information for sockaddr_in structure */
   server.sin_family = AF_INET;
   server.sin_addr.s_addr = htonl(INADDR_ANY);
   server.sin_port = htons(port);
   server_ptr = (struct sockaddr *) &server;
   server_len = sizeof server;

   /*Bind Socket*/
   result = bind(sock, server_ptr, server_len);
   if (result < 0) {
      err_sys("Error binding.");
   }

   /*Listen Socket*/
   result = listen(sock, MAXPENDING);
   if (result < 0) {
      err_sys("Error listen.");
   }

   printf("Connecting to port %d\n", port);

   client_ptr = (struct sockaddr *) &client;
   client_len = sizeof client;

   new_sock = accept(sock, NULL, NULL);
   if (new_sock < 0) {
      err_sys("Error accept");
   }

   printf("Client is connected!\n");
   char mark;

   /*Show board*/
   do{
      show_board();

      printf("It is the turn of the Client\n");
      //recieve_movement(new_sock);
      //choice = cast(mark);
      recv(new_sock, buffer, sizeof(buffer), 0);
      printf("The client says: %d\n", buffer[0]);
      //memset(buffer, 0, sizeof(buffer));

      printf("%d\n", buffer[0]);
      //choice = cast(buffer[0]);
      add_element('X', buffer[0]);

      printf("It is your turn\n");
      printf("Please, choose an option (1-9)\n");
      scanf("%d", &choice);
      add_element('O', choice);
      //player = (player % 2) ? 1 : 2;
   }while(i == -1);
      show_board();
   return 0;
}

void show_board() {
   system("cls");
   printf("\n\n     Tic-Tac-Toe Game\n\n");

   printf("     |     |      \n");
   printf("  %c  |  %c  |  %c  \n", board[1], board[2], board[3]);

   printf("_____|_____|_____ \n");
   printf("     |     |      \n");

   printf("  %c  |  %c  |  %c  \n", board[4], board[5], board[6]);

   printf("_____|_____|_____ \n");
   printf("     |     |      \n");

   printf("  %c  |  %c  |  %c  \n", board[7], board[8], board[9]);

   printf("     |     |       \n\n");
}

void add_element(char element, int choice) {
   if(choice == 1 && board[1] == '1')
	board[1] = element;
   else if(choice == 2 && board[2] == '2')
	board[2] = element;
   else if(choice == 3 && board[3] == '3')
	board[3] = element;
   else if(choice == 4 && board[4] == '4')
	board[4] = element;
   else if(choice == 5 && board[5] == '5')
	board[5] = element;
   else if(choice == 6 && board[6] == '6')
	board[6] = element;
   else if(choice == 7 && board[7] == '7')
	board[7] = element;
   else if(choice == 8 && board[8] == '8')
	board[8] = element;
   else if(choice == 9 && board[9] == '9')
	board[9] = element;
   else
	printf("Invalid move\n");
	getchar();
   show_board();
}

int cast(char pos) {
   int num;
   return num = (int)pos-48;
}

int check_win() {
   if(board[1] == board[2] && board[2] == board[3])
	return 1;
   else if(board[4] == board[5] && board[5] == board[6])
	return 1;
   else if(board[7] == board[8] && board[8] == board[9])
	return 1;
   else if(board[1] == board[4] && board[4] == board[7])
	return 1;
   else if(board[2] == board[5] && board[5] == board[8])
	return 1;
   else if(board[3] == board[6] && board[6] == board[9])
	return 1;
   else if(board[1] == board[5] && board[5] == board[9])
	return 1;
   else if(board[3] == board[5] && board[5] == board[7])
	return 1;
   else if(board[1] != '1' && board[2] != '2' && board[3] != '3' &&
	   board[4] != '4' && board[5] != '5' && board[6] != '6' &&
	   board[7] != '7' && board[8] != '8' && board[9] != '9')
	return 0;
   else
	return -1;
}


  // printf("\n");
   //int count = 0;
  // for(int i=0; i<9; i++) {
//      if(count == 3) {
//        printf("\n");
//        printf("\t\t%c", board[i], " ");
//        count = 1;
//      }else{
//        printf("\t\t%c", board[i], " ");
  //        count++;
//      }
   //}
 //  printf("\n\n");
   //handle_client(new_sock);


