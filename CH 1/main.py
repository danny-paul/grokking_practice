import binary_search as search_lib

def main():
    ordered_list = [1, 2, 5, 6, 44, 55, 88, 99]
    
    print("test, in main")
    find_value = 1
    index_is = search_lib.binary_search(ordered_list, find_value)
    print(ordered_list, end='\n\n')
    if index_is != -1:
        print("Value ", ordered_list[index_is], " at index ", index_is)
    else:
        print("Value", find_value, "not found")

    
if __name__ == "__main__":
    main()