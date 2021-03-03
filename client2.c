#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <netdb.h>

#define BUFFSIZE 5

char buffer[1024];
char board[10] = {'o','1','2','3','4','5','6','7','8','9'};

void show_board();
int check_win();
int cast(char pos);

void err_sys(char *mess) {
    perror(mess);
    exit(1);
}

char get_movement(int client) {
    recv(client, buffer, sizeof(buffer), 0);
    printf("The client says: %c\n", buffer);
    //string buf = buffer;
    memset(buffer, 0, sizeof(buffer));
    getchar();
    return buffer;
}

void send_movement(int server, char message) {
    buffer[0] = message;
    send(server, buffer, sizeof(buffer), 0);
    printf("Movement sent!\n");
    memset(buffer, 0, sizeof(buffer));
}

int main(int argc, char *argv[]) {
    struct sockaddr_in server;
    struct sockaddr *server_ptr;
    struct hostent *rem;
    unsigned int server_len;
    int sock, new_sock, result, i, choice;
    int address = atoi(argv[1]);
    int port = atoi(argv[2]);

    /*Check input arguments*/
    if (argc < 3){
       fprintf(stderr, "usage: %s <n> <port>\n", argv[0]);
       exit(0);
    }

    /*Create Socket*/
    sock = socket(PF_INET , SOCK_STREAM , IPPROTO_TCP);
    if (sock < 0) {
       err_sys("Error socket.");
    }

    /* Set information for sockaddr_in structure */
    //memset(&server, 0, server_len);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(argv[1]);
    //bcopy((char *) rem -> h_addr, (char *) &server.sin_addr, rem -> h_length);
    server.sin_port = htons(port);
    server_ptr = (struct sockaddr *) &server;
    server_len = sizeof server;

    result = connect(sock, server_ptr, server_len);
    if(result < 0) {
	err_sys("Error connect.");
    }

    printf("Connected to server!\n");

    char mark;

    /*Show board*/
    do{
       show_board();

       printf("It is your turn\n");
       printf("Please, choose an option (1-9)\n");
       scanf("%d", &choice);

       add_element('X', choice);

       send_movement(sock, choice);

       printf("Now it is the turn of the Server\n");
    }while(i == -1);
       show_board();
  return 0;
}

void show_board() {
   system("cls");
   printf("\n\n   Tic-Tac-Toe   \n\n");

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
        //player--;
        getchar();
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

