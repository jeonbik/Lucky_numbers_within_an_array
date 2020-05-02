#Lucky number
#import pandas as pd
def lucky_number(n):
    initial_position=2
    if len(n)>=initial_position:
        for i in range (len(n)):
          
                removing_array=[]
                for elem in n:
                    if ((n.index(elem)+1)%initial_position==0):
                        removing_array.append(elem)
                        
                n=list(set(n)-set(removing_array))
                n.sort(reverse=False)
                initial_position+=1
        print(n)

                        
                    

         
           
        
        
        
        
        
        


def main():
    number=int(input("Enter number: "))
    numbers=[]
    for i in range (number):
        numbers.append(i+1)
    lucky_number(numbers)



if __name__=="__main__":
    main()


