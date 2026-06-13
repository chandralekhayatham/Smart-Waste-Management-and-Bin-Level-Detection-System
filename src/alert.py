def get_status(fill_percentage):

    if fill_percentage >= 80:
        return "FULL"

    elif fill_percentage >= 50:
        return "HALF FULL"

    else:
        return "EMPTY"