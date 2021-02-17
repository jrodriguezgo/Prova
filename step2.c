#include <stdio.h> 
#include <string.h>
//the maximum possible string length(can be increased)
#define LINESIZE 200
//the maximum possible name file length(can be increased)
#define NAMESIZE 50
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
					char text[LINESIZE]="";
					// loop function 
					while(1){
						// take one line from the file READ
                                        	fgets(text,sizeof(text),myfile);
						//checking if the line is exist
						if(text[0]!='\0'){
						    	// count of lines
                                                        i++;
                                                        // put one line to the file WRITE
                                                        fputs(text,myfiledest);
						}
						//checking if its a not final of the file  READ
						if(!feof(myfile)){
							//cleaning up of line 
							for(int ii=0;ii<LINESIZE;ii++){
                		                                text[ii]='\0';
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
//