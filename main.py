question=[["Current Railway Minister of India is","Piyush Goyal","Mamta Banarjee","RamVilas","Ashwini Vaishnav",4],
          ["Which god is also known as ‘Gauri Nandan’?","Agni","Indra","Ganesh","Hanuman",3],
          ["What does not grow on tree according to a popular Hindi saying?","Money","Flower","Leaves","Fruit",1],
          ["Which city is known as the Pink City of India?","Banglore","Mysore","Jaipur","Kochi",3],
          ["Who wrote India's National Anthem?","Lal Bahdur Shastri","Rabindranath Tagore","Chetan Bhagat","RK Narayan",2],
          ["How many major religions are there in India?",6,7,8,9,1],
          ["Which of the following states doesn’t share its boundary with Gujarat?","Maharastra","Rajasthan","Madhya Pradesh","Goa",4],
          ["According to Indian Mythology, Kans, the brother of Devaki was the ruler of which city?","Mathura","Dwarka","Indraprasta","Ujjain",1],
          ["Who wrote the play “Romeo and Juliet?","Oscar wilde","William Shakespear","Jann Austen","Scott Fitzerland",2],
          ["Which state in India is also known as “Dev Bhoomi”?","Rajasthan","Uttrakhand","Uttar Pradesh","Andhra Pradesh",2]]

Levels=[1000,3000,5000,10000,20000,40000,80000,160000,320000,640000]
money=0
for i in range(0,len(question)):
    questions=question[i]
    print(f"Question For Rs. {Levels[i]}")
    print(questions[0])
    print(f"1.{questions[1]}             2.{questions[2]}")
    print(f"3.{questions[3]}             4.{questions[4]}")
    
    reply=int(input("Press 0 to Quit or Enter the Answer No.: "))
    if reply==0:
        break
    money=Levels[i-1]
    if reply==questions[-1]:
        print(f"Correct Answer, You won Rs. {Levels[i]}")

        if (Levels[i]==3):
            money=10000
        elif (Levels[i]==6):
            money=80000
        elif (Levels[i]==9):
            money=640000
    else:
        print(f"Wrong Answer, Correct Answer is {questions[-1]}")
        break

print(f"Your total Won Money is Rs. {money}")



