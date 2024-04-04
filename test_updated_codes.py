import os
import json
with open('file_test_dict.json') as json_file:
    file_test_dict = json.load(json_file)

os.system('mkdir file_to_be_tested_v2')
i = 0
for key in file_test_dict.keys():

    generated_code_file = open('corrected_codes/'+key+'.py', 'r')
    test_template_file = open('generated_test_cases_renamed/'+file_test_dict[key], 'r')
    test_template_content = test_template_file.read()
    test_content = test_template_content.replace('<insert generated code here>', generated_code_file.read())
    file_to_test = open('file_to_be_tested_v2/'+key, 'w')
    file_to_test.write(test_content)
    generated_code_file.close()
    test_template_file.close()
    file_to_test.close()
