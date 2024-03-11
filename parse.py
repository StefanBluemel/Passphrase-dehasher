#import sys
import hashlib
import os
import time
from collections import defaultdict
#input_data = sys.stdin.read()

#Output File path
file_path = "output.txt"
file_path2 = "removed_phrases.txt"
file_path3 = "newly_generated_phrases.txt"

#Input
input_path = "test3.txt"

# Open the file in write mode and reset its content
with open(file_path, 'w') as file:
    file.write("")
with open(file_path2, 'w') as file2:
    file2.write("") 
with open(file_path3, 'w') as file3:
    file3.write("") 

word_frequency = defaultdict(int)  # Store word frequencies
#word_starts_sentence = defaultdict(int)  # Store words that start sentences 
word_starts_sentence = defaultdict(lambda: defaultdict(int)) # Store a combination of 2 words that start sentences
word_ends_sentence = defaultdict(int)
word_follows2 = defaultdict(lambda: defaultdict(int))  # Store words that follow other words
word_follows3 = defaultdict(lambda: defaultdict(int))  # Store words that follow other words
word_follows4 = defaultdict(lambda: defaultdict(int))  # Store words that follow other words
word_follows5 = defaultdict(lambda: defaultdict(int))  # Store words that follow other words
word_follows6 = defaultdict(lambda: defaultdict(int))  # Store words that follow other words


def clear_console():
    #windows
    if os.name == 'nt':
        _ = os.system('cls')

    # For Linux/MacOS
    else:
        _ = os.system('clear')

def check_hash(string, example_hash,Test):
    hashed_string = hashlib.sha256(string.encode()).hexdigest()
    if hashed_string == example_hash:
        if Test == False:
            print(f"The hashed value of '{string}' matches the example hash: {example_hash}")
        return True
    else:
        return False
    
def check_variant_hashes(char,string,example_hash,Test):
    if check_hash(string.replace('\'re',' are').replace(char,''),example_hash,Test):
        return True
    elif check_hash(string.replace('\'re',' are').replace(char,'').lower(),example_hash,Test): #all lowercase
        return True
    elif check_hash(string.replace('\'re',' are').replace(char,'').upper(),example_hash,Test): #all uppercase
        return True
    elif check_hash((string[0:1].upper() + string[1:].lower()).replace('\'re',' are').replace(char,''),example_hash,Test): #only first char uppercase
        return True
    else:
        return False
    
def check_complex_variant_hashes(char, char2, string,example_hash,Test):
    if check_hash(string.replace(char,'').replace(char2,''),example_hash,Test):
        return True
    elif check_hash(string.replace(char,'').replace(char2,'').lower(),example_hash,Test): #all lowercase
        return True
    elif check_hash(string.replace(char,'').replace(char2,'').upper(),example_hash,Test): #all uppercase
        return True
    elif check_hash(string.replace('\'re',' are').replace(char,'').replace(char2,'').upper(),example_hash,Test): #all uppercase
        return True
    elif check_hash((string[0:1].upper() + string[1:].lower()).replace(char,'').replace(char2,''),example_hash,Test): #only first char uppercase
        return True
    else:
        return False    
    
def delta_time():
    # Get the current time
    current_time = time.time()

    # Retrieve the last execution time from the global scope
    global last_execution_time

    # Calculate the delta time since the last execution
    if 'last_execution_time' in globals():
        delta = current_time - last_execution_time
    else:
        delta = None

    # Update the last execution time
    last_execution_time = current_time

    return delta

def process_all_hash_cases(string,example_hash,Test):
    # Compare the hashed string with the example value
    if check_hash(string,example_hash,Test):
        return True
    if check_hash(string.lower(),example_hash,Test):
        return True
    if check_hash(string.upper(),example_hash,Test):
        return True
    if check_hash(string[0:1].upper() + string[1:].lower(),example_hash,Test):
        return True
    
    #replace('ssword','$$word')
    if check_hash(string.replace('ssword','$$word'),example_hash,Test):
        return True
    if check_hash(string.replace('ssword','$$word').lower(),example_hash,Test):
        return True
    if check_hash(string.replace('ssword','$$word').upper(),example_hash,Test):
        return True
    if check_hash((string[0:1].upper() + string[1:].lower()).replace('ssword','$$word'),example_hash,Test):
        return True
    
    #most special chars deleted 
    if check_hash(string.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    if check_hash(string.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').lower(),example_hash,Test):
        return True
    if check_hash(string.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').upper(),example_hash,Test):
        return True
    if check_hash((string[0:1].upper() + string[1:].lower()).replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    
    #most special chars deleted 
    if check_hash(string.replace('it\'s',' it is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    if check_hash(string.replace('it\'s',' it is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').lower(),example_hash,Test):
        return True
    if check_hash(string.replace('it\'s',' it is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').upper(),example_hash,Test):
        return True
    if check_hash((string[0:1].upper() + string[1:].lower()).replace('it\'s',' it is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    
    #most special chars deleted 
    if check_hash(string.replace('it\'s',' is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    if check_hash(string.replace('it\'s',' is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').lower(),example_hash,Test):
        return True
    if check_hash(string.replace('it\'s',' is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').upper(),example_hash,Test):
        return True
    if check_hash((string[0:1].upper() + string[1:].lower()).replace('it\'s',' is').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    
    #most special chars deleted except space
    if check_hash(string.replace('\'re',' are').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    if check_hash(string.replace('\'re',' are').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').lower(),example_hash,Test):
        return True
    if check_hash(string.replace('\'re',' are').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#','').upper(),example_hash,Test):
        return True
    if check_hash((string[0:1].upper() + string[1:].lower()).replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','').replace('#',''),example_hash,Test):
        return True
    
    #most special chars deleted and .replace('ssword','$$word')
    if check_hash(string.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('ssword','$$word').replace('?',''),example_hash,Test):
        return True
    if check_hash(string.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('ssword','$$word').replace('?','').lower(),example_hash,Test):
        return True
    if check_hash(string.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('?','').replace('ssword','$$word').upper(),example_hash,Test):
        return True
    if check_hash((string[0:1].upper() + string[1:].lower()).replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('?','').replace('ssword','$$word'),example_hash,Test):
        return True

    
    #first letter of each word uppercase and most special chars deleted and .replace('ssword','$$word')
    words = string.split(" ")
    string2 = ""
    for x in words:
        string2 += x[0:1].upper() + x[1:].lower() + " "
    string2 = string2.strip()
    #print(string2.replace('\'re',' are').replace(' ','') == "YetAnotherPassword")
    if check_hash(string2,example_hash,Test):
        return True
    if check_hash(string2.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('?',''),example_hash,Test):
        return True
    if check_hash(string2.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('?','').lower(),example_hash,Test):
        return True
    if check_hash(string2.replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('?','').upper(),example_hash,Test):
        return True
    if check_hash((string2[0:1].upper() + string2[1:].lower()).replace('\'re',' are').replace(' ','').replace('\'','').replace(',','').replace('.','').replace('!','').replace(':','').replace(';','').replace('#','').replace('?',''),example_hash,Test):
        return True
    
    #remove only one specific special character
    elif check_variant_hashes(' ',string,example_hash,Test): #remove space character
        return True
    elif check_variant_hashes('\'',string,example_hash,Test): #remove ' character
        return True
    elif check_variant_hashes(',',string,example_hash,Test): #remove , character
        return True
    elif check_variant_hashes('!',string,example_hash,Test): #remove , character
        return True
    elif check_variant_hashes('?',string,example_hash,Test): #remove , character
        return True
    elif check_variant_hashes('.',string,example_hash,Test): #remove , character
        return True
    elif check_variant_hashes(':',string,example_hash,Test): #remove , character
        return True
    elif check_variant_hashes(';',string,example_hash,Test): #remove , character
        return True
    
    #remove various combinations of two special characters from test data
    elif check_complex_variant_hashes(' ','\'',string,example_hash,Test): #remove ' and space characters
        return True
    elif check_complex_variant_hashes(' ',',',string,example_hash,Test): #remove , and space characters
        return True
    elif check_complex_variant_hashes(',','\'',string,example_hash,Test): #remove ' and , characters
        return True
    #?
    elif check_complex_variant_hashes('?','\'',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('?',',',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('?',' ',string,example_hash,Test): 
        return True
    #!
    elif check_complex_variant_hashes('!','\'',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('!',',',string,example_hash,Test):
        return True
    elif check_complex_variant_hashes('!',' ',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('!','?',string,example_hash,Test): 
        return True
    #.
    elif check_complex_variant_hashes('.','\'',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('.',',',string,example_hash,Test):
        return True
    elif check_complex_variant_hashes('.',' ',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('.','?',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('.','!',string,example_hash,Test): 
        return True
    #:
    elif check_complex_variant_hashes(':','\'',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(':',',',string,example_hash,Test):
        return True
    elif check_complex_variant_hashes(':',' ',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(':','?',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(':','!',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(':','.',string,example_hash,Test): 
        return True
    #;
    elif check_complex_variant_hashes(';','\'',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(';',',',string,example_hash,Test):
        return True
    elif check_complex_variant_hashes(';',' ',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(';','?',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(';','!',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(';','.',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes(';',':',string,example_hash,Test): 
        return True
    ##
    elif check_complex_variant_hashes('#','\'',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('#',',',string,example_hash,Test):
        return True
    elif check_complex_variant_hashes('#',' ',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('#','?',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('#','!',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('#','.',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('#',':',string,example_hash,Test): 
        return True
    elif check_complex_variant_hashes('#',';',string,example_hash,Test): 
        return True
    else:
        return False 

def create_testhash(test):
    test
    print(test,'Sha256 hash:')
    print(hashlib.sha256(test.encode()).hexdigest())
        
def ooooooooold_generate_passphrases(words_starting_sentences):
    count_phrases = 0
    creationlimit = 10000
    #"guessing this password is not possible due to its complexity"

    for T1, T2s in words_starting_sentences:
        #print("T1: ",T1)
        #print("T2s: ",T2s)
        for T2 in T2s:
            #print("T2:",T2)
            for followsT2 in word_follows3[T1,T2]:
                #if countT5 > T5creationlimit:
                    #break
                for followsT3 in word_follows4[T1,T2,followsT2]:
                    if followsT3 not in (T1 + " " + followsT2):
                        for followsT4 in word_follows3[followsT2,followsT3]:
                            if followsT4 not in (T1 + " " + followsT2 + " " + followsT3):        
                                for followsT5 in word_follows3[followsT3,followsT4]:
                                    x = ""
                                    x += T1 + " " + T2 + " " + followsT2 + " " + followsT3 + " " + followsT4 + " " + followsT5
                                    if followsT5 not in  (T1 + " " + T2 + " " + followsT2 + " " + followsT3 + " " + followsT4):
                                        for followsT6 in word_follows4[followsT3,followsT4,followsT5]:
                                            for followsT7 in word_follows5[followsT3,followsT4,followsT5,followsT6]:
                                                for followsT8 in word_follows6[followsT3,followsT4,followsT5,followsT6,followsT7]:
                                                    for followsT9 in word_follows3[followsT7,followsT8]:
                                                        for followsT10 in word_follows6[followsT5,followsT6,followsT7,followsT8,followsT9]:
                                                            for followsT11 in word_follows6[followsT6,followsT7,followsT8,followsT9,followsT10]:
                                                                for followsT12 in word_follows6[followsT7,followsT8,followsT9,followsT10,followsT11]:
                                                                    y = ""
                                                                    y += x + " " + followsT6 + " " + followsT7 + " " + followsT8 + " " + followsT9 + " " + followsT10 + " " + followsT11 + " " + followsT12
                                                                    print(y)
                                                                    with open(file_path3, 'a') as file3:
                                                                        file3.write(y + '\n') 
                                                                        #file3.write('"' + y + '", ')        

def main_crack(): #this is the most important hash if this crack succeeds the entire project is a success
    example_hash = "e7b20d98d9f56097fe28ab222d22ea67c07fc461a4fde676463f859aa7ebea69" #this is what we want to crack
    if crack_hash(example_hash,False) == False:
        print("No Success at main hash crack :(")
        print("")
    else:
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")
        print("---------- Success !!! ----------")

def redundancy_check(string):
    #find redundant sentences

    input_text2 = input_data
    # Remove leading and trailing double quotes
    input_text2 = input_text2.strip('"')
    # Split the input text by ", " to separate each string
    strings2 = input_text2.split('", "')
    counter = 0
    mysentences = string
    copy = ""
    for sentence in strings2:
        if mysentences in sentence:
            counter += 1 #redundancy found
            if copy == sentence:
                counter -= 10000 #redundancy found but its harder to remove as at least one copy should remain
            copy = mysentences
        if counter > 1:
            break

    #no redundancy rewrite
    if counter <= 1 and counter >= 0:
        with open(file_path, 'a') as file:
            #file.write(mysentences + '\n') 
            file.write('"' + mysentences + '", ')

    #partial redundancy rewrite
    if counter <= -5000:
        with open(file_path2, 'r') as input2:
            sentences3 = input2.read().splitlines()
            counter2 = 0
            for sen in sentences3:
                if mysentences in sen:
                    counter2 += 1
                    #print(sen)
            if counter2 == 0:
                with open(file_path, 'a') as file:
                    file.write('"' + mysentences + '", ')
                    #file.write(mysentences + '\n') 
                with open(file_path2, 'a') as file2:
                    #file2.write('"' + mysentences + '", ')
                    file2.write(mysentences + '\n') 

def T5_analysis(words,tier5_arr):
    if words:
        if len(words) >= 5:
            n = len(tier5_arr)
            dontadd = False
            for tier5 in tier5_arr:
                if words[0:5] == tier5:
                    dontadd = True
            if dontadd == False:
                word_starts_sentence[words[0]][words[1]] += 1
                last_couple_words = " ".join(words[-4:])  # Get the last couple of words as a string
                #print(last_couple_words)
                word_ends_sentence[last_couple_words] += 1  # Increment the count for the last couple of words
                x_ = [words[0], words[1], words[2] , words[3] , words[4]]
                if(n < 3):
                    tier5_arr.append(x_)
                    #print("a---------------------------------------------------------------------------------------------------------------" , x_)
                    #print("words",words)
                else:
                    tier5_arr = [tier5_arr[1],tier5_arr[2],x_]
                    #print("")
                    #print("---------------------------------------------------------------------------------------------------------------" , x_)
                    #print("words",words)
                    #print(tier5_arr)
                    #print("----")
                    #print("")
                #print(x_)
                #print(tier5_arr)
    return tier5_arr

def T7_analysis(words,tier7_arr):
    if words:
        if len(words) >= 7:
            n = len(tier7_arr)
            dontadd = False
            for tier7 in tier7_arr:
                if words[0:7] == tier7:
                    dontadd = True
            if dontadd == False:
                x_ = [words[0], words[1], words[2] , words[3] , words[4] , words[5] , words[6]]
                if(n < 3):
                    tier7_arr.append(x_)
                    #print("a---------------------------------------------------------------------------------------------------------------" , x_)
                    #print("words",words)
                else:
                    tier7_arr = [tier7_arr[1],tier7_arr[2],x_]
                    #print("b---------------------------------------------------------------------------------------------------------------" , x_)
                    #print("words",words)
                #print(x_)
                #print(tier7_arr)
    return tier7_arr

def analysis():
     with open(input_path, 'r') as file:
        # Iterate over each line in the file
            print("Phase A")
            for string in file:
                sentence = string.strip()

                # Tokenization and frequency counting   
   
                sentence = sentence.replace(",","").replace(".","").replace(":","").replace(";","").replace("!","").replace("?","").replace("-","")
                words = sentence.split()
                # Update word frequency counts
                for word in words:
                    word_frequency[word] += 1

                # Update words that start sentences
                T5_analysis(words,[])

                # Update words that follow other words
                if len(words) > 2:
                    for i in range(len(words) - 1):
                        word_follows2[words[i]][words[i + 1]] += 1
                    for i in range(len(words) - 2):  # Changed to len(words) - 2 for three-word sequences
                        word_follows3[(words[i], words[i + 1])][words[i + 2]] += 1  # Use a tuple for three-word sequences
                if len(words) > 3:
                    for i in range(len(words) - 3):  # Changed to len(words) - 2 for four-word sequences
                        word_follows4[(words[i], words[i + 1], words[i + 2])][words[i + 3]] += 1  # Use a tuple for four-word sequences
                if len(words) > 4:
                    for i in range(len(words) - 4):  # Changed to len(words) - 2 for four-word sequences
                        word_follows5[(words[i], words[i + 1], words[i + 2], words[i + 3])][words[i + 4]] += 1  # Use a tuple for five-word sequences
                if len(words) > 5:
                    for i in range(len(words) - 5):  # Changed to len(words) - 2 for four-word sequences
                        word_follows6[(words[i], words[i + 1], words[i + 2], words[i + 3], words[i + 4])][words[i + 5]] += 1  # Use a tuple for six-word sequences

            # Example analysis
            most_frequent_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:30]
            #words_starting_sentences = sorted(word_starts_sentence.items(), key=lambda x: x[1], reverse=True)[:70]
            words_starting_sentences = sorted(word_starts_sentence.items(), 
                                        key=lambda x: sum(x[1].values()), 
                                        reverse=True)[:70]

            #print(word_follows3["my", "nth"])
            # for x in word_follows3["my", "nth"]:
                #    print(x)
            
            if True:
                #print(word_ends_sentence)
                generate_passphrases(words_starting_sentences,word_ends_sentence)

                  

            # Output analysis results
            #print("Top 30 frequent words:")
            #print(most_frequent_words)
            #print("")
            #print("number of unique words")
            #print(len(word_frequency.items()))
            #print("")
            if False: # DEPRECATED
                print("Top 70 Word combination that start sentences (tier 5 uniqueness):")
                #print(words_starting_sentences)
                for word, word2 in words_starting_sentences:
                    print(word,word2)
                #print(word_frequency["is"])
                print("")
                print("")
                print("")
                print("Word following frequencies level 2:")
                count = 0
                for word, follows in word_follows2.items():
                    print(word, ':\n', follows)
                    print("----")
                    count += 1
                    if count == 8:
                        break
                
                count = 0
                print("")
                print("")
                print("")
                print("Word following frequencies level 3:")
                for word, follows in word_follows3.items():
                    print(word, "----", follows)
                    print("----")
                    count += 1
                    if count == 8:
                        break


                #print("------")
                
                #for follows in word_follows2["security"]:
                    #print("T2:", follows)
                    #for word2, follows2 in word_follows2["security", follows]:
                        #print("T3:     ",word2, follows2)
            
def generate_passphrases(words_starting_sentences,word_ends_sentence):

    T4_arr = []
    count_phrases = 0
    creationlimit = 10000000

    for T1, T2s in words_starting_sentences:
        for T2 in T2s:
            for followsT2 in word_follows3[T1,T2]:
                x = ""
                x += T1 + " " + T2 + " " + followsT2
                for followsT3 in word_follows4[T1,T2,followsT2]:
                    if followsT3 != T1 and followsT3 != T2 and followsT3 != followsT2:
                        y = x + " " + followsT3
                        if y not in T4_arr:
                            T4_arr.append(y)

    print("length of T4 combinations: ", len(T4_arr))
    print(T4_arr[0])
    #print(T4_arr)

    newarr = T4_arr[:]

    for i in range(6):
        #print("i = ", i)
        newarr,count_phrases = AddT3depth(newarr,count_phrases, creationlimit,word_ends_sentence)
    print("T3 length of newarr combinations: ", len(newarr))
    print(newarr[0])
    
    for i in range(3):
        #print("i = ", i)
        newarr,count_phrases = AddT4depth(newarr,count_phrases, creationlimit,word_ends_sentence)
    print("T4 length of newarr combinations: ", len(newarr))
    print(newarr[0])


    for i in range(3):
        #print("i = ", i)
        print("T5 length of newarr combinations: ", len(newarr))
        if len(newarr) > 0:
            print(newarr[0])
            newarr,count_phrases = AddT5depth(newarr,count_phrases, creationlimit,word_ends_sentence)
        else:
            print("newarr is empty")
    


    for i in range(20):
        #print("i = ", i)
        print("T6 length of newarr combinations: ", len(newarr))
        if len(newarr) > 0:
            print(newarr[0])
            newarr,count_phrases = AddT6depth(newarr,count_phrases, creationlimit,word_ends_sentence)
        else:
            print("newarr is empty")
            
      
def AddT2depth(arr, count_phrases, creationlimit,word_ends_sentence):
    #print(arr)
    words_arr = []
    for string1 in arr:
        if count_phrases > creationlimit:
            print("reached creationlimit")
            break
        #print(string1)
        words = string1.split(" ")
        #print(words)
        n = len(words)
        if n > 3:
            for T2 in word_follows2[words[n-1]]:
                if count_phrases > creationlimit:
                    print("reached creationlimit")
                    break
                if T2 not in words:
                    #print(words)
                    words2 = " ".join(words[:])
                    words2 += " " + T2
                    #print(words2)
                    words_arr.append(words2)
    #print(words_arr)
    return words_arr,count_phrases      

def AddT3depth(arr, count_phrases, creationlimit,word_ends_sentence):
    #print(arr)
    words_arr = []
    for string1 in arr:
        if count_phrases > creationlimit:
            print("reached creationlimit")
            break
        #print(string1)
        words = string1.split(" ")
        #print(words)
        n = len(words)
        if n > 3:
            for T3 in word_follows3[words[n-2],words[n-1]]:
                if count_phrases > creationlimit:
                    print("reached creationlimit")
                    break
                if T3 not in words:
                    #print(words)
                    words2 = " ".join(words[:])
                    words2 += " " + T3
                    #print(words2)
                    words_arr.append(words2)
    #print(words_arr)
    return words_arr,count_phrases

def AddT4depth(arr, count_phrases, creationlimit,word_ends_sentence):
    #print(arr)
    words_arr = []
    for string1 in arr:
        if count_phrases > creationlimit:
            print("reached creationlimit")
            break
        #print(string1)
        words = string1.split(" ")
        #print(words)
        n = len(words)
        if n > 4:
            for T4 in word_follows4[words[n-3],words[n-2],words[n-1]]:
                if count_phrases > creationlimit:
                    print("reached creationlimit")
                    break
                if T4 not in words:
                    #print(words)
                    words2 = " ".join(words[:])
                    words2 += " " + T4
                    #print(words2)
                    words_arr.append(words2)
    #print(words_arr)
    return words_arr,count_phrases

def AddT5depth(arr, count_phrases, creationlimit,word_ends_sentence):
    print("count_phrases: ", count_phrases)
    #print(arr)
    words_arr = []
    for string1 in arr:
        if count_phrases > creationlimit:
            print("reached creationlimit")
            break
        #print(string1)
        words = string1.split(" ")
        #print(words)
        n = len(words)
        if n > 5:
            for T5 in word_follows5[words[n-4],words[n-3],words[n-2],words[n-1]]:
                if count_phrases > creationlimit:
                    print("reached creationlimit")
                    break
                if T5 not in words:
                    #print(words)
                    words2 = " ".join(words[:])
                    words2 += " " + T5

                    breakout = False
                    words3 = words2.split(" ")
                    last_couple_words = " ".join(words3[-4:])  # Get the last couple of words as a string
                    for lastwords in word_ends_sentence:
                        if last_couple_words == lastwords:
                            with open(file_path3, 'a') as file3:
                                #print("lastwords & last_couple_words",lastwords,"\n",last_couple_words)
                                file3.write(words2 + '\n') 
                                #file3.write('"' + words2 + '", ')
                            breakout = True
                            count_phrases += 1
                            break
                    if not breakout:
                        words_arr.append(words2)
                    #print(words2)
    #print(words_arr)
    return words_arr,count_phrases

def AddT6depth(arr, count_phrases, creationlimit,word_ends_sentence):
    print("count_phrases: ", count_phrases)
    #print(arr)
    words_arr = []
    for string1 in arr:
        if count_phrases > creationlimit:
            print("reached creationlimit")
            break
        #print(string1)
        words = string1.split(" ")
        #print(words)
        n = len(words)
        if n > 6:
            for T6 in word_follows6[words[n-5],words[n-4],words[n-3],words[n-2],words[n-1]]:
                if count_phrases > creationlimit:
                    print("reached creationlimit")
                    break
                if T6 not in words:
                    #print(words)
                    words2 = " ".join(words[:])
                    words2 += " " + T6
                    
                    breakout = False
                    words3 = words2.split(" ")
                    last_couple_words = " ".join(words3[-4:])  # Get the last couple of words as a string
                    for lastwords in word_ends_sentence:
                        if last_couple_words == lastwords:
                            with open(file_path3, 'a') as file3:
                                file3.write(words2 + '\n') 
                                #file3.write('"' + words2 + '", ')
                            breakout = True
                            count_phrases += 1
                            break
                        #print(words2)
                        #print("lastwords: ", lastwords,"\n","last_couple_words: ",last_couple_words)
                    if not breakout:
                        words_arr.append(words2)
    #print(words_arr)
    return words_arr,count_phrases
   
def convert_input_format():
    with open(input_path, 'r') as file:
        # Iterate over each line in the file
            print("Phase A")
            for string in file:
                sentence = string.strip()
                with open(file_path, 'a') as file:
                    file.write(string + '\n') 
                    #file.write('"' + mysentences + '", ')
        
def Unit_Test():    
    success_count = 0
    fail_count = 0
    Testcount = 1

    #------------------------1
                                                                                #Input "Yet Another Pass'word"
    example_hash = "8837cfd5caeff105b5fd442cf78867139b49f5b952c16755a5ed777737cd76ea" #"Yet Another Password"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #------------------------2

                                                                                #Input "Yet Another Pass'word"
    example_hash = "86c6dec9fc9647a6e9aea892f07f6466747cc66a0fc3be194da9de4c3c08a605" #"YetAnotherPassword"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #------------------------3

                                                                                #Input "Yet Another Pass'word"
    example_hash = "6f3ef313e829071baf1bf714b618b43ff8b27edd3761f72a348a8556a72af1ce" #"yetanotherpassword"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #------------------------4

                                                                                #Input "Yet Another Pass'word"
    example_hash = "58743e09856db930b3c5ff0bc3c6bdb42d5ee718c8697e84746fb2b42434c81e" #"YETANOTHERPASSWORD"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #------------------------5
                                                                               # Input "Thisisas'ecurepass?!word    'reyoubraveenoughtohackit"
    example_hash = "9106ccbec6a4481cca14a615caeee791000a9a698a8d164709cb79233cb31460" #"Thisisasecurepasswordareyoubraveenoughtohackit"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #------------------------6

                                                                                #Input "Yet Another Pass'word"
    example_hash = "ab4c64bff657e106de9fecc2ce3f614290c71c7669ba94da9e9a7f22e8e65b78" #"YETANOTHERPA$$WORD"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #------------------------7
                                                                                  
                                                                                #Input "Yet Another Pass'word"
    example_hash = "ab4c64bff657e106de9fecc2ce3f614290c71c7669ba94da9e9a7f22e8e65b78" #"YETANOTHERPA$$WORD"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #-------------------------8
                                                                                #Input "This is a secure password good luck trying to guess it"
    example_hash = "95d31a77d733f24a9533116f5a5786831604c51a4b721cb5efe4ac8e53ae7468" #"This is a secure password"
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #-------------------------9 
                                                                                #Input "This needs to be brute forced"
    example_hash = "2234931c6414ef67a391d93eddad70ac43f66c1599193cba1f800289588d0b97" #test123ihatethis
    if crack_hash(example_hash,True) == False:
        print("Unit Test " , Testcount , " --- FAIL!")
        fail_count += 1
    else:
        print("Unit Test " , Testcount , " --- OK!")
        success_count += 1
    Testcount += 1

    #-------------------------10

def crack_hash(example_hash,Test):
    # Process the input data
    if False:
        if input_data:
            #print("Input data received:", input_data)
            # Input text
            input_text = input_data
            # Remove leading and trailing double quotes
            input_text = input_text.strip('"')
            # Split the input text by ", " to separate each string
            strings = input_text.split('", "')

    progress_count = 0
    word_count = 0
    sum_of_phrases = 0
    delta_time() #init

    #change to True if you want to priortize exact matches with your Input file instead of iterating through partial lengths that iterate through all word combinations
    if False:
        with open(input_path, 'r') as file:
        # Iterate over each line in the file
            print("Phase A")
            for string in file:
                string = string.strip()
                #if "This is a secure password good luck trying to guess it" == string.strip():
                    #print(string)
                #print(string)
                # Process each line
                #print(string.strip())
                #Plan A - less resource intense
                #for string in strings:


                progress_count += 1
                #n = len(strings)
                if progress_count%1000 == 0:
                    print("Phase A progress: ", progress_count)
                    print("---------------------------------------------------delta",round(delta_time(),4)*1000,"ms") 

                #searches for redundancy and creates an output.txt file without them
                #the removed parts are marked in output2.txt
                if(Test == False):
                    redundancy_check(string)


                words = string.split(' ')
                #print(words)
                word_count += len(words)
                sum_of_phrases += 1
                if process_all_hash_cases(string,example_hash,Test):
                    return True

    #----------------------------------------#
                

    tier5_arr = []
    tier7_arr = []
    tier9_arr = []
    tier11_arr = []

    t5_red_delta = 0
    t7_red_delta = 0
    t5_delta = 0
    t7_delta = 0
    t20_delta = 0
    other_delta = 0
    anal5_delta = 0
    anal7_delta = 0

    #iterate through partial lengths through all word combinations until full length
    with open(input_path, 'r') as file:
    # Iterate over each line in the file
        print("Phase B")
        progress_count = 0
        for string in file:

            string = string.strip()
            words = string.split(' ')
            progress_count += 1
            #n = len(strings)

            if progress_count%1000 == 0:
                other_delta += delta_time()

                total_delta = t5_red_delta + t5_delta + t7_delta + t7_red_delta + t20_delta + other_delta + anal5_delta + anal7_delta
                print("Phase B progress: ", progress_count)
                print("---------------------------------------------------t5_red_delta",round(t5_red_delta,4)*1000,"ms") 
                print("---------------------------------------------------t5_delta",round(t5_delta,4)*1000,"ms") 
                print("---------------------------------------------------t7_red_delta",round(t7_red_delta,4)*1000,"ms") 
                print("---------------------------------------------------t7_delta",round(t7_delta,4)*1000,"ms") 
                print("---------------------------------------------------t20_delta",round(t20_delta,4)*1000,"ms") 
                print("---------------------------------------------------other_delta",round(other_delta,4)*1000,"ms") 
                print("---------------------------------------------------anal5_delta",round(anal5_delta,4)*1000,"ms") 
                print("---------------------------------------------------anal7_delta",round(anal7_delta,4)*1000,"ms") 
                print("--------------------------------------------------------------------------------------") 
                print("---------------------------------------------------total_delta",round(total_delta,4)*1000,"ms") 
                t5_red_delta = 0
                t5_delta = 0
                t7_red_delta = 0
                t7_delta = 0
                t20_delta = 0
                other_delta = 0
                anal5_delta = 0
                anal7_delta = 0
            
            if len(words) > 4:
                redundant = False


            #t5 ---- 
                
                other_delta += delta_time()
                for redundancycheck in tier5_arr:
                    if redundancycheck ==[words[0], words[1], words[2] , words[3] , words[4]]:
                        redundant = True
                        break
                t5_red_delta += delta_time()

                if redundant == False:
                    newstring = ""
                    #if(2 < len(tier5_arr)):
                        #print(tier5_arr)
                    #print(words)
                    for x in range(0,len(words)):
                        if x > 0:
                            newstring += " "
                        newstring += words[x]
                        if process_all_hash_cases(newstring,example_hash,Test):
                            return True
                        
                    t5_delta += delta_time()
                else:

                #t7 ---- 

                    for redundancycheck in tier7_arr:
                        if redundancycheck ==[words[0], words[1], words[2] , words[3] , words[4] , words[5] , words[6]]:
                            redundant = True
                            break

                    t7_red_delta += delta_time()

                    if redundant == False:
                        newstring = words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4]
                        for x in range(5,len(words)):
                            newstring += " "
                            newstring += words[x]
                            #print(newstring)

                            if process_all_hash_cases(newstring,example_hash,Test):
                                return True
                        
                        t7_delta += delta_time()
                    else:

                    #t9 ---- 
                        if len(words) > 6:
                            newstring = words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6]
                            for x in range(7,len(words)):
                                newstring += " "
                                newstring += words[x]
                                #print(newstring)

                                if process_all_hash_cases(newstring,example_hash,Test):
                                    return True
                            
                            t20_delta += delta_time()
                

                other_delta += delta_time()
                tier5_arr = T5_analysis(words,tier5_arr)
                anal5_delta += delta_time()
                if len(words) > 6:
                    tier7_arr = T7_analysis(words,tier7_arr)
                    anal7_delta  += delta_time()
                
    #----------------------------------------#

    if Test == False:
        print("")
        print("total number of phrases:   " , sum_of_phrases)
        print("total word count:          " , word_count)
        print("the avg word count/phrases:" , (word_count / sum_of_phrases))
        print("")   
    return False
    #else:
        #print("No input data received")
        #return False

clear_console()
analysis()  
#Unit_Test()
#create_testhash("test123ihatethis")
#main_crack()
#convert_input_format() # convert from "phrase1", "phrase2", "etc." --> phrases without "" seperated by a new line

if True:
        
    #any print statement below that is commented out has been accomplished 
    print("")
    print("TODOS: ")
    print("fix analysis function which uses Deprecated file reading logic")
    print("figure out if the script should support piped input or just use absolute hard coded path input")

    ###------
    print("create a new generation function that completely bruteforces passwords based on how frequently used words are in the dictonaries")

    #example top 10 words being "a,b,c,d,e,f,g,h,i,j,k"
    #lets do up to 4 layers of word combinations + salted characters like 123 ! ? etc.

    #for example generate:
    #a
    #aa
    #aaa
    #aaaa
    #aaab
    #...
    #aab
    #aac
    #aad
    #aae
    #...
    #ab
    #aba
    #abb
    #abc
    #abd
    #abe
    #...
    #ac
    #aca
    #acb
    #acc
    #acd
    #ace
    #...
    #ad
    #...
    #ae
    #...
    #af
    #...
    #ag
    #...
    ###-------

    #print("figure out a faster way to read the data having massive amounts of data stored in a variable is too slow maybe read it line by line")
    #print("read input line by line from a file instead of stuffing massive amount of data in a variable and reading from the variable line by line")
    print("teach the script some basic grammar like subordinate clause stuff")
    print("add salt...")
    print("Add salting character such as !!!,?,123,1234,12345 at the start or end of phrases ")
    print("make dedicated dictonaries for subjects, verbs, adjectives and so on")
    print("add a new phrase generating algorithm that uses basic grammar like each 1 subject, object, verb and adjective to create more out of scope passphrases without prior observed word combinations")
    #print(measure and optimize processing speed with large file inputs)
    #print("fighting redundancy")
    #print("add unit test for partial check of passphrases for example hash the first word then the first two then the first three and so on")
    #print("analyze how natural sentences typically end and forcefully stop at that point while generating new random ones")
    #print("generate new phrases based on frequency analysis of existing example data")
    print("crawl famous quotes / famous song lyrics")
    print("Add typo check for example 1 key around the intended key for each char in a passphrase with maximum one allowed error at a time")
    print("Add typo check switch 2 characters Tihs -> This")
    #print("Optimize Logik to analyze word combination frequency")
    #print("Add Logik to Generate Random new phrases based on the frequency observations from the previous analysis")
    #print("make only the first letter of each word uppercase")
    print("generate phrases based on a random combination of most frequently used words in the passphrase analysis even if it has never been seen that they are combined like that")
    print("figure out a solution for words like: It's I'm I'll can't There's don't doesn't")
    print("Create a menu that takes a sentences as input and compares it with its dictonaries to display the required dictonaries to recreate it")
    print("Add Automated chatGPT phrase generation")




    #usefull cmds
    #cat test.txt | python3 parse.py                 #Deprecated cmd currently no piped input supported
    #echo -n "YetAnotherPassword" | shasum -a 256    #Create a Test Hash in any unix based shell
    #