"""
def occupied(parking_spaces, y, t):
    int(parking_spaces)
    char_list = list(y)
    char_list2 = list(t)
    number_of_spots_that_remained_occupied = 0
    for i in range(len(char_list)):
        if char_list[i] == char_list2[i]:
            number_of_spots_that_remained_occupied += 1
    print(number_of_spots_that_remained_occupied)
occupied(8,"CCCCC...", "C.C.C.C.")
"""
"""
language = ""
lines_to_be_expected = input("How many lines of text are you going to input?: ")
language_sample_text = input("Put your text here if you want its language to be determined: ")
x  = list(language_sample_text)
def eng_or_fren_determiner():
    s_count = 0
    t_count = 0
    for char in x:
        if char == "s" or char == "S":
            s_count += 1
        elif char == "t" or char == "T":
            t_count += 1
    if s_count >= t_count:
        language = "French"
    elif t_count > s_count:
        language = "English"
    print(language)
eng_or_fren_determiner()
"""

def HONI_block_counter(x):
    HONI_block_count = 0
    H_count = 0
    O_count = 0
    N_count = 0
    I_count = 0
    y = x.upper()
    z = list(y)
    for letter in y:
        if letter == "H":
            H_count += 1
        if H_count > O_count:
            if letter == "O":
                O_count += 1
        if O_count > N_count:
            if letter == "N":
                N_count += 1
        if N_count > I_count:
            if letter == "I":
                I_count += 1
        if H_count >= 1 and O_count >= 1 and N_count >= 1 and I_count >= 1:
            HONI_block_count += 1
            H_count = O_count = N_count = I_count = 0
    print(HONI_block_count)
HONI_block_counter("PROHODNIHODNIK")
