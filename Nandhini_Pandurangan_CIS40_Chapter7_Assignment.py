# CIS 40: Summer 2020: Chapter 7 Assignment: Nandhini Pandurangan
# This program reads a file containing text and the contents of
# the file is sent to the output file, preceded by line numbers


flag = True  # controls user input for file names
while flag:
    try:
        i_file_name = input("Please enter the name of the input file: ")
        o_file_name = input("Please enter the name of the output file: ")

        i_file = open(i_file_name, 'r')
        o_file = open(o_file_name, 'w')

        flag = False
    except IOError: # if the input file does not exist
        print("\nERROR: Please enter an existing input file name\n")

# reading the input line line by line and writing its contents
# to the output file
line_num = 1
for line in i_file:
    line = line.strip()

    line_info = str(line_num) + ") " + line + "\n"
    o_file.write(line_info)
    line_num += 1

print("\nSuccessfully written to file!")

o_file.close()
i_file.close()

"""
Output: 
Please enter the name of the input file: Rhymes.txt
Please enter the name of the output file: Rhymes_output.txt

Successfully written to file!
------------------------------------------------------------
Please enter the name of the input file: helloWorld.txt
Please enter the name of the output file: Rhymes_output.txt

ERROR: Please enter an existing input file name

Please enter the name of the input file: Rhymes.txt 
Please enter the name of the output file: Rhymes_output.txt

Successfully written to file!
"""
