def chatbot():

    print("===== Welcome to Customer Support Chatbot =====")
    print("Type 'bye' to exit")

    while True:

        user = input("\nYou: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! How can I help you?")

        elif "product" in user:
            print("Bot: We have laptops, mobiles and accessories available.")

        elif "price" in user:
            print("Bot: Prices start from Rs. 10,000.")

        elif "delivery" in user:
            print("Bot: Delivery takes 3 to 5 working days.")

        elif "payment" in user:
            print("Bot: We accept UPI, Cards and Cash on Delivery.")

        elif "contact" in user:
            print("Bot: You can contact us at support@gmail.com")

        elif user == "bye":
            print("Bot: Thank you for visiting!")
            break

        else:
            print("Bot: Sorry, I did not understand your question.")

chatbot()