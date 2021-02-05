//
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//the maximum possible string length(can be increased)
#define LINESIZE 200
//the maximum possible name length(can be increased)
#define NAMESIZE 50
int main(void){
        printf("Copy a source file to a destination file\n");
        //Ask and take a  file-name for a reading from user
	printf("Name of the u file\n");
        char file_name[NAMESIZE]="";
        gets(file_name);
	// error checking
        if ( file_name!= NULL){
                FILE *myfile;
		 // try to open the named file for a reading and error checking
                if((myfile = fopen(file_name,"r")) != NULL){
			printf("%s is open\n",file_name);
                        char file_name_dest[NAMESIZE]="";
			strncpy(file_name_dest,file_name ,NAMESIZE );
			//adding the suffix ".OUT" after the file name
                        strcat(file_name_dest,".OUT");
                        if( file_name_dest != NULL){
                                FILE *myfiledest;
				 // try to open the named file for a writing and error checking
                                if((myfiledest = fopen(file_name_dest,"w"))!= NULL){
                                        int i = 0 ;
                                        char text[LINESIZE]="";
					char new_text[LINESIZE]="";
					// loop function
					while(1){
						 // take one line from the file READ
                                                fgets(new_text,sizeof(new_text),myfile);
						if(new_text[0]!='\0'){
                                                        //loop for checking each character in a string
                                                        for(int i=1;i<sizeof(new_text);i++){
                                                                // its a final of line
                                                                if(new_text[i]=='\0'){
                                                                        //checking if we will pass to the next line
                                                                        if(new_text[i-1]=='\n'){
										//checking if we will not fall below zero
										if(i-2>=0){
                                                                                	//counter exception <CR>
                                                                               		if(new_text[i-2]=='\r') {
												sprintf(text,"%d",i-2);
                                                                                        	// exit from loop FOR
                                                                                        	break;
                                                                                	}
                                                                        	}
                                                                        	sprintf(text,"%d",i-1);
                                                                        	// exit from loop FOR
                                                                        	break;
									}
									//exit from loop FOR
									sprintf(text,"%d",i);
									break;
                                                                }
                                                        }
                                                        strcat(text,") ");
                                                        strcat(text,new_text);
                                                        i++;
                                                        fputs(text,myfiledest);
						}
						 //checking if its a not final of the file  READ
                                                if(!feof(myfile)){
							//cleaning up of line 
							for(int ii=0;ii<LINESIZE;ii++){
		                                                text[ii]='\0';
								new_text[ii]='\0';
                		                        }
                                                }else{
							// exit from loop
                                                        break;
                                                }
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

