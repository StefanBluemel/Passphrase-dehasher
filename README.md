# Passphrase-dehasher
Dictionary attack tool for dehashing passwords composed of predictable combinations of natural language and salt values for ethical/educational purposes.


# Disclaimer
This tool was created as an educational research project. 

Dictonaries to use with this tool will not be directly provided by the author of this tool. 

Though some simple chatGPT queries are provided in the gptquery_templates.txt file to be used to create example data.

# Capabilities / how to use
This Tool currently mainly focuses on dehashing sha256 hashes. 

To focus on other hash technologies please modify the check_hash() function in the parse.py file in order to do so. This might be implemented in a future version be default.

The main script containing all functionallity is the parse.py script. In the current version it uses a hard coded global variable called "input_path" to determine which file to use as dictonary for either generating its own more extensive dictonary based on how frequently word combination patterns of various lengths are observed or to use to compare it with a target hash to crack.

Lets break this down a little:

We can take an Input Text file, analyze it on a line by line basis and then auto generate all kinds of new combinations of words based on the observed patterns in the original Input.
(This will work better if the Input is using only one language, preferably containing example phrases around the topic of password phrases, popular songs lyrics or movies quotes)

It is adviced to seperate this type of input from unrelated dictonaries that mainly focus on attack different behavior patterns.


Another capability of the Tool is to use a given Input Dictonary to compare its contents with a target hash.
This Tool currently supports either a range of Unit test hash Values or one specific main hash value.
Please check out the functions Unit_Test() and main_crack() in order to specify which hashes you want to crack

Feel free to try your luck at dehashing the currently configured hash value in the main_hash() function ;)

This tool is also capable of generating a clean output.txt file based on its Input that remove all redundant phrases that might have been created via ai 


# Documentation

A detailed Documentation of this project will be added at a later date.