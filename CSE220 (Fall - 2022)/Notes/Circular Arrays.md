# Circular Arrays

#### Thumb Rule 1
When traversing a circular Array:
* One variable as Loop Controller (How many times the loop is going to run)
* Different variable for index of Circular Array

#### Thumb Rule 2
Whenever you increment the index of a circular array, always mod the incremented value with the circular array's length.

> index + 1 % len(arr)

#### Thumb Rule 3

Watch [this video](https://bux.bracu.ac.bd/courses/course-v1:buX+CSE220+2022_Spring/courseware/3ab32391b7054488b5260b23b080f632/be648c7fad1b47f380e4eb3c07664c8a/?activate_block_id=block-v1%3AbuX%2BCSE220%2B2022_Spring%2Btype%40sequential%2Bblock%40be648c7fad1b47f380e4eb3c07664c8a)

> Last_index = (start + size - 1) % len(arr)

#### Thumb Rule 4
Whenever you decrement the index of a circular array, always check, keep a check wheater it became negative. If it does, point it to the end of the array. 

#### 


#### Forward Printing a circular Array

```py
def printForward(arr, start, size):
    index = start
    i = 0

    while (i < size):
        print(arr[index])
        index = (index + 1) % len(arr)
        i += 1

circular_arr = [40,50,0,0,0,0,0,0,10,20,30]
printForward(circular_arr, 8, 5)
```
Output:
```txt
10
20
30
40
50
```
#### Reverse Printing a Circular Array

```py
def printReverse(arr,start,size):
    index=(start + size - 1) % len(arr)
    i = 0

    while(i < size):
        print(arr[index])
        index = index - 1

        if(index<0):
            index = len(arr) - 1  
        
        i += 1


circularArray=[40,50,0,0,0,0,0,0,10,20,30]
printReverse(circularArray,8,5)
```

#### Creating a Circular Array from Linear Arrays

```py
def circularize(linear,start,size):

    circular=[0]*len(linear)

    index=start

    i=0

    while(i<size):

        circular[index]=linear[i]

        index=(index+1)%len(circular) 

        i=i+1

    return circular



linear=[10,20,30,40,50,0,0,0,0,0,0]

circ=circularize(linear,8,5)

print(circ)
```

