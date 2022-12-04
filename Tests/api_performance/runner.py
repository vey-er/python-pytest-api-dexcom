import json
import os
import subprocess
from datetime import datetime

import yaml
from pytz import timezone

dt = datetime.now(timezone('US/Central')).strftime("%m/%d/%Y %H:%M")


dir_path = os.path.dirname(os.path.realpath(__file__))


class Runner():

    def update_config_file(self, data):
        data = {k: v for k, v in data.items() if v is not None}  # remove null items
        # default values
        data['locustfile'] = f'{dir_path}/performance_test.py'
        data['headless'] = True
        data['csv'] = f'{dir_path}/report/report'

        if 'spawn-rate' not in data:
            data['spawn-rate'] = 1
        if 'runtime' not in data:
            data['run-time'] = '10s'
        else:
            data['run-time'] = data.pop('runtime')

        if 'users' not in data:
            data['users'] = 1
        if 'method' not in data:
            data['tag'] = 'get'
        else:
            data['tag'] = data.pop('method')
        if 'body' in data:
            json.loads(data['body'])
        if 'headers' in data:
            json.loads(data['headers'])

        with open(f'{dir_path}/config/config.yml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

        return True

    def runner(self):
        subprocess.call(['sh', dir_path + '/test_performance.sh'])

if __name__ == '__main__':
    Runner().runner()
