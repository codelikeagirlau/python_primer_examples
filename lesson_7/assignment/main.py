import vowel_counter
import vowel_counter_script_guard
import vowel_counter_extended
import vowel_counter_refactor

print("\nVowel Counter Examples:")

#Simple execution using returned count
print("\nSimple Example")

name = "Eloise"
num_of_vowels = vowel_counter.vowel_counter(name)
print(f"Your name {name} has {num_of_vowels} vowels")

# Extended example 
print("\nExtended Example")
vowel_counter_extended.vowel_counter("Sarah Brown")

# Script Guard Example
print("\nScript Guard Example")
vowel_counter_script_guard.vowel_counting(name)

print("\nRefactored Example")
vowel_counter_refactor.vowel_counter("Sarah Brown")