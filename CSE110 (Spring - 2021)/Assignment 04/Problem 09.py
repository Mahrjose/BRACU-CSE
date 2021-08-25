print(
    [
        num
        for num in [
            int(num)
            for num in input("Enter 10 numbers separated by comma(,):").split(",")
        ]
        if num % 2 != 0
    ]
)
