import yaml
from jinja2 import Environment, FileSystemLoader

with open('network/vars.yml', 'r') as file:
    vars = yaml.safe_load(file)

environment = Environment(loader=FileSystemLoader("network/"))
network_template = environment.get_template("vpc-and-subnets.j2")

content = network_template.render(vars)

filename = "to-deploy.yml"
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"template generated {filename}")