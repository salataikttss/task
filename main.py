def filter_short_strings(array):
    return [string for string in array if len(string) <= 3]

def main():
    input_array = ["Hello", "2", "world", ":-)" ]
    result = filter_short_strings(input_array)
    print(result)

main()
