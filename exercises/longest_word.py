def longest_word(sentence):
    # Finding the longest string using a loop  
    longest = ""  
    for word in sentence.split(" "):  
        if len(word) >= len(longest):  
            longest = word  

    return longest

if __name__ == "__main__":
    print(longest_word("what a wonderful world")) # -> "wonderful")