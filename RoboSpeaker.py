import os

if __name__ == '__main__':
    print("Welcome My Dear Friend To Robo-Speaker Created By CodeWithSalty aka Salman")
    os.system("say 'Welcome My Dear Friend To Robo-Speaker Created By CodeWithSalty aka Salman'")
    os.system("say 'What do you want me to say, Sir?'")
    while True:
        x = input("-----> : ")
        if x == 'q':
            os.system("say 'Bye my friend, I will miss you'")
            break
        command = f"say '{x}'"
        os.system(command)
