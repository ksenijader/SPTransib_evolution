# encoding: utf8
import sys

def sequence_extraction(text_file,output_file):
    '''Method allowing to exctract BLAST alignment sequences from BLAST results file'''
    with open(text_file,"r") as file:
        with open(output_file,"w") as output:
            lines=file.readlines() #For each line in file
            for line in lines: #For each line in file
                if ">" in line:
                    sequence = line #Store the sequence ID
                    output.write(sequence) #Write the sequence ID in outout
                if "Range" in line: #If multiple ranges existe for given sequence ID
                    if "Range 1" not in line: #Unless it's the first range
                        output.write(sequence) #Repeat the sequence ID
                if "Sbjct" in line: #Sbjct line corresponds to BLAST hit sequence
                    linesplit= line.split("  ") #Split the line
                    newline= linesplit[2] #Store only the sequence
                    if " " in newline:
                        second= newline.split(" ")
                        output.write(second[1]+"\n") #Write the sequence
                    else:
                        output.write(newline+"\n")


argument=sys.argv #Creating a list to store the arguments passed by user

if __name__ == "__main__":
    # Input takes the value given by user after "-input"
    input_file=argument[argument.index("-input")+1]
    # Output takes the value given by user after "-output"
    file_output=argument[argument.index("-output")+1]
    #Execute the method that writes the outpus in a file provided by the user
    sequence_extraction(input_file,file_output)
