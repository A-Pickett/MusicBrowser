# def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     kwargs.pop('end', **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:  # Changing the range and.....
        print(word[::-1], end=sep_character, **kwargs)  # ...print the first word separately...
    # print(end=end_character)  #  ...which means we dont need this line.
    print(args[0][::-1], end=end_character, **kwargs)  #


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another Sting")


print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)