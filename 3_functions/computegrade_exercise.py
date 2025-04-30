#Rewrite the grade program from the previous chapter using  a function called computegrade that takes a score
# as its parameter and returns a grade as a string.

def computegrade(score):
    try:
        score = float(score)

        if score < 0.0 or score > 1.0:
            return "Error: Score must be between 0.0 and 1.0"

        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"

    except Exception as e:
        return f"Invalid input: {e}"

