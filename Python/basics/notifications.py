def yell(text):
    text = text.upper()
    num_of_chars = len(text)
    result = text + "!" * (num_of_chars // 4)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't repeat yourself. Keep things DRY")
