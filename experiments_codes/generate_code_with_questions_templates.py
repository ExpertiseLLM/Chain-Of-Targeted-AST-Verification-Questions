import os, ast, tokenize, subprocess
from func_parser import FuncParser


def extract_id_from_file_name(file_name):
    return file_name.split('_')[-1].replace('.py', '')


buggy_code_with_questions = 'buggy_questions_with_templates/buggy_code_with_question_template_'
for i in range(5):
    os.system('mkdir ' + buggy_code_with_questions + str(i + 1))

output = subprocess.run(['ls', 'new_hallucination_codes'],
                        text=True,
                        capture_output=True)
buggies = output.stdout.split('\n')
buggies.remove('')

os.system('mkdir ' + buggy_code_with_questions)
i = 0
file_test_dict = dict()
for file_path in buggies:
    path_buggy_file = 'new_hallucination_codes/' + file_path
    for i in range(5):
        if os.path.isfile(path_buggy_file):
            with tokenize.open(path_buggy_file) as sf:
                source_file_before = sf.read()
        try:
            ast_before = ast.parse(source_file_before)
        except:
            continue
        bf_obj = FuncParser()
        bf_tree = ast.parse(ast_before)
        content_file = open(path_buggy_file, 'r')

        example = open('../initial_prompt_for_update_code.txt', 'r')
        file_with_questions = open(buggy_code_with_questions + str(i + 1) + '/' + file_path.replace('.py','.txt'), 'a+')
        attribute_question_template = open(
            'template_questions/attribute_error_quesitons/rephrased_attribute_' + str(i + 1) + '.txt', 'r')
        method_template_question = open(
            'template_questions/function_error_questions/rephrased_function_' + str(i + 1) + '.txt', 'r')
        attribute_question = attribute_question_template.read()
        method_question = method_template_question.read()

        file_with_questions.write(example.read())
        file_with_questions.write('\n<code>\n')
        file_with_questions.write(content_file.read())
        content_file.close()
        try:
            bf_obj.visit(bf_tree)
        except:
            continue
        # print('File Name ' + file_path + ' --- ' + str(bf_obj.attributes))
        file_with_questions.write('\n<questions>\n')
        file_with_questions.write(
            attribute_question.replace('<attribute-nodes>', ', '.join(bf_obj.attributes)) if len(
                bf_obj.attributes) > 0 else '')
        file_with_questions.write(
            method_question.replace('<functions-name>', ', '.join(bf_obj.methodAttributes)) if len(
                bf_obj.methodAttributes) > 0 else '')
        file_with_questions.write('\n<correction>\n')
        file_with_questions.close()
