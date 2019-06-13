# Hector

__Hector__ is an addon for the excellent [mitmproxy](https://mitmproxy.org)
application, which captures and generates API documentation according to the
[OpenAPI Specification](https://swagger.io/specification/).


## Setup

Create a virtual environment using your preferred method and install
dependencies. Python 3 is strongly preferred.

```shell
$ python3 -mvenv ~/env/hector
$ pip install -r requirements.txt
```


## Usage

```shell
$ mitmdump -s ./hector.py --set hector_template=template.yaml \
                          --set hector_input=input.yaml \
                          --set hector_output=output.yaml
```

__hector__ will write swagger for every host accessed during your mitmproxy
session. At the end of the session all swagger data will be written to a single
yaml file, separated by `--` per host.


## Options

### hector_template _(optional)_

This option specifies the base yaml that will be used by __hector__. You may
provide your own template, or the default, `hector_template.yaml` will be used

### hector output _(optional)_

This option specifies the file to which the swagger yaml will be written at the
end of the session. Default: `output.yaml`

### hector input _(optional)_

This option allows you to load an existing swagger yaml, perhaps to resume a
previous session. Default: `None`


## TODO

* Add parameter and response details
* Add option to filter by host or regex
* Optionally write to multiple files instead of just one
* Post-process swagger to collapse on base-path
* Add a command to trigger a write to file
