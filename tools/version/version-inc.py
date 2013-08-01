#!/usr/bin/env python3
from string import Template
import argparse
import json


def read_configuration(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config


def write_configuration(config, config_file):
    output_order = ['project_name', 'company_name',
        'version_major', 'version_minor', 'version_build']
    ordering = dict()
    for (oid, field_name) in enumerate(output_order):
        ordering[field_name] = oid

    outlist = []
    for k in sorted(config.keys(), key=lambda k: ordering[k]):
        outlist.append(json.dumps({k: config[k]}))
    outlist = "{\n\t" + ",\n\t".join((s[1:-1] for s in outlist)) + "\n}"

    #s = "[" + ",".join(outlist) + "]"
    with open(config_file, 'w') as f:
        f.write(outlist)


def read_template(template_file):
    with open(template_file, 'r') as f_template:
        template = Template(f_template.read())
    return template


def write_output(filename, content):
    with open(filename, 'w') as f:
        f.write(content)


def parse_version(target_version):
    try:
        versions = target_version.split('.')
        (major, minor, build) = (int(v) for v in versions)
    except:
        raise ValueError("version must be in format like '1.0.0'.")
    return (major, minor, build)


def set_version(config, options):
    if options.target_version is not None:
        # set version to the designated value.
        (major, minor, build) = parse_version(options.target_version)
        config['version_major'] = major
        config['version_minor'] = minor
        config['version_build'] = build
    elif options.increase_major:
        # increase major version, reset minor and build.
        config['version_major'] += 1
        config['version_minor'] = 0
        config['version_build'] = 0
    elif options.increase_minor:
        # increase minor version and reset build.
        config['version_minor'] += 1
        config['version_build'] = 0
    else:
        # increase build version by 1.
        config['version_build'] += 1
    return config


def main():
    # Parse options
    usage = "%(prog)s [options]"
    description = "Increase version and generate a header file."
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument("-i", "--input", dest="config_file",
                      action="store", metavar="<config-file>",
                      help="read current versioning from <config-file>")
    parser.add_argument("-o", "--output", dest="output_file",
                      action="store", metavar="<file>",
                      help="write header file output to <file>. "
                      "Use 'version.h' if not specified")

    inc_group = parser.add_argument_group('Versioning Options',
                    "The build version will be increased "
                    "if none of the following options is specified.")
    inc_group.add_argument("-m", "--major-increase", dest="increase_major",
                         action="store_true", default=False,
                         help="increase major version")
    inc_group.add_argument("-n", "--minor-increase", dest="increase_minor",
                         action="store_true", default=False,
                         help="increase minor version")
    inc_group.add_argument("-s", "--set-version", dest="target_version",
                         action="store", metavar="<version>",
                         help="set to the designated <version> (e.g. 1.5.0)")

    args = parser.parse_args()

    if args.increase_major is True and args.increase_minor is True:
        parser.error('cannot increase both major version and minor version.')

    default_config_file = 'version_config.json'
    default_output_file = 'version.h'
    default_template_file = 'version.template'

    config_file = default_config_file
    output_file = default_output_file
    template_file = default_template_file
    if args.output_file is not None:
        output_file = args.output_file

    # Read the configuration file.
    config = read_configuration(config_file)

    # Set version.
    try:
        config = set_version(config, args)
    except ValueError as err:
        parser.error(err)

    # Read template, substitute, and save.
    t = read_template(template_file)
    write_output(output_file, t.safe_substitute(config))

    # save current configuration.
    write_configuration(config, config_file)

    # Prompt
    print("File generated '{0}'.".format(output_file))
    print('Current version: {0}.{1}.{2}'.format(config['version_major'],
          config['version_minor'],
          config['version_build'],))


if __name__ == '__main__':
    main()
