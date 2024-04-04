import pandas as pd
from get_hallucinations import generate_hallucination_files
import os
import tokenize
import json

hallucination_codes = 'hallucination_codes'
file_test_initial_buggy_json = 'file_test_initial_buggy.json'


class Task:
    def __init__(self, id, number_of_test):
        self.id = id
        self.number_of_test = number_of_test


hallucinations = generate_hallucination_files('../bug_types_hallucination.csv', '../bug_types.csv')
# Mise à jour des chemins vers les codes buggy
for i in range(0, hallucinations.shape[0]):
    hallucinations.at[i, 'link to repo'] = hallucinations.iloc[i]['link to repo'].replace(
        'https://github.com/arghavanMor/bugs_in_LLMs/tree/master', '../coder_eval')
    if 'buggy' not in hallucinations.iloc[i]['link to repo']:
        hallucinations.at[i, 'link to repo'] = hallucinations.iloc[i]['link to repo'] + '/buggy'

number_of_test = pd.read_csv('../number_of_test.csv')
test_dict = dict()
for i in range(0, number_of_test.shape[0]):
    test_dict[number_of_test.iloc[i]['func_name']] = Task(number_of_test.iloc[i]['_id'],
                                                          number_of_test.iloc[i]['number_of_test_cases'])
test_dict['parser_flags#'] = test_dict['parser_flags']
test_dict['parser_flags#completion'] = test_dict['parser_flags']
os.system('mkdir ' + hallucination_codes)
i = 0
file_test_dict = dict()
set_of_files = list()
# Liste des chemins pour les codes buggy
buggies = [hallucinations.iloc[i]['link to repo'] + '/' + hallucinations.iloc[i]['buggy_id'] for i in
           range(0, hallucinations.shape[0])]
for file_path in buggies:
    if os.path.isfile(file_path):
        with tokenize.open(file_path) as sf:
            file_contents = []
            content_file = open(file_path, 'r')
            task_name = file_path.split('/')[-3]

            new_file = file_path.split('/')[3] + '_' + task_name + '_' + hallucinations.iloc[i]['buggy_id'].replace(
                '.py', '') + '_' + str(test_dict[task_name].id + '.py')
            file_test_dict[new_file] = task_name + '_' + str(test_dict[task_name].id) + '.py'
            if task_name == 'parser_flags#' or task_name == 'parser_flags#completion':
                file_test_dict[new_file] = 'parser_flags_' + str(test_dict['parser_flags'].id + '.py')
            buggy_file = open(hallucination_codes + '/' + new_file, 'w')
            buggy_file.write(content_file.read())
            content_file.close()
            buggy_file.close()
            i = i + 1

with open(file_test_initial_buggy_json, "w") as outfile:
    json.dump(file_test_dict, outfile)
for file in set_of_files:
    print(file)
