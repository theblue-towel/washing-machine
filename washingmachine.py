#Change the sample list to whatever you'd like to sort

sample_list = [66, 60, 40, 38, 64, 75, 73, 58, 52, 60, 70, 72, 62, 60, 84, 57, 47, 46, 58, 39, 60, 50, 82, 60, 51, 53, 56, 71, 45, 70, 59, 61, 49, 49, 60, 72, 38, 58, 57, 65]

rounds = input("How many rounds do you want to wash?")
while rounds > 0:
    for i in range(len(sample_list)):
        if i < len(sample_list) - 1:
            if sample_list[i] > sample_list[i + 1]:
                for i in range(len(sample_list)):
                    if i != 0 or i != len(sample_list) + 1:
                        current = sample_list[i]
                        prev = sample_list[i - 1]
                        if current < prev:
                            sample_list.pop(i)
                            sample_list.insert(0, current)
        else: 
            print('completed one round of washing')
    rounds -= 1

print(sample_list)