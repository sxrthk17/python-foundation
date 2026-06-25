deep_thought_ans = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if deep_thought_ans.lower() not in ['42', 'forty-two', 'forty two']:
    print("No")
else:
    print("Yes")
