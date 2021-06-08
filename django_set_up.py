

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

    #TODO 1. replace 'myapp' in views.py and project urls w/ app name 2. change settings.py
    #TODO 3? put bootstrap and jquery and stuff in there

if bootstrap_it:
    js_dir = os.path.join(project_root, 'staticfiles', 'js')
    Path(js_dir).mkdir(parents=True, exist_ok=True)

    css_dir = os.path.join(project_root, 'staticfiles', 'css')
    Path(css_dir).mkdir(parents=True, exist_ok=True)

    img_dir = os.path.join(project_root, 'staticfiles', 'img')
    Path(img_dir).mkdir(parents=True, exist_ok=True)
