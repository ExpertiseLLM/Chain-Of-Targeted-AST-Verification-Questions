import os, json, subprocess

generated_code_runs_root = "correction_templates_run5"
sub_codes = "template_"

with open('file_test_initial_buggy.json') as json_file:
    file_test_dict = json.load(json_file)


i = 0
for j in range (1,6,1):
    generated_corrected_code = generated_code_runs_root + '/' + sub_codes+str(j)+'_py'
    file_to_be_tested = generated_code_runs_root + '/test_'+sub_codes+str(j)
    os.system('mkdir ' + file_to_be_tested)
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
