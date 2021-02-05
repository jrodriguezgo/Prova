//
#include <stdio.h>
# include <string.h>
//the maximum possible string length(can be increased)
# define LINESIZE 200
//the maximum possible name file length(can be increased)
# define NAMESIZE 50
int main(void){
        printf("Copy a source file to a destination file\n");
         //Ask and take a  file-name for reading from user
	printf("Name of the u file\n");
        char file_name[NAMESIZE]="";
        gets(file_name);
	// error name cheking
        if ( file_name!= NULL){
                FILE *myfile;
		// try to open the named file for a reading and error checking
                if((myfile = fopen(file_name,"r")) != NULL){
			printf("%s is open\n",file_name);
                        char file_name_dest[NAMESIZE]="";
                        strncpy(file_name_dest,file_name ,NAMESIZE );
			// adding the suffix ".OUT" after the file name
                        strcat(file_name_dest,".OUT");
			// error name cheking
                        if( file_name_dest != NULL){
                                FILE *myfiledest;
				// try to open the named file for a writing and error checking
                                if((myfiledest = fopen(file_name_dest,"w"))!= NULL){
                                        int i = 0 ;
                                        char text[LINESIZE][LINESIZE];
					// loop function
					while(1){
						// take one line from the file READ
                                              	 fgets(text[i],sizeof(text[i]),myfile);
						 //checking if the line is exist
						 if(text[i][0]!='\0'){
							i++;
							//count of lines
						 }
						//checking if its a not final of the file  READ
						if(!feof(myfile)){
							//cleaning up of line
							for(int ii=0;ii<LINESIZE;ii++){
                		                        	text[i][ii]='\0';
		         	                        }
                                                }else{
							// exit from loop
                                                        break;
                                                }
                                        }

					int test =0 ;
					for(test=0;test<LINESIZE;test++){
						if(text[0][test]=='\0') {
							break;
						}
					}
					// put the last line to the file WRITE like a first line
					for (int ii=0;ii<LINESIZE;ii++){
						// checking if the last line had a line break ; if not we will add it
						if(text[i-1][ii]=='\0'){
							if(text[i-1][ii-1]!='\n'){
								text[i-1][ii]='\n';
								if(text[0][test-1]=='\n'){
									text[0][test-1]='\0';
								}
							}
							if(ii-2>=0){
								if(text[i-1][ii-2]!='\r'){
									if(text[0][test-2]=='\r'){
										text[0][test-2]='\0';
									}
								}
							}
							break;
						}
					}
					fputs(text[i-1],myfiledest);
					// put rest line to the file WRITE from second to penultimate
					for(int j=1;j<i-1;j++){
						fputs(text[j],myfiledest);
					}
					// checking if at the file READ was been more than 1 line
					if(i!=1){
						// put the first line to the file WRITE like a last line
						fputs(text[0],myfiledest);
					}
                                        printf("\nI copied %d lines from %s to %s\n",i,file_name,file_name_dest);
                                        fclose(myfiledest);
                                }else{
                                        printf("Error! Can't write at the file");
                                }
                        }else{
                                printf("Error! file_name_dest is NULL");
                        }
                        fclose(myfile);
                }else{
                        printf("File do not exist!\n");
                }
        }else{
                printf("Error! file_name is NULL");
        }
return 0 ;
}
