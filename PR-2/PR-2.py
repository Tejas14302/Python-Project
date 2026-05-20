while True:
    print("Welcome to Pattern Generator And Number Analyzer!")
    print()
    print("1.Generate a Patterns!")
    print("2.Analyze A Range Of Numbers!")
    print("3.Exit!")
    print()
    choice=int(input("Enter Your Choice:"))
    match choice:
        case 1:
            print("1.Right Triangle Pattern!")
            print("2.Reverse Triangle Pattern!")
            print("3.Pyramid Pattern!")
            pattern_choice=int(input("Enter Your Choice:"))
            match pattern_choice:
                case 1:
                    row=int(input("Enter The Number Of Rows:"))
                    print()
                    print("Pattern:")
                    for row in range(1,row+1):
                        for colm in range(1,row+1):
                            print("*",end=" ")
                        print()
                    print()
                case 2:
                    row=int(input("Enter The Number Of Rows:"))
                    print()
                    print("Pattern:")
                    for row in range(row,0,-1):
                        for colm in range(row):
                            print("*",end=" ")
                        print()
                    print()
                case 3:
                    row=int(input("Enter The Number Of Rows:"))
                    print()
                    print("Pattern:")
                    for i in range(1,row+1):
                        print(" " * (row-i),end="")
                        for colm in range(i):
                            print("*",end=" ")
                        print()
                    print()
                case _:
                    print("Invalid Choice!!!")
        case 2:
            start_range=int(input("Enter The Start Of The Range:"))
            end_range=int(input("Enter The End Of The Range:"))
            original_start=start_range
            original_end=end_range
            while start_range<= end_range:
                if start_range%2==0:
                    print("Number",start_range,"Is Even")
                else:
                    print("Number",start_range,"Is Odd")
                start_range+=1
            print()
            print("1.Sum Of The Odd Number!")
            print("2.Sum Of The Even Number!")
            print("3.Sum Of The All Number!")
            sum_choice=int(input("Your Choice:"))
            match sum_choice:
                case 1:
                    odd_sum=0
                    sum=original_start
                    while sum<= original_end:
                        if sum%2!=0:
                            odd_sum=odd_sum+sum
                        sum+=1
                    print("Sum Of The Odd Number Is:",odd_sum)
                    print()
                case 2:
                    even_sum=0
                    sum=original_start
                    while sum<= original_end:
                        if sum%2==0:
                            even_sum=even_sum+sum
                        sum+=1
                    print("Sum Of The Even Number Is:",even_sum)
                    print()
                case 3:
                    total_sum=0
                    sum=original_start
                    while sum<= original_end:
                        total_sum=total_sum+sum
                        sum+=1
                    print("Sum Of The All Number Is:",total_sum)
                    print()
                case _:
                    print("Invalid Choice!!!")
        case 3:
            print("Exiting The Program. Goodbye!")
            break
        case _:
            print("invalid choice!!!")