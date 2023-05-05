""" 
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 1 - Implement a groupAndSortOwners function that:
Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name (i.e. grouped by
owner name), in alphabetical order of file names.
For example, for dictionary {'Input.txt': 'Albert', 'Code.py': 'Stanley', 'Output.txt':
'Albert','btech.txt' : 'Albert'} the groupAndSortOwners function should return {'Albert':
['btech.txt', 'Input.txt', 'Output.txt'], 'Stanley': ['Code.py']}
"""

def groupAndSortOwners(files: dict) -> dict:

    owners = dict()

    for file, owner in files.items():
        owners[owner] = owners.get(owner, []) + [file]

    for owner in owners.keys():
        owners[owner] = sorted(owners[owner], key = lambda s: s.lower())

    return owners


print(groupAndSortOwners({'Input.txt': 'Albert', 'Code.py': 'Stanley', 'Output.txt':
'Albert', 'btech.txt' : 'Albert'}))