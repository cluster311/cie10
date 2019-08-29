""" CIE dict """
import csv
import json
import os
import zipfile


class CIECodes:
    here = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(here, 'data')
    local_zip_csv = os.path.join(data_folder, 'cie-10.zip')
    local_csv = os.path.join(data_folder, 'cie-10.csv')  # robado de acá https://github.com/verasativa/CIE-10
    local_json = os.path.join(data_folder, 'cie-10.json')

    tree = {}

    def __init__(self):
        if self.tree == {}:
            self.read_json()

    def info(self, code):
        if code not in self.tree:
            code = code.replace('.', '')  # W231 == W23.1
            if code not in self.tree:
                return None
        
        ret = self.tree[code]
        descriptions = [ret['description']]
        while ret['depends_on'] is not None:
            ret = self.tree[ret['depends_on']]
            descriptions.append(ret['description'])

        ret = self.tree[code]
        ret['multiple_descriptions'] = descriptions
        ret['code'] = code
        return ret

    def read_json(self):
        # read defined JSON an load to the _self.tree_ property
        if os.path.isfile(self.local_json):
            f = open(self.local_json, 'r')
            self.tree = json.load(f)
            f.close
        else:
            self.read_csv()

    def read_csv(self):
        # read CSV and transfor to a useful JSON
        # extracts CSV if is not ready
        if not os.path.isfile(self.local_csv):
            self.extract_csv()
            
        tree = {}   # results
        fieldnames = ['code', 'code_0', 'code_1', 'code_2', 'code_3',
                      'code_4', 'description', 'level', 'source']
        f = open(self.local_csv, 'r')
        reader = csv.DictReader(f, fieldnames=fieldnames)
        next(f)  # headers
        errors = []
        for row in reader:
            # fix all shit
            for k, v in row.items():
                row[k] = v.strip().replace('–', '-')

            code = row['code']
            
            if code in self.tree:
                raise Exception('Duplicated code {}'.format(code))
            
            for coden in ['code_0', 'code_1', 'code_2', 'code_3', 'code_4']:
                rcoden = row[coden]
                if rcoden != '' and rcoden not in tree:
                    raise Exception('Missing code {}'.format(rcoden))
            
            level = int(row['level'])
            tree[code] = {'description': row['description'],
                          'source': row['source'],
                          'level': level} 
            
            depends_on_field = 'code_{}'.format(level-1)
            
            if level > 0:
                if row[depends_on_field] not in tree:
                    raise Exception('Parent node do not exists {}'.format(row[depends_on_field]))
                tree[code]['depends_on'] = row[depends_on_field]
            else:
                tree[code]['depends_on'] = None

        f.close()

        f2 = open(self.local_json, 'w')
        f2.write(json.dumps(tree, indent=2))
        f2.close

        self.tree = tree
    
    def extract_csv(self):
        with zipfile.ZipFile(self.local_zip_csv, 'r') as zip_ref:
            zip_ref.extractall(self.data_folder)
    
    def search(self, txt):
        for code, content in self.tree.items():
            full_info = self.info(code=code)
            # saca del medio, Solr
            full_str = ' '.join([str(val).lower() for key, val in full_info.items()])
            if full_str.find(txt.lower()) > -1:
                yield full_info

