import re

# Predicates for translation
predicates = {
    "is a human": "H",  # e.g., John is a human
    "is mortal": "M",   # e.g., John is mortal
    "loves": "L",       # e.g., John loves Mary
    "is a dog": "D",    # e.g., John is a dog
    "is an animal": "A", # e.g., John is an animal
    "is brown": "B",    # e.g., John is brown
    "is a person": "P",  # e.g., John is a person
    "is a teacher": "T",  # e.g., John is a teacher
    "is a student": "S",  # e.g., John is a student
    "respects": "R",     # e.g., John respects Mary
    "knows": "K",       # e.g., John knows Mary
    "likes mathematics": "Lm",  # John likes mathematics
    "likes science": "Ls",     # John likes science
    "is married to": "Ma",  # John is married to Mary
    "is a bachelor": "Bch", # John is a bachelor
    "is a parent of": "Pnt", # John is a parent of someone
    "is raining": "R",    # It is raining
    "is wet": "G",        # The ground is wet
    "taller than": "TallerThan",  # For taller than statements
}

# Function to handle sentence translation
def translate_to_fol(sentence):
    sentence = sentence.strip().lower()

    # Handle sentence structures
    if "is both" in sentence and "and" in sentence:
        return translate_bachelor_and_married(sentence)

    if "is the mother of" in sentence:
        return translate_mother_of(sentence)

    if "are both students" in sentence:
        return translate_both_students(sentence)

    if "if" in sentence and "then" in sentence:
        return translate_if_then(sentence)

    if "there is a person who knows" in sentence:
        return translate_knows_everyone(sentence)

    if "nobody is taller than themselves" in sentence:
        return translate_nobody_taller_than_themselves(sentence)

    return "Translation not available for this sentence structure."

# Helper functions for specific cases

def translate_bachelor_and_married(sentence):
    match = re.match(r"there is no ([a-zA-Z]+) who is both ([a-zA-Z]+) and ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        obj1 = match.group(2)
        obj2 = match.group(3)
        return f"¬∃x ({predicates.get(obj1)}(x) ∧ {predicates.get(obj2)}(x))"
    return "Invalid sentence structure."

def translate_mother_of(sentence):
    match = re.match(r"([a-zA-Z]+) is the mother of ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        obj = match.group(2)
        return f"Pnt({subject}, {obj})"
    return "Invalid sentence structure."

def translate_both_students(sentence):
    match = re.match(r"([a-zA-Z]+) and ([a-zA-Z]+) are both students", sentence)
    if match:
        subject1 = match.group(1)
        subject2 = match.group(2)
        return f"S({subject1}) ∧ S({subject2})"
    return "Invalid sentence structure."

def translate_if_then(sentence):
    match = re.match(r"if it is ([a-zA-Z]+), then the ground is ([a-zA-Z]+)", sentence)
    if match:
        condition = match.group(1)
        result = match.group(2)
        return f"{predicates.get(condition)} → {predicates.get(result)}(Ground)"
    return "Invalid sentence structure."

def translate_knows_everyone(sentence):
    match = re.match(r"there is a ([a-zA-Z]+) who knows every other ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        object_ = match.group(2)
        return f"∃x ∀y ({predicates.get(object_)}(y) ∧ x ≠ y → K(x, y))"
    return "Invalid sentence structure."

def translate_nobody_taller_than_themselves(sentence):
    if "nobody is taller than themselves" in sentence:
        return "∀x ¬TallerThan(x, x)"
    return "Invalid sentence structure."

# Main loop to interact with the user
def main():
    print("Enter a sentence like:")
    print("7. There is no person who is both a bachelor and married.")
    print("8. Mary is the mother of John.")
    print("9. John and Mary are both students.")
    print("10. If it is raining, then the ground is wet.")
    print("11. There is a person who knows every other person.")
    print("12. Nobody is taller than themselves.")
    print("Type 'exit' to quit.")

    sentences = [
        "There is no person who is both a bachelor and married.",
        "Mary is the mother of John.",
        "John and Mary are both students.",
        "If it is raining, then the ground is wet.",
        "There is a person who knows every other person.",
        "Nobody is taller than themselves."
    ]

    for sentence in sentences:
        print(f"Original sentence: {sentence}")
        # Translate the sentence into FOL
        fol_translation = translate_to_fol(sentence)
        print("First-Order Logic Translation:", fol_translation)

# Run the program
if __name__ == "__main__":
    main()
