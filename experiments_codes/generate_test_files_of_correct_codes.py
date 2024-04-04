import os, json, subprocess

generated_corrected_code = 'correction_codes_results/result_run_5'
file_to_be_tested = 'correction_codes_results/test_result_run_5'

with open('correct_test_dict.json') as json_file:
    file_test_dict = json.load(json_file)

os.system('mkdir ' + file_to_be_tested)
i = 0
output = subprocess.run(['ls', generated_corrected_code],
                        text=True,
                        capture_output=True)
buggies = output.stdout.split('\n')
buggies.remove('')
for key in buggies:
    generated_code_file = open(generated_corrected_code + '/' + key, 'r')
    test_template_file = open('../generated_test_cases_renamed/' + file_test_dict[key], 'r')
    test_template_content = test_template_file.read()
    test_content = test_template_content.replace('<insert generated code here>', generated_code_file.read())
    file_to_test = open(file_to_be_tested+'/' + key, 'w')
    file_to_test.write(test_content)
    generated_code_file.close()
    test_template_file.close()
    file_to_test.close()