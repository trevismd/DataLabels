"""
Exctracts useful lines from DB select export to have only lines where a second
CBCT has been performed on the same day for the same treatment.
"""
import pandas as pd
import csv

# todo: integrate with other files in order to export work list per reason.


data = pd.read_csv('rad_seance.csv', sep=";", quotechar="\"",
                   names=["treatment", "date", "time", "comment"],
                   dtype=str, header=0)

data["id_date"] = data.treatment.str.cat(data.date)

not_uniques = set(data.groupby("id_date").filter(lambda x: len(x) > 1).id_date)

data_duplicated_only = data.loc[data.id_date.apply(lambda s: s in not_uniques),
                                data.columns[0:4]]

data_duplicated_only.to_csv("ok_cols_start.csv", sep=",",
                            quoting=csv.QUOTE_ALL, index=False)
