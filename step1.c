#include <stdio.h>
//the maximum possible string length(can be increased)
#define LINESIZE 200
int main(void){
	char file_name[LINESIZE]="";
	//Ask and take a  file-name for a reading from user
	printf("Name of the file\n");
	gets(file_name);
	// error checking
	if ( file_name!= NULL){
		FILE *myfile;
		char text[LINESIZE]="";
		// try to open the named file and error checking
		if((myfile = fopen(file_name,"r")) != NULL){
			printf("%s is open\n",file_name);
			// loop function to read the file
			while(1){
				// take one line from the file
				fgets(text,sizeof(text),myfile);
				   //checking if the line is exist
                                if(text[0]!='\0'){
                                        //  showing this line
                                        printf("%s",text ) ;
                                }

				 // checking if its a not final of the file
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
