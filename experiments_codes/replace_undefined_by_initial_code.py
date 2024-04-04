import subprocess

corrected_codes = 'corrected_codes_v3'
output = subprocess.run(['ls', corrected_codes],
                        text=True,
                        capture_output=True)

corrected_files = output.stdout.split('\n')
corrected_files.remove('')

for corrected_file in corrected_files:
    f = open(corrected_codes + '/' + corrected_file, 'r')
    content = f.read()
    f.close()
    if '<undefined>' in content:
        initial_file = open('new_hallucination_codes/' + corrected_file, 'r')
        file_to_replace_content = open(corrected_codes + '/' + corrected_file, 'w')
        file_to_replace_content.write(initial_file.read())
        initial_file.close()
        file_to_replace_content.close()
