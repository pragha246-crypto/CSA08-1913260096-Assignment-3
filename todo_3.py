calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    # TODO 1 completed: count non-stop words using dict.get().
    counts = {}
    for text in texts:
        for word in text.split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    # TODO 2 completed: highest frequency first; alphabetical for ties.
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

print(top(frequencies(calls, STOP), 3))
