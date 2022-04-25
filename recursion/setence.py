"""
clause = name + verb + that

sentence = clause(clause(clause(base)))
"""

import random
from typing import List


names = ["Valerio", "Francesca", "Joel",
         "Anna", "Julio", "Milton",
         "Natasha", "Andrew", "Jane"]

verbs = ["thinks", "says", "suspects",
         "ignores", "supposes", "is afraid",
         "has learned", "doesn't accept", "has inferred"]


def generate_recursive_sentence(levels: int,
                                names: List[str],
                                verbs: List[str]) -> str:
    if levels <= 1:
        return "I love recursion"
    else:
        clause = f"{random.choice(names)} {random.choice(verbs)} that "
        return clause + generate_recursive_sentence(levels-1, names, verbs)


if __name__ == "__main__":
    sentence = generate_recursive_sentence(20, names, verbs)
    print(sentence)










