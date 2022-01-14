# Bozhko_Elena_dz_7
Домашнее задание по уроку 7


ДЗ 1


import os
pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)



folder = r'C:\Проекты\venv\Bozhko_Elena_dz_7\my_project'
django_dirs = [item
               for item in os.listdir(folder)
               if os.path.isdir(os.path.join(folder, item))]
print(django_dirs)




ДЗ 3


import os
import shutil
my_dir = 'task_7_3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)
    
    
    
    ДЗ4
    
    
    import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
    out_dict[10 ** len(str(file))] += 1

print(out_dict)

