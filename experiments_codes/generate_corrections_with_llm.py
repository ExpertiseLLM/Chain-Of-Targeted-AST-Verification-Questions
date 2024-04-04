import subprocess, os, time
from openai import OpenAI

temperatures = [0.8]
os.system('mkdir correction_codes_results')
for j in range(0, 5, 1):
    for temperature in temperatures:
        buggy_code_with_questions = 'correct_codes_with_questions'
        corrected_codes = 'correction_codes_results/result_run_' + str(j+1)
        output = subprocess.run(['ls', buggy_code_with_questions],
                                text=True,
                                capture_output=True)
        question_files = output.stdout.split('\n')
        question_files.remove('')
        os.system('mkdir ' + corrected_codes)
        client = OpenAI(api_key='<OPENAI-API-KEYS>')
        i = 0
        for question_file in question_files:
            i = i + 1
            print('----'+str(j+1)+'/5---------------------- (' + str(i) + '/' + str(len(question_files)) + ') -------------')
            print('Treating file ' + question_file)
            print('-------------------------------------------------------------------------------')
            content = open(buggy_code_with_questions + '/' + question_file, 'r')
            initial_messages = [
                {"role": "user", "content": content.read()}
            ]
            completion = client.chat.completions.create(
                seed=42 + j,
                temperature=0.8,
                model="gpt-3.5-turbo",
                messages=initial_messages
            )
            f = open(corrected_codes + "/" + question_file, "w")
            answer = completion.choices[0].message.content
            f.write(answer)
            f.close()
            time.sleep(1)
