def sentence_to_fol(sentence):
    # Predefined mappings for predicates and structures
    predicates = {
        "is a human": "Human({})",
        "is mortal": "Mortal({})",
        "loves": "Loves({}, {})",
        "is a dog": "Dog({})",
        "is an animal": "Animal({})",
        "is the mother of": "Mother({}, {})",
        "is a student": "Student({})",
        "knows": "Knows({}, {})",
        "is taller than": "Taller({}, {})",
        "passed the exam": "PassedExam({})",
        "is a pet of": "PetOf({}, {})",
        "teaches": "Teaches({}, {})",
        "respects": "Respects({}, {})",
        "likes": "Likes({}, {})",
        "is both a bachelor and married": "(Bachelor({}) and Married({}))",
    }

    quantifiers = {
        "every": "forall",
        "all": "forall",
        "some": "exists",
        "there is": "exists",
        "nobody": "forall not",
        "no one": "forall not",
        "there is no": "not exists",
    }

    # Normalize sentence and initialize FOL
    sentence = sentence.lower()
    fol = ""

    # Handle logical connectors: "and", "if...then"
    if " and " in sentence and "is" not in sentence:
        parts = sentence.split(" and ")
        left_fol = sentence_to_fol(parts[0].strip())
        right_fol = sentence_to_fol(parts[1].strip())
        return f"({left_fol}) and ({right_fol})"

    if "if" in sentence and "then" in sentence:
        parts = sentence.split("then")
        condition = sentence_to_fol(parts[0].replace("if", "").strip())
        consequence = sentence_to_fol(parts[1].strip())
        return f"({condition}) -> ({consequence})"

    # Check for quantifiers
    for quantifier, fol_rep in quantifiers.items():
        if quantifier in sentence:
            fol += f"{fol_rep} "

    # Identify and map predicates
    for phrase, fol_rep in predicates.items():
        if phrase in sentence:
            parts = sentence.split(phrase)
            entities = [part.strip() for part in parts if part.strip()]
            if "{}" in fol_rep and len(entities) < fol_rep.count("{}"):
                return "Error: Not enough entities for the predicate."
            entities = [e.capitalize() for e in entities]  # Format entities
            fol += fol_rep.format(*entities)
            break

    return fol if fol else "Could not map the sentence to FOL."


# Main program for multiple sentences
def main():
    print("Enter sentences to translate into First-Order Logic (FOL).")
    print("Type 'done' when you are finished.\n")

    sentences = [
        "There is no person who is both a bachelor and married",
        "Mary is the mother of John",
        "John and Mary are both students",
        "If it is raining, then the ground is wet",
        "There is a person who knows every other person",
        "Nobody is taller than themselves",
    ]

    print("\nFOL Translations:\n")
    for i, sentence in enumerate(sentences, start=1):
        fol = sentence_to_fol(sentence)
        print(f"{i}. Sentence: {sentence}")
        print(f"   FOL: {fol}\n")


# Run the program
if __name__ == "__main__":
    main()
