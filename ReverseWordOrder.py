sentence = input("Give me a cool sentence and I'll reverse it...\n")

sent_list = sentence.split(" ")

reverse_sent = reversed(sent_list)

print(" ".join(reverse_sent))
