

import subprocess, os
from pathlib import Path
from shutil import copyfile
#https://stackoverflow.com/questions/123198/how-can-a-file-be-copied


project_root = r'C:\Users\aiden\Desktop\test_django'
project_name = project_root.split('\\')[-1]
app_name = 'my_dumb_app'
bootstrap_it = False

if app_name not in os.listdir(project_root):
    output = subprocess.check_output(["python", os.path.join(project_root, "manage.py"), "startapp", app_name])
else:
    print('pizza')
    app_dir = os.path.join(project_root, app_name)
    project_settings_dir = os.path.join(project_root, project_name)
    #create urls.py, forms.py, add index to views.py
    forms_file = os.path.join(app_dir, 'forms.py')
    if not os.path.exists(forms_file):
        open(forms_file, 'w').close()

    templates_dir = os.path.join(app_dir, 'templates', app_name)
    Path(templates_dir).mkdir(parents=True, exist_ok=True)

    index_file = os.path.join(templates_dir, 'index.html')
    if not os.path.exists(index_file):
        open(index_file, 'w').close()

    copyfile('app_urls.py', os.path.join(app_dir, 'urls.py'))
    copyfile('app_views.py', os.path.join(app_dir, 'views.py'))
    copyfile('project_urls.py', os.path.join(project_settings_dir, 'urls.py'))


if bootstrap_it:
    pass
