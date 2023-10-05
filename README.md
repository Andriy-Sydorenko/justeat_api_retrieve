# Retrieving info of British restaurants by postcode

*Python package that allows to extract information about restaurants in Britain url.*

## Usage

1. Clone git repo using this command:
```shell
git clone https://github.com/Andriy-Sydorenko/justeat_api_retrieve
```

2. Open project in your IDE and create venv.
```shell
python -m venv venv
```

3. Activate venv:
- on Windows
    ```shell
    venv\Scripts\activate
    ```
- on macOS
    ```shell
    source venv/bin/activate
    ```

4. Install requirements:
```shell
pip install -r requirements.txt
```

5. You can use already prepared [main.py](C:\Users\White nigga\projects\test_tasks\justeat_api_retrieve\main.py) file to check out the functionality.

## Notes
> NOTE: to use this code, you need to use desktop VPN(Poland, Austria, Turkey, Sweden, Netherlands), e.g. [ProtonVPN](https://protonvpn.com)(Not an advertisement)

> NOTE: if you want to write restaurant data into a file, you can set `write_to_file` parameter to `True`

> NOTE: also you can specify filename, using parameter `filename` (you don't need to write file's extension, it's JSON by default).
>
> If not specified, filename will be automatically generated.

## Examples of Usage
- Specifying filename
```python
from restaurants_retrieval.justeat import Client

client = Client()
result = client.by_postal_code("NG1 1AA", filename="some_file_name", write_to_file=True)
```

- Automatically generated filename
```python
from restaurants_retrieval.justeat import Client

client = Client()
result = client.by_postal_code("NG1 1AA", write_to_file=True)
```

## Possible improvements:
- Logging and traceback libraries can be added for better exception handling
- Add built-in proxy solution so users from different countries can access target API without using desktop VPN
