import subprocess, os, time
from openai import OpenAI

correction_folder_root = 'correction_templates_run'
for k in range (1,6,1):
    correction_folder_rootk = correction_folder_root+str(k)
    os.system('mkdir ' + correction_folder_rootk)
    for i in range(5):
        os.system('mkdir '+correction_folder_rootk+'/template_'+str(i+1))

api_keys = ['<OPENAI-API-KEYS>']
for j in range(1,6,1):
    for k in range(5) :
        buggy_code_with_questions = 'buggy_questions_with_templates/buggy_code_with_question_template_'
        corrected_codes = correction_folder_root+str(j)+'/template_'+str(k+1)
        output = subprocess.run(['ls', buggy_code_with_questions+str(k+1)],
                                text=True,
                                capture_output=True)
        question_files = output.stdout.split('\n')
        question_files.remove('')
        i = 0
        for question_file in question_files:
            client = OpenAI(api_key=api_keys[0])
            i = i + 1
            print('seed = '+str(41+j)+'---------'+str(j)+'/5------------ ('+str(k+1)+'/5 ---- '+str(i)+'/'+str(len(question_files))+') -------------')
            print('Treating file '+ question_file )
            print('-------------------------------------------------------------------------------')
            content = open(buggy_code_with_questions+str(k+1) + '/' + question_file, 'r')
            if(os.path.isfile(corrected_codes + "/" + question_file)):
                print(corrected_codes + '/' + question_file + ' exists ')
                continue
            initial_messages = [
                {"role": "user", "content": content.read()}
            ]
            completion = client.chat.completions.create(
                seed=41+j,
                temperature=0.8,
                model="gpt-3.5-turbo",
                messages=initial_messages
            )

            f = open(corrected_codes + "/" + question_file, "w")
            answer = completion.choices[0].message.content
            f.write(answer)
            f.close()
            time.sleep(1)