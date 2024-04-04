import json
import os
import csv

llm='PanGu-Coder'
with open(f'Raw-sample10-{llm}.jsonl', 'r') as json_file:
    json_list = list(json_file)
with open(f'CoderEval4Python.json', 'r') as json_file:
    json_ = json.load(json_file)['RECORDS']

if not os.path.isdir(llm):
   os.mkdir(llm)

with open(f'{llm}-samples.csv', 'w') as csvwriter:
 writer = csv.writer(csvwriter, delimiter=";")
 writer.writerow(['path_repo', 'func_name', 'path_buggy', 'buggy_id', 'level'])
 for json_str in json_list:
    result = json.loads(json_str)

    found = False
    for entry in json_:
      if entry['_id'] == result['ques_id']:
         found = True
         break 

    assert found, "Error"

    if result['level'] not in ['self_contained', 'slib_runnable', 'plib_runnable']:
       continue
    if not(os.path.isdir(os.path.join(llm, result['level']))):
      os.mkdir(os.path.join(llm, result['level']))

    # Creating function under test directory
    if not(os.path.isdir(os.path.join(llm, result['level'], result['name']))):
       dir = os.path.join(llm, result['level'], result['name'])
       os.mkdir(os.path.join(dir))
    else:
       # If same name but not same package
       if not(os.path.isdir(os.path.join(llm, result['level'], result['name'] + '#' + entry['package']))):
          dir = os.path.join(llm, result['level'], result['name'] + '#' + entry['package'])
          os.mkdir(os.path.join(dir))
       else:
          # Seem to be one fork
          print(entry['name'])
          continue
    # Create oracle for the function under test
    with open(os.path.join(dir, 'oracle.py'), 'w') as f:
       f.writelines(entry['code'])

    if not(os.path.isdir(os.path.join(dir, 'buggy'))):
       os.mkdir(os.path.join(dir, 'buggy'))

    for ind, c in enumerate(result['generate_results']):
       if not(c['is_pass']):
          writer.writerow([dir, result['name'], os.path.join(dir, 'buggy'), f'buggy_{ind}.py', result['level']])
          with open(os.path.join(dir, 'buggy', f'buggy_{ind}.py'), 'w') as f:
            f.writelines(c['generate_code'])
