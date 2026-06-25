from collections import Counter
items = []
while True:
    try:
        prompt = input("")
        items.append(prompt.strip().upper())
    except EOFError:
        item_count = Counter(items)
        item_count = sorted(item_count.items(), key=lambda x: x[0])
        for item, count in item_count:
            print(f"{count} {item}")
        break
