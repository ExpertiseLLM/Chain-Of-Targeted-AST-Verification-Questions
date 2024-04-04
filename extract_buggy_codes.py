# import os
# import pandas as pd
# import subprocess
#
# path = "Bugs_in_LLMs_Hallucinations.xlsx"
# to_replace_link = 'https://github.com/arghavanMor/bugs_in_LLMs/tree/master/'
# replace_string = ''
# buggy_codes_files_datasheet = pd.read_excel(path,sheet_name=1)
# new_root_paths = [file.replace(to_replace_link, replace_string) for file in buggy_codes_files_datasheet['link_to_file']]
# buggy_codes_files_datasheet['file'] = new_root_paths;
# buggy_codes_files_datasheet['file'] = buggy_codes_files_datasheet['file']+'/buggy/'+buggy_codes_files_datasheet['buggy_id']
# print(buggy_codes_files_datasheet['file'][0])
# os.system('mkdir buggy_codes')
# i = 0
# for path in buggy_codes_files_datasheet['file']:
#     subprocess.run(['cp',path,'buggy_codes/buggy_'+str(i)+'.py'])
#     i = i + 1
#
#
