import subprocess, os, time
from openai import OpenAI

buggy_code_with_questions = 'new_hallucination_codes'
corrected_codes = 'improved_corrected_codes'
output = subprocess.run(['ls', buggy_code_with_questions],
                        text=True,
                        capture_output=True)
question_files = output.stdout.split('\n')
question_files.remove('')
os.system('mkdir ' + corrected_codes)
client = OpenAI(api_key='<OPENAI-API-KEY>')
os.system('mkdir improved_code_runs')
for j in range(4,5,1):
    corrected_codes = 'improved_code_runs/improved_run_'+str(j)
    os.system('mkdir ' +corrected_codes )
    i = 0
    for question_file in question_files:
        i = i + 1
        print(str(j+1) + '/5----------------------- ('+str(i)+'/'+str(len(question_files))+') -------------')
        print('Treating file '+ question_file )
        print('-------------------------------------------------------------------------------')
        content = open(buggy_code_with_questions + '/' + question_file, 'r')
        instruction = '\n Please can you improve this code or correct the bugs ? \n'
        initial_messages = [
            {"role": "user", "content": content.read() + instruction}
        ]
        completion = client.chat.completions.create(
            seed=42+j,
            temperature=0.8,
            model="gpt-3.5-turbo",
            messages=initial_messages
        )
        f = open(corrected_codes + "/" + question_file, "w")
        answer = completion.choices[0].message.content
        f.write(answer)
        f.close()
        time.sleep(1)
