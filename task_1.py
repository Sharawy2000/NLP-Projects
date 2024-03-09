import nltk

# u_input=("NLTK is a leading platform for building Python programs to work with human language data."
#        " NLTK is available for Windows, Mac OS X, and Linux. Best of all, "
#        "NLTK is a free, open source, community-driven project")

u_input=str(input("\nEnter your text input : "))

user_choice=int(input("\nThere 3 choices you have \n1. print tokenized words \n2. print tokenized sentences \n3. print output using split function \n\nSo enter a number 1..3 : "))


if user_choice == 1 :
    w_tokinized=nltk.word_tokenize(u_input)
    print("\n",w_tokinized)


elif user_choice==2 :
    s_tokinized = nltk.sent_tokenize(u_input)
    print("\n",s_tokinized)

elif user_choice==3 :
    sp_tokinized = u_input.split(",")
    print("\n",sp_tokinized)

else:
    raise "Enter number from 1 to 3 :("