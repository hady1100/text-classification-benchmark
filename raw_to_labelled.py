# import csv
# import re
# #
# with open("data/dbpedia/Location_raw.csv", "r") as fp:
#     reader = csv.reader(fp, delimiter=',')
#     table = [row for row in reader]
#     with open("data/Organization.csv", "w+") as fw:
#         fieldnames = ['class', 'abstract']
#         writer = csv.DictWriter(fw, fieldnames=fieldnames, delimiter='|')
#         for row in table:
#             if len(row) == 2:
#                 writer.writerow({'class': '2', 'abstract': row[1]})
#             else:
#                 print len(row)
#
# tb = []
# with open("data/Organization.csv", "r") as fp:
#     reader = csv.reader(fp, delimiter='|')
#     tb = [row for row in reader]
#     for row in tb:
#         if len(row) != 2:
#             print(len(row))
#     # print x
# #
# import numpy as np
# CONST_WIKI_ALL = "data/Organization.csv"
#
# dataset = np.genfromtxt(CONST_WIKI_ALL, delimiter="|", skip_header=1,
# dtype=None)
#
# print dataset