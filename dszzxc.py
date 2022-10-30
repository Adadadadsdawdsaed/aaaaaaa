from colorama import *
init(autoreset= True)
print("Звичайний текст")
print(Fore.GREEN + "зелений текст")
print(Style.BRIGHT + "Жирний текст")
print(Back.LIGHTRED_EX + "світло- червоний фон тексту")
print(Fore.BLACK + Style.BRIGHT  + Back.WHITE + " як на мене всі ці модули цікаві, і можуть бути корисними для виділення тексту у консолі ")
print(Fore.BLACK + Style.BRIGHT  + Back.WHITE + " Також можна буде не підписувати, наприклад який персонаж , а поосто написати до якого персонажа відносится певний колір")


