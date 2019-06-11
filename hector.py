import copy
import yaml
from mitmproxy import ctx


class Hector:

    def __init__(self):
        self._output = {}

    def load(self, loader):
        loader.add_option(
                name='hector_template',
                typespec=str,
                default='./hector_template.yaml',
                help='Yaml file to be used as base for swagger output.')

        loader.add_option(
                name='hector_output',
                typespec=str,
                default='./output.yaml',
                help='Yaml file where the generated swagger will be output.')

        loader.add_option(
                name='hector_input',
                typespec=str,
                default='',
                help='Swagger yaml file to be loaded and added to.')

    def running(self):
        with open(ctx.options.hector_template) as template:
            self._template = yaml.load(template, Loader=yaml.Loader)

        if ctx.options.hector_input != '':
            with open(ctx.options.hector_input, 'r') as swagger:
                for doc in yaml.load_all(swagger, Loader=yaml.Loader):
                    print(doc)
                    self._output[doc['host']] = doc

    def done(self):
        with open(ctx.options.hector_output, 'w') as output:
            print(yaml.dump_all(self._output.values(),
                                Dumper=yaml.Dumper), file=output)

    def request(self, flow):
        request = flow.request

        if request.host not in self._output:
            self._output[request.host] = copy.deepcopy(self._template)

        target = self._output[request.host]
        target['host'] = request.host

        if request.scheme not in target['schemes']:
            target['schemes'].append(request.scheme)

        if request.path not in target:
            target['paths'][request.path] = {}


addons = [
    Hector()
]
