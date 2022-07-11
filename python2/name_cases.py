if __name__ == '__main__':
    name = "Eric"
    message1 = f"Hello {name}, would you like to learn some Python today?"
    print(message1)
    print(name.lower())
    print(name.title())
    print(name.upper())

    famous_person = "\tAlbert Einstein\n"
    message2 = f'{famous_person} once said "A person who never made a mistake never tried anything new."'
    print(message2)
    print(message2.lstrip())
    print(message2.rstrip())
    print(message2.strip())
