from xmltodict import parse
import json


def parsed_to_json(func):
    def wrapper(*args, **kwargs):
        xml = func(*args, **kwargs)
        return json.dumps(parse(xml), indent=4)
    return wrapper


@parsed_to_json
def read_xml(file_path):
    xml = open(file_path)
    return "".join(xml.readlines())


result_json = read_xml("adapter/CDs.xml")  # replace CDs with food and see the marvel!
print(result_json)


