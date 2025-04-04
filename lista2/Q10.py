print("\n                     ~::~ Tabuada de 1 a 10 ~::~\n")

for x in range(1, 11):
    print(f"{x:20}", end="")  
    
    for y in range(1, 11):

        print(f" {x * y:2}", end="") 
    print()  