import os, json, subprocess

with open('file_test_initial_buggy.json') as json_file:
    file_test_dict = json.load(json_file)

new_dict = dict()
output = subprocess.run(['ls', 'correct_codes_experiments'],
                        text=True,
                        capture_output=True)
correct_codes_l = output.stdout.split('\n')
correct_codes = [code for code in correct_codes_l if code != '']
print(correct_codes)
for correct_code in correct_codes:
    for test_dict in file_test_dict.keys():
        if(correct_code.split('__')[1] in test_dict):
            new_dict[correct_code] = file_test_dict[test_dict]

with open('correct_test_dict.json','w') as outfile:
    json.dump(new_dict, outfile)
