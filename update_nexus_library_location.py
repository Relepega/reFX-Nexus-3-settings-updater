import json
import os.path

settings = 'C:\\Users\\Public\\Documents\\reFX\\nexus\\settings.json'

dirname = os.path.abspath(os.getcwd())

# open settings file and read existing settings
f = open(settings, 'r')
data = json.load(f)
f.close()

# modify the library folder directory
data['library_folder'] = dirname

# save settings file with modified settings
with open(settings, 'w') as f:
    f.write(json.dumps(data, indent=4))
