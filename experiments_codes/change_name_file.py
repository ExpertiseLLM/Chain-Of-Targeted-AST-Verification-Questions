import os, subprocess

root = 'correction_templates_run5'
for i in range(1,6,1):
    output = subprocess.run(['ls', root+'/template_'+str(i)],
                            text=True,
                            capture_output=True)
    buggies = output.stdout.split('\n')
    buggies.remove('')
    os.system('mkdir ' +root+'/template_'+str(i)+'_py')
    for buggy in buggies:
        initial = open(root+'/template_'+str(i)+'/'+buggy,'r')
        treated = open(root+'/template_'+str(i)+'_py/'+buggy.replace('.txt','.py'),'w')
        treated.write(initial.read())