#!/usr/bin/python
"""Starter code for exploring the Enron dataset (emails + finances).

loads up the dataset (pickled dict of dicts).
The dataset has the form:
enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
{features_dict} is a dictionary of features associated with that person.
You should explore features_dict as part of the mini-project,
but here's an example to get you started:

enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl",
                         'r'))

n_poi = sum(1 for x in enron_data.values() if x['poi'])
n_poi_no_comp = sum(1 for x in enron_data.values()
                    if (x['poi'] and x['total_payments'] == 'NaN'))
n = len(enron_data)
n_no_comp = sum(1 for x in enron_data.values()
                if x['total_payments'] == 'NaN')
print n_poi
print n, n_no_comp

print 'Number pois with no total comp: \
        {}, {:.2%}'.format(n_poi_no_comp, n_poi_no_comp * 1.0 / n_poi)

# print len(enron_data)
# print len(enron_data["SKILLING JEFFREY K"])
# print enron_data["SKILLING JEFFREY K"]
# print enron_data["SKILLING JEFFREY K"]["poi"]
n_salary = 0
n_email = 0
for d in enron_data:
    if enron_data[d]['email_address'] != 'NaN':
        n_email += 1
    if enron_data[d]['total_payments'] == 'NaN':
        n_salary += 1

        # print r'{name} : {total_payments:n}'
        # .format(name = d, total_payments = enron_data[d]['total_payments'])
        # n_poi+=1
res = 1.0 * n_salary / len(enron_data)
print res
print 'Count salary : {}'.format(n_salary)
print 'Count data : {}'.format(len(enron_data))
print '{n_miss_pay} \
        missing people with salary which represent {perc:.2%} \
        of overall'.format(n_miss_pay=n_salary, perc=res)
print n_email
name = 'Jeffrey Skilling'
n = str.split(name, ' ')
name = n[1].upper() + ' ' + n[0].upper()
name = 'SKILLING JEFFREY K'
print enron_data[name]

# import re
# exp = r'\([y|n]\)'
#
# i = 0
# j = 0
# with open("../final_project/poi_names.txt") as f:
#     for line in f:
#         print line
#         match = re.match(exp, line)
#         if match:
#             i += 1
#             if match.group() == "(y)":
#                 j +=1
# print 'We found %d POI in the file, and %d with matching emails' % (i, j)
