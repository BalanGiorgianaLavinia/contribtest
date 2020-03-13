# generate site from static pages, loosely inspired by Jekyll
# run like this:
#   ./generate.py test/source output
# the generated `output` should be the same as `test/expected_output`

# imported sys and json

import sys
import os
import logging
import jinja2
import json

log = logging.getLogger(__name__)


def list_files(folder_path):
    # return base as the name of the file without the extension
    for name in os.listdir(folder_path):
        base, ext = os.path.splitext(name)
        if ext != '.rst':
            continue
        yield os.path.join(folder_path, name), base

def read_file(file_path):
    # read file only as text
    with open(file_path, 'r') as f:
        raw_metadata = ""
        for line in f:
            if line.strip() == '---':
                break
            raw_metadata += line
        content = ""
        for line in f:
            content += line

        return json.loads(f'{raw_metadata}'), content

def write_output(name, html):
    # TODO should not use sys.argv here, it breaks encapsulation
    # creates the folder if it does not exist
    path = sys.argv[2]
    if not os.path.exists(path):
        os.makedirs(path)

    with open(os.path.join(path, name +'.html'), "w") as f:
        f.write(html)

def generate_site(folder_path):
    log.info("Generating site from %r", folder_path)
    # aded jinja2.FileSystemLoader
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(folder_path + 'layout'))
    
    # save the new return value for name
    for file_path, name in list_files(folder_path):
        metadata, content = read_file(file_path)
        # it should have been 'layout', not ;template'
        template_name = metadata['layout']
        template = jinja_env.get_template(template_name)
        data = dict(metadata, content=content)
        # call to render function, not on the object
        html = template.render(**data)
        write_output(name, html)
        log.info("Writing %r with template %r", name, template_name)


def main():
    generate_site(sys.argv[1])


if __name__ == '__main__':
    logging.basicConfig()
    main()
