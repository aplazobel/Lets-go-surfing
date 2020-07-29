import pandas as pd
import numpy as np


def bestBeach(dframe, experience_input):

    cleanup_cols = {"Wave quality_num":     {"Totally Epic": 4, "World Class": 3, "Regional Classic": 2, "Normal": 1, "Sloppy": 0},
                "Frequency_num": {"Very consistent (150 day/year)": 4, "Regular": 3, "Sometimes break": 2, "Rarely break (5day/year)": 1,
                                  "Don't know": 1 }}

    #dframe = dframe[dframe['Wave quality'].notna()]
    #dframe = dframe[dframe['Frequency'].notna()]

    dframe["Wave quality_num"] = dframe["Wave quality"]
    dframe["Frequency_num"] = dframe["Frequency"]

    dframe.replace(cleanup_cols, inplace=True)

    dframe["Score"] = dframe["Wave quality_num"] + dframe["Frequency_num"]
    dframe = dframe.drop(['Wave quality_num', 'Frequency_num'], axis=1)

    dframe = dframe.sort_values(by=['Score'], ascending=False)


    if experience_input == "Beginner":
        new_dframe = dframe[(dframe['Experience'] == "Beginners wave")|(dframe['Experience'] == "All surfers")]
    elif experience_input == "Experienced":
        new_dframe = dframe[(dframe['Experience'] == "All surfers")|(dframe['Experience'] == "Experienced surfers")]
    elif experience_input == "Advanced/Pro":
        new_dframe = dframe[(dframe['Experience'] == "All surfers")|(dframe['Experience'] == "Experienced surfers")|(dframe['Experience'] == "Pros or kamikaze only...")]

    return new_dframe.head()