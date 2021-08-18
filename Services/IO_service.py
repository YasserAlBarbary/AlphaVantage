def get_input_from_user_int(cli_text="") -> int:
    try:
        return int(input(cli_text))
    except:
        raise ValueError("An integer was expected, please restart!")


def get_input_from_user_str(cli_text="") -> str:
    try:
        return input(cli_text)
    except:
        raise IOError("Something went wrong, please try again!")
