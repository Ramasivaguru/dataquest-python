## 1. Overview ##

vocabulary = open('dictionary.txt')
print(vocabulary.read())

## 2. Tokenizing the Vocabulary ##

vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = vocabulary.split(' ')

## 3. Replacing Special Characters ##

f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace('.','')
story_string = story_string.replace("'",'')
story_string = story_string.replace(';','')
story_string = story_string.replace('\n','')

## 5. Practice: Creating a Function that Cleans Text ##

f = open("story.txt", 'r')
story_string = f.read()

def clean_text(text_string):
    cleaned_string = text_string.replace(".","")
    cleaned_string = cleaned_string.replace(",","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(";","")
    cleaned_string = cleaned_string.replace("\n","")
    return(cleaned_string)

cleaned_story = clean_text(story_string)

## 6. Changing Word Case ##

def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
cleaned_story = clean_text(story_string)

## 7. Multiple Arguments ##

f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

# Previous code for clean_text().
def clean_text(text_string, clean_chars):
    for i in clean_chars:
        text_string = text_string.replace(i,'')
    return(text_string.lower())
  
cleaned_story = clean_text(story_string,clean_chars)

## 8. Tokenizing the Story ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
def tokenize(text_string, special_characters):
    text_string = clean_text(text_string, special_characters)
    text_string = text_string.split(' ')
    return(text_string)

clean_chars = [",", ".", "'", ";", "\n"]
cleaned_story = clean_text(story_string, clean_chars)
tokenized_story = tokenize(story_string, clean_chars)

## 9. Finding Misspelled Words ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
for i in tokenized_story:
    if i not in tokenized_vocabulary:
        misspelled_words.append(i)