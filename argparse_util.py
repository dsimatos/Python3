#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
argparse_util makes use of argparse standard library.
It asks the user for arguments to use in command line, 
and returns the code for parsing these command line arguments
'''
def main():
	aList = []
	
	# Creating a parser
	aList.append("import sys, argparse")
	
	ArgumentParserString = ""
	prog = input("Give prog - The name of the program (default: sys.argv[0]) : ")
	if prog:
		ArgumentParserString = "prog = '" + prog + "'"
	
	usage = input("Give usage - The string describing the program usage (default: generated from arguments added to parser) : ")
	if usage:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", usage = '" + usage + "'"
		else:
			ArgumentParserString = "usage = '" + usage + "'"
		
	description = input("Give description - Text to display before the argument help (default: none) \n \
If you want to refer to programs name use the %(prog)s format specifier \n \
Give description : ")
	if description:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", description = '" + description + "'"
		else:
			ArgumentParserString = "description = '" + description + "'"
			
	epilog = input("Give epilog - Text to display after the argument help (default: none) \n \
If you want to refer to programs name use the %(prog)s format specifier \n \
Give epilog : ")
	if epilog:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", epilog = '" + epilog + "'"
		else:
			ArgumentParserString = "epilog = '" + epilog + "'"
	
	parents = input("Give parents - A list of ArgumentParser objects whose arguments should also be included (default: void list) : ")
	if parents:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", parents = [" + parents + "]"
		else:
			ArgumentParserString = "parents = [" + parents + "]"
	
	formatter_class = input("Select a number for formatter_class - A class for customizing the help output \n \
1. HelpFormatter (default : line-wrap the description and epilog texts in command-line help messages) \n \
2. RawDescriptionHelpFormatter : description and epilog are already correctly formatted and should not \n \
   be line-wrapped \n \
3. RawTextHelpFormatter : maintains whitespace for all sorts of help text, including argument descriptions, \n \
   multiple newlines replaced by one \n \
4. ArgumentDefaultsHelpFormatter : automatically adds information about default values to each of the \n \
   argument help messages \n \
5. MetavarTypeHelpFormatter : uses the name of the type argument for each argument as the display name \n \
   for its values (rather than using the dest as the regular formatter does \n \
Give formatter class : ")
	if formatter_class == '1':
		formatter_class = 'argparse.HelpFormatter'
	elif formatter_class == '2':
		formatter_class = 'argparse.RawDescriptionHelpFormatter'
	elif formatter_class == '3':
		formatter_class = 'argparse.RawTextHelpFormatter'
	elif formatter_class == '4':
		formatter_class = 'argparse.ArgumentDefaultsHelpFormatter'
	elif formatter_class == '5':
		formatter_class = 'argparse.MetavarTypeHelpFormatter'
	else:
		formatter_class = ''
	if formatter_class:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", formatter_class = " + formatter_class
		else:
			ArgumentParserString = "formatter_class = " + formatter_class
	
	prefix_chars = input("Give prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘) : ")
	if prefix_chars:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", prefix_chars = '" + prefix_chars + "'"
		else:
			ArgumentParserString = "prefix_chars = '" + prefix_chars + "'"
	
	fromfile_prefix_chars = input("Give fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None) : ")
	if fromfile_prefix_chars:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", fromfile_prefix_chars = '" + fromfile_prefix_chars + "'"
		else:
			ArgumentParserString = "fromfile_prefix_chars = '" + fromfile_prefix_chars + "'"
	
	argument_default = input("Select argument_default - The global default value for arguments (default: None) \n \
1. argparse.SUPPRESS : to globally suppress attribute creation on parse_args() calls \n \
Give your choise : ")
	if argument_default == "1":
		argument_default = 'argparse.SUPPRESS'
	else:
		argument_default = ''
	if argument_default:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", argument_default = " + argument_default
		else:
			ArgumentParserString = "argument_default = " + argument_default
	
	conflict_handler = input("Select conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary) \n \
1. error (default) \n \
2. resolve : Sometimes (e.g. when using parents) it may be useful to simply override any older arguments with the same option string \n \
Give your choise : ")
	if conflict_handler == "1":
		conflict_handler = 'error'
	elif conflict_handler == "2":
		conflict_handler = 'resolve'
	else:
		conflict_handler = ''
	if conflict_handler:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", conflict_handler = " + conflict_handler
		else:
			ArgumentParserString = "conflict_handler = " + conflict_handler
	
	add_help = input("Give add_help - Add a -h/--help option to the parser (default: True) : ")
	if add_help:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", add_help = " + add_help
		else:
			ArgumentParserString = "add_help = " + add_help
	
	allow_abbrev = input("Give allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True) : ")
	if allow_abbrev:
		if ArgumentParserString:
			ArgumentParserString = ArgumentParserString + ", allow_abbrev = " + allow_abbrev
		else:
			ArgumentParserString = "allow_abbrev = " + allow_abbrev
	
	if ArgumentParserString:
		ArgumentParserString = "parser = argparse.ArgumentParser(" + ArgumentParserString + ")"
	else:
		ArgumentParserString = "parser = argparse.ArgumentParser()"

	aList.append(ArgumentParserString)
    
    # Add optional arguments
    aList = []
	for i in range(int(input("How many 'OPTIONAL' arguments do we have : "))):
		print("For the optional argument no ", i, sep = '', end = '')
		print(" give : ")
		
		name = ''
		while not name:
			name = input('name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo \n \
You may use prefix_chars you gave before. Separate names with a comma and a space \n \
Give your name or flags : ")
		name1 = [i.strip() for i in name.split(',')] # convert a string into list items without leading or trailing spaces
		name = ''
		for i in name1:
			name = name + "'" + i + "', "            # convert the list items into a comma separated name or flags string
		AddArgumentString = name[:-2]                # cut the last two characters
		
		action = input("Give action - The basic type of action to be taken when this argument is encountered at the command line")
		nargs = input("Give nargs - The number of command-line arguments that should be consumed")
		const = input("Give const - A constant value required by some action and nargs selections")
		default = input("Give default - The value produced if the argument is absent from the command line")
		type1 = input("Give type - The type to which the command-line argument should be converted")
		choices = input("Give choices - A container of the allowable values for the argument")
		required = input("Give required - Whether or not the command-line option may be omitted (optionals only)")
		help = input("Give help - A brief description of what the argument does")
		metavar = input("Give metavar - A name for the argument in usage messages")
		dest = input("Give dest - The name of the attribute to be added to the object returned by parse_args()")
		
		if AddArgumentString:
			AddArgumentString = "parser.add_argument(" + AddArgumentString +")"
			aList.append(AddArgumentString)
	
	# Add positional arguments
    aList = []
	for i in range(int(input("How many 'POSITIIONAL' arguments do we have : "))):
		AddArgumentString =''
		
		
		if AddArgumentString:
			AddArgumentString = "parser.add_argument(" + AddArgumentString +")"
			aList.append(AddArgumentString)
	
	# Add last line
	aList.append("args = parser.parse_args()")
	
	# Write everything in a file
	fname = input("Give NAME of the FILE to contain the parsing code you just described : ")
	with open(fname, "w") as f:
		for term in aList:
			f.write(term + "\n")
	print()
	print("You can find your parsing code in file : ", fname, sep = '')
	print()
	exit(0)

if __name__ == "__main__":
	main() 














