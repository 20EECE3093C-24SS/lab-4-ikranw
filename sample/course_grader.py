# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """
    Convert a student's score into a letter grade.

    Arguments:
        grade's score (int or float): The numerical score of the student.

    Returns:
       a string: An upper-case string of the student's letter grade based on the argument.

    Raises:
        ValueError: If the score is outside the 0 to 100 range.
        TypeError: If the score is not an int or float.

    Example:
        >>> convert_to_letter_grade(64)
        'D'
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return 'A'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C'
    elif score >= 60 and score <= 69:
        return 'D'
    else:
        return 'F'
