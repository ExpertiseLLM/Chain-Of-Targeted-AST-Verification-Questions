import pandas as pd

f = open('testcasesoriginal', 'r')
content = f.read()
testcases = content.split('----------------------------')
testcases.remove('')
dictionary = dict()
for i in range(0, len(testcases)):
    testcases[i] = testcases[i].split('\n', 1)[1]
    id = testcases[i].split('\n', 1)[0]
    test = testcases[i].split('\n', 1)[1]
    dictionary[id] = test
print(dictionary['62e60f43d76274f8a4026e28'])
data_frame_test_cases = pd.DataFrame.from_dict({'_id': dictionary.keys(), 'tests': dictionary.values()})
data_frame_test_cases.to_csv('test_case.csv')
