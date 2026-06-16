<<<<<<< HEAD
import statistics
print("Welcome to Data Analyzer and Trasformer Program")
print()

def data_collector():
    '''collect the data and store it.'''
    data=list(map(int,input("Enter 1D Array Elements(use space): ").split()))
    print("Data Stored Successfully!")
    return data

def data_summary():
    '''give out the maximum,minimum values, sum of the array, and total elements in arr using built-in function'''
    if not arr:
        print("No data found! Please input Data first (option 1).")
        return
    print(f"Total Elements:{len(arr)}")
    print(f"Minimum Value:{min(arr)}")
    print(f"Maximum Value:{max(arr)}")
    print(f"Total Sum Of the Array:{sum(arr)}")

def factorial(num):
    '''calculate factorial of the given number'''
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
def threshold():
    '''give the bigger number than given number'''
    threshold=int(input("Enter The Threshold value to filter out data above this value:"))
    filterfunc=lambda val: val >= threshold
    filtered_result=list(filter(filterfunc,arr))
    print(f"\nFiltered Data (values >= {threshold}):")
    if filtered_result:
        print(", ".join(map(str, filtered_result)))
    else:
        print("No records matched the threshold criteria rules.")

def sorting():
    '''sort the array in either ascending or decending order'''
    if not arr:
        print("No data found! Please input Data first (option 1).")
    print("Press 1 for Ascending")
    print("Press 2 for Descending")
    sort_choice=int(input("Enter Your choice:"))
    match sort_choice:
        case 1:
            arr.sort()
            print("\nSorted Data in Ascending Order:")
            print(", ".join(map(str,arr)))
        case 2:
            arr.sort(reverse=True)
            print("\nSorted Data in Ascending Order:")
            print(", ".join(map(str,arr)))
        case _:
            print("Invalid sorting choice option parameter selection.")

def dataset_stat():
    '''give the minimun,maximum value,sum, and average value of the array'''
    min_value=arr[0]
    for num in arr:
        if num<min_value:
            min_value=num
    max_value=arr[0]
    for num in arr:
        if num>max_value:
            max_value=num
    total=0
    for num in arr:
        total+=num
    average=statistics.mean(arr)
    print("Dataset Statistics:")
    print(f" - Minimum value: {min_value}")
    print(f" - Maximum value: {max_value}")
    print(f" - Sum of all values: {total}")
    print(f" - Average value: {average}")
    print()

arr=[]
while True:
    print("Main Menu: ")
    print("Press 1 To Input Data")
    print("Press 2 To Display Data Summary")
    print("Press 3 To Calculate factorial")
    print("Press 4 To Filter Data By Threshold")
    print("Press 5 To Sort Data")
    print("Press 6 To Display Dataset Statistics")
    print("Press 7 To Exit Progame")
    choice=int(input("Enter Your Choice: "))
    print()
    match choice:
        case 1:
            print(data_collector.__doc__)
            arr=data_collector()
            print()
        case 2:
            print(data_summary.__doc__)
            data_summary()
            print()
        case 3:
            print(factorial.__doc__)
            num=int(input("Enter Any Number For Factorial:"))
            result=factorial(num)
            print(f"Tha Factorial of the Number is:{result}\n")
        case 4:
            print(threshold.__doc__)
            threshold()
            print()
        case 5:
            print(sorting.__doc__)
            sorting()
            print()
        case 6:
            print(dataset_stat.__doc__)
            dataset_stat()
        case 7:
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:
=======
import statistics
print("Welcome to Data Analyzer and Trasformer Program")
print()

def data_collector():
    '''collect the data and store it.'''
    data=list(map(int,input("Enter 1D Array Elements(use space): ").split()))
    print("Data Stored Successfully!")
    return data

def data_summary():
    '''give out the maximum,minimum values, sum of the array, and total elements in arr using built-in function'''
    if not arr:
        print("No data found! Please input Data first (option 1).")
        return
    print(f"Total Elements:{len(arr)}")
    print(f"Minimum Value:{min(arr)}")
    print(f"Maximum Value:{max(arr)}")
    print(f"Total Sum Of the Array:{sum(arr)}")

def factorial(num):
    '''calculate factorial of the given number'''
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
def threshold():
    '''give the bigger number than given number'''
    threshold=int(input("Enter The Threshold value to filter out data above this value:"))
    filterfunc=lambda val: val >= threshold
    filtered_result=list(filter(filterfunc,arr))
    print(f"\nFiltered Data (values >= {threshold}):")
    if filtered_result:
        print(", ".join(map(str, filtered_result)))
    else:
        print("No records matched the threshold criteria rules.")

def sorting():
    '''sort the array in either ascending or decending order'''
    if not arr:
        print("No data found! Please input Data first (option 1).")
    print("Press 1 for Ascending")
    print("Press 2 for Descending")
    sort_choice=int(input("Enter Your choice:"))
    match sort_choice:
        case 1:
            arr.sort()
            print("\nSorted Data in Ascending Order:")
            print(", ".join(map(str,arr)))
        case 2:
            arr.sort(reverse=True)
            print("\nSorted Data in Ascending Order:")
            print(", ".join(map(str,arr)))
        case _:
            print("Invalid sorting choice option parameter selection.")

def dataset_stat():
    '''give the minimun,maximum value,sum, and average value of the array'''
    min_value=arr[0]
    for num in arr:
        if num<min_value:
            min_value=num
    max_value=arr[0]
    for num in arr:
        if num>max_value:
            max_value=num
    total=0
    for num in arr:
        total+=num
    average=statistics.mean(arr)
    print("Dataset Statistics:")
    print(f" - Minimum value: {min_value}")
    print(f" - Maximum value: {max_value}")
    print(f" - Sum of all values: {total}")
    print(f" - Average value: {average}")
    print()

arr=[]
while True:
    print("Main Menu: ")
    print("Press 1 To Input Data")
    print("Press 2 To Display Data Summary")
    print("Press 3 To Calculate factorial")
    print("Press 4 To Filter Data By Threshold")
    print("Press 5 To Sort Data")
    print("Press 6 To Display Dataset Statistics")
    print("Press 7 To Exit Progame")
    choice=int(input("Enter Your Choice: "))
    print()
    match choice:
        case 1:
            print(data_collector.__doc__)
            arr=data_collector()
            print()
        case 2:
            print(data_summary.__doc__)
            data_summary()
            print()
        case 3:
            print(factorial.__doc__)
            num=int(input("Enter Any Number For Factorial:"))
            result=factorial(num)
            print(f"Tha Factorial of the Number is:{result}\n")
        case 4:
            print(threshold.__doc__)
            threshold()
            print()
        case 5:
            print(sorting.__doc__)
            sorting()
            print()
        case 6:
            print(dataset_stat.__doc__)
            dataset_stat()
        case 7:
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:
>>>>>>> 2babcf9e8b929388ef2ba690a2e062e7e300e372
            print("Invalid choice")