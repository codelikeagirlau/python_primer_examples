def vowel_counting(my_name):
    vowel_list = "aeiou"
    vowel_count = 0    
    
    for char in my_name:
        if char.lower() in vowel_list:
            vowel_count += 1
            
    print(f"My name is {my_name}, which contains {vowel_count} vowels.")   

if __name__ =="__main__":
    vowel_counting("my name")