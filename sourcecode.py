# Define the questions and answers
questions = [
    ["Current Railway Minister of India is", "Piyush Goyal", "Mamta Banarjee", "RamVilas", "Ashwini Vaishnav", 4],
    ["Which god is also known as ‘Gauri Nandan’?", "Agni", "Indra", "Ganesh", "Hanuman", 3],
    ["What does not grow on tree according to a popular Hindi saying?", "Money", "Flower", "Leaves", "Fruit", 1],
    ["Which city is known as the Pink City of India?", "Banglore", "Mysore", "Jaipur", "Kochi", 3],
    ["Who wrote India's National Anthem?", "Lal Bahdur Shastri", "Rabindranath Tagore", "Chetan Bhagat", "RK Narayan", 2],
    ["How many major religions are there in India?", 6, 7, 8, 9, 1],
    ["Which of the following states doesn’t share its boundary with Gujarat?", "Maharastra", "Rajasthan", "Madhya Pradesh", "Goa", 4],
    ["According to Indian Mythology, Kans, the brother of Devaki was the ruler of which city?", "Mathura", "Dwarka", "Indraprasta", "Ujjain", 1],
    ["Who wrote the play “Romeo and Juliet?", "Oscar wilde", "William Shakespear", "Jann Austen", "Scott Fitzerland", 2],
    ["Which state in India is also known as “Dev Bhoomi”?", "Rajasthan", "Uttrakhand", "Uttar Pradesh", "Andhra Pradesh", 2],
    ["What is the chemical symbol for gold?", "Ag", "Au", "Hg", "Pb", 2],
    ["Which planet in our solar system is known for being the largest?", "Earth", "Saturn", "Jupiter", "Uranus", 3],
    ["Who is the author of the book 'To Kill a Mockingbird'?", "F. Scott Fitzgerald", "Harper Lee", "Jane Austen", "J.K. Rowling", 2],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3],
    ["Who is the lead singer of the rock band Queen?", "Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon", 1],
    ["What is the largest mammal on Earth?", "Blue whale", "Fin whale", "Humpback whale", "Sperm whale", 1],
    ["Who is the author of the book 'The Lord of the Rings'?", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin", "J.K. Rowling", 1],
    ["What is the chemical symbol for silver?", "Ag", "Au", "Hg", "Pb", 1],
    ["Which country is known for its chocolate?", "Belgium", "Switzerland", "France", "Italy", 1],
    ["Who is the lead singer of the rock band Guns N' Roses?", "Axl Rose", "Slash", "Duff McKagan", "Matt Sorum", 1],
    ["What is the capital of China?", "Beijing", "Shanghai", "Guangzhou", "Hong Kong", 1],
    ["Which river is known as the ‘Lifeline of Egypt’?","Nile River","Ganga river","Tsangpo","Gediz",1]
]

# Define the levels and their corresponding amounts
levels = [1000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000, 2560000, 5120000, 10240000, 20480000, 40960000, 81920000, 163840000, 327680000, 655360000,70000000]

# Initialize the money won
money_won = 0

# Loop through each question
for i, question in enumerate(questions):
    # Print the question and options
    print(f"Question For Rs. {levels[i]}")
    print(question[0])
    print(f"1.{question[1]}             2.{question[2]}")
    print(f"3.{question[3]}             4.{question[4]}")

    # Get the user's response
    response = input("Press 0 to Quit or Enter the Answer No.: ")

    # Check if the user wants to quit
    if response == "0":
        break

    # Convert the response to an integer
    response = int(response)

    # Check if the response is correct
    if response == question[-1]:
        # Update the money won
        money_won = levels[i]
        print(f"Correct Answer, You won Rs. {levels[i]}")
    else:
        # Print the correct answer
        print(f"Wrong Answer, Correct Answer is {question[-1]}")
        break

# Print the total money won
print(f"Your total Won Money is Rs. {money_won}")