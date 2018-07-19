import os
import json
from functools import lru_cache

class ConfigDeepSpeech:
    
    @lru_cache(maxsize=32)
    def get_config(self, key):
        print('inside module')
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'config.json')
        
        with open(file_path, 'r') as f:
            config = json.load(f)
            
        root_dir = str(os.path.abspath(os.path.join(module_dir, '../../')))
        ds_config = config['deepspeech']
        model = root_dir + ds_config['model']
        alphabet = root_dir + ds_config['alphabet']
        lm = root_dir + ds_config['lm']
        trie = root_dir + ds_config['trie']
        audiofiledir = root_dir + ds_config['audiofiledir']
        audiofilelength = ds_config['audiofilelength']
        debug = ds_config['debug']
        if key == 'model':
            return model
        elif key == 'alphabet':
            return alphabet
        elif key == 'lm':
            return lm
        elif key == 'trie':
            return trie
        elif key == 'audiofiledir':
            return audiofiledir
        elif key == 'audiofilelength':
            return audiofilelength
        elif key == 'debug':
            return debug
        else:
            raise Exception('Invalid key value.')
        