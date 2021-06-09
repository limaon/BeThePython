# Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't privide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name("alvaro", "oLiveIra"))

