#!/usr/bin/python3

# Import Yamale and make a schema object:
import argparse
import os.path
import re
import sys
import yamale
from yamale.validators import DefaultValidators, Validator
from yamale.yamale_error import YamaleError

class Hexdump(Validator):
    """ Custom Date validator """
    tag = 'hexdump'

    def _is_valid(self, value):
        return self.hex_check(value)

    def hex_check(self, value):
        regex = re.compile(r'^([a-f,A-F,0-9]{2}\s){15}[a-f,A-F,0-9]{2}\n', flags=re.I)

        if len(value) <= 0:
            return False

        for i in range(48, len(value), 48):
            if not regex.match(value[i-48:i]):
                return False

        floor_div = len(value)//48
        if 48*floor_div != len(value):
            regex = re.compile(r'^([a-f,A-F,0-9]{2}\s){1,}[a-f,A-F,0-9]{2}$', flags=re.I)

            if not regex.match(value[len(value)-48:len(value)-1]):
                return False

        return True

validators = DefaultValidators.copy()  # This is a dictionary
validators[Hexdump.tag] = Hexdump

args_parser = argparse.ArgumentParser(description='Validate yaml output of the PKS analyzer.')
args_parser.add_argument('-s', '--schema', nargs='?', default='./schemas/schema-all.yaml', \
help='the path to schema')
args_parser.add_argument('-d', '--data', nargs='?', default='./examples/packets-all.yaml', \
help='the output analyzer')

args = args_parser.parse_args()

try:
    if os.path.exists(args.schema) and os.path.exists(args.data):

        schema = yamale.make_schema(args.schema, parser='ruamel', validators=validators)

        # Create a Data object
        data = yamale.make_data(args.data, parser='ruamel')

        # Validate data against the schema. Throws a ValueError if data is invalid.
        try:
            yamale.validate(schema, data)
            print("Validation success! \U0001F44D")
        except ValueError as err:
            print('Validation failed! \U0001F44E \n%s' % str(err))
            exit(1)
    else:
        raise FileExistsError("The schema or data file does not exist.")
except (YamaleError, FileExistsError) as err:
    print(err)
    sys.exit(1)
