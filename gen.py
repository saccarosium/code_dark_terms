import yaml
import jinja2
import os

templates_dir = "./templates/"
env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir))
theme = {}

with open("./scheme.yaml", "r") as f:
    theme = yaml.safe_load(f)
    f.close()

for filename in os.listdir(templates_dir):
    f = os.path.join("./", filename)
    tmp = env.get_template(f)
    con = tmp.render(theme)
    open(f.replace('.j2', ''), 'w').close()
    with open(f.replace('.j2', ''), 'w') as f:
        f.write(con)
        f.close()
