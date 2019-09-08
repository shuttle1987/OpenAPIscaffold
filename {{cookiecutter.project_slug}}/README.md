# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description}}

## License

{% if cookiecutter.open_source_license != "Not open source" %}
This project uses the {{cookiecutter.open_source_license}} licence. Please see the `LICENSE` file for more details.
{% endif %}

## Running the development server

Make sure that the virtual environment you are running has the requirements installed then run:

```bash
python dev_server.py
```

## Running the test suite

The requirements for the test suite can be found in test_requirements.txt

```bash
pip install -r test_requirements.txt
```

Make sure you have pytest installed then run the tests with:

```bash
python -m pytest .
```
