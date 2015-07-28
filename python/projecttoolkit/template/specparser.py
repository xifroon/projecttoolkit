import sys
import os
import os.path as path
import json
import logging

class SpecParser:
    """Static and instance parser of Template Specification JSON"""
    specification = {}
    substdict = {}

    def __init__(self, specpath, content_constructor_function, substdict={}):
        self.Logger = logging.getLogger('projecttoolkit')
        self.specpath = specpath
		self.Logger.debug('SpecParser created, parsing ' + self.specpath)

        # Extract information from path
        # TODO: Remove unnecessary field
        self.template_dir, self.specfilename = path.split(specpath)
        self.specification['name'], tail = path.splitext(self.specfilename)
        self.specdir = path.join(self.template_dir, self.specification['name'])

        self.content_constructor_function = content_constructor_function
        self.substdict.update(substdict)
        print(str(substdict))
        # Parse and save
        self.parse()

    def getmetadata(self):
        metadata = dict(self.specification)
        del metadata['content']
        return metadata

    def parse_parents_chain(self, parent_specname):
        parent_specpath = path.join(self.template_dir, parent_specname + '.json')
        self.parent_parser = SpecParser(parent_specpath,
                                        self.content_constructor_function,
                                        self.substdict)
        # Indirect double-linked list hierarchy
        self.parent_parser.child_specname = self.specname

    def parse_content(self, contentdict, depthpath=''):
        if not isinstance(contentdict, dict):
            self.Logger.error('Constructing invalid file structure:'
                         + str(contentdict))
            return

        for filename, description in contentdict.items():
            if not 'type' in description:
                description['type'] = FileCreatorHint.NewFile
            self.content_constructor_function(path.join(depthpath, filename),
                                              description,
                                              self.specification['name'])
            # Recurse on folder
            if  description['type'] == FileCreatorHint.Folder and 'content' in description:
                newdepthpath = path.join(depthpath, filename)
                self.parse_content(description['content'], newdepthpath)

    def __validate_format(self, specification):
        """Validating specification format"""
        if not 'content' in specification:
            self.Logger.warning('Spec. is invalid: no content field specified.')
            return -1
        if not 'name' in specification or specification['name'] != self.specification['name']:
            self.Logger.warning('Spec. is invalid: name unspecified or inconsistent with filename.')
            return -1
        # Valid
        return 0

    def __load_json_safe(specfd):
        try:
            self.Logger.debug('Load json: ' + specfd.abspath)
            self.specification = json.load(specfd)
        except Exception as err:
            self.Logger.warning('JSON load failed ({0}): '.format(err) + project_spec_path)
            return -1
        return 0

    def parse(self):
        # Open json file
        specpath = path.join(self.specpath)
        specfd = open(project_spec_path, 'r')
        if __load_json_safe(specfd):
            return
        if __validate_format(project_spec):
            return
        if 'inherit' in self.specification:
            self.Logger.debug('Parent type is ' + self.specification['inherit'])
            # Recursive on parent
            self.parse_parents_chain(self.specification['inherit'])
        self.parse_content(self.specification['content'])
