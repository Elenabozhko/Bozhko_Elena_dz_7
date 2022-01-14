
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