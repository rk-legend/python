def split_and_join(line):
    # Split the string into a list using the space delimiter
    words = line.split(" ")
    
    # Join the list elements back into a string using a hyphen
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
