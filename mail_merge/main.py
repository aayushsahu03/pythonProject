text = 'Hi [name], you have a pre-aprroved\n offer of Rs.1,00,000'
with open("names_list.txt", 'r') as file:
    for name in file.readlines():
        with open(f"./{name.strip()}_letter.txt", 'w') as letter:
            letter.write(text.replace('[name]',name))
