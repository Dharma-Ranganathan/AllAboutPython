
print("Simple calculator...")
try:
    while(True):
        print("""
choose any operation,
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
        """)
        opr = int(input("Enter Operation Number: "))
        if(opr==5):
            print()
            print("wanna start again? click run!")
            break
        
        if(opr==1):
            print()
            print("1. Addition has selected")
            inputs=int(input("Number of inputs? : "))
            if(inputs<=0):
                print("Number of input cannot be 0 or less than 0...")
            store=[]
            while(inputs>0):
                value=int(input("Enter value: "))
                store.append(value)
                inputs-=1
            answer=0
            for i in store:
                answer+=i
            print("Added :",answer)
    
        if(opr==2):
            print()
            print("1. Subtraction has selected")
            inputs=int(input("Number of inputs? : "))
            if(inputs<=0):
                print("Number of input cannot be 0 or less than 0...")
            store=[]
            while(inputs>0):
                value=int(input("Enter value: "))
                store.append(value)
                inputs-=1
            
            pos=[]
            neg=[]
            for i in store:
                if(i>=0):
                    pos.append(i)
                else:
                    neg.append(i)
            
            answer=0
            
            if(not(len(neg))):
                for i in pos:
                    if(answer==0):
                        answer=pos[0]
                        continue
                    answer-=i
            elif(not(len(neg))):
                for i in neg:
                    if(answer==0):
                        answer=neg[0]
                        continue
                    answer+=i
            else:
                sub1=0
                sub2=0
                for i in pos:
                    sub1+=i
                for i in neg:
                    sub2+=i
                answer=sub1+sub2
                    
            print("Subtracted :",answer)
            
        if(opr==3):
            print()
            print("1. Multiplication has selected")
            inputs=int(input("Number of inputs? : "))
            if(inputs<=0):
                print("Number of input cannot be 0 or less than 0...")
            store=[]
            while(inputs>0):
                value=int(input("Enter value: "))
                store.append(value)
                inputs-=1
            answer=1
            for i in store:
                answer*=i
            print("Multiplied :",answer)
    
        if(opr==4):
            print()
            print("1. Division has selected")
            inputs=int(input("Number of inputs? : "))
            if(inputs<=0):
                print("Number of input cannot be 0 or less than 0...")
                
            
            store=[]
            while(inputs>0):
                value=int(input("Enter value: "))
                store.append(value)
                inputs-=1
            answer=0
            for i in store:
                if(answer==0):
                    answer=store[0]
                    continue 
                answer/=i
                
                
            print("Divided :",answer)
    
except Exception as error:
    print()
    print("Error Message:",error)
