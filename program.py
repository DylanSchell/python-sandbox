while True:
    name = input('What is your name? ')
    
    if name == "":
        print("Mysterious eh?")
        break
    
    times_input = input('How many times? ')
    
    try:
        times = int(times_input)
    except:
        print(f"{times_input} is not a (whole) number!")
        break

    for x in range(int(times)):
        print(f"Hello {name}!")