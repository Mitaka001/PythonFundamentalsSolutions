def loading(numbers):
    percent = numbers // 10
    if numbers == 100:
        return f"{numbers}% Complete!\n[{percent * '%'}]"
    else:
        return f"{numbers}% [{percent * '%'}{(10 - percent) * '.'}]\nStill loading..."


number = int(input())
print(loading(number))
