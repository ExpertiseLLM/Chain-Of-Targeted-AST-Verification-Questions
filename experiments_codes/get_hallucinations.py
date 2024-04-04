import pandas as pd


def extract_hallucinations(hallucination_pd, content='allucination'):
    hallucination_pd = hallucination_pd.dropna(axis='rows')
    rows_to_keep = [x for x in range(hallucination_pd.shape[0]) if content in hallucination_pd.iloc[x]['Labels']]
    hallucination_pd = pd.DataFrame(columns=hallucination_pd.columns, data=list(hallucination_pd.values))
    hallucination_pd = hallucination_pd.drop([x for x in range(0, hallucination_pd.shape[0]) if x not in rows_to_keep])
    hallucination_pd = pd.DataFrame(columns=hallucination_pd.columns, data=list(hallucination_pd.values))
    return hallucination_pd


def generate_hallucination_files(file1, file2):
    hallucinations = pd.read_csv(file1)
    bug_types = pd.read_csv(file2)
    bug_types = bug_types.drop(['path_repo', 'path_buggy', 'Label Arghavan'], axis=1)
    bug_types = bug_types.rename(columns={'Final': 'Labels'})
    hallucinations = extract_hallucinations(hallucinations)
    bugs_typess = extract_hallucinations(bug_types, 'rong')
    bugs_types = extract_hallucinations(bug_types)
    bug_types = pd.concat([bugs_types, bugs_typess])
    bug_types = pd.DataFrame(columns=bug_types.columns, data=bug_types.values)
    hallucinations = pd.concat([hallucinations, bug_types])
    hallucinations = hallucinations.dropna(axis="rows")
    hallucinations = hallucinations.drop_duplicates()
    hallucinations = pd.DataFrame(columns=hallucinations.columns, data=hallucinations.values)
    return hallucinations
