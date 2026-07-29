import json
import numpy as np
import urllib.request

_SPARC_RAW = 'https://raw.githubusercontent.com/cfs-energy/SPARCPublic/main/DeviceDescription'

def fetch_json(filename):
    """Read a JSON file straight from the SPARCPublic repo, without writing it to disk."""
    print(f'Fetching {filename} from SPARCPublic...', end=' ', flush=True)
    with urllib.request.urlopen(f'{_SPARC_RAW}/{filename}') as resp:
        data = json.load(resp)
    print('done.')
    return data

SPARC_geom = fetch_json('OS_SPARC_Device_Description.json')

#
vv_inner_obj = SPARC_geom['wall']['description_2d'][1]['vessel']['unit'][0]['annular']
vv_inner = np.vstack((vv_inner_obj['outline_inner']['r'],vv_inner_obj['outline_inner']['z'])).transpose()
vv_inner_thickness = np.array(vv_inner_obj['outline_outer']['r']).max()-np.array(vv_inner_obj['outline_inner']['r']).max()

#
vv_outer_obj = SPARC_geom['wall']['description_2d'][1]['vessel']['unit'][1]['annular']
vv_outer = np.vstack((vv_outer_obj['outline_inner']['r'],vv_outer_obj['outline_inner']['z'])).transpose()
vv_outer_thickness = np.array(vv_outer_obj['outline_outer']['r']).max()-np.array(vv_outer_obj['outline_inner']['r']).max()

coil_dict = {}
for coil in SPARC_geom['pf_active']['coil']:
    filament_locations = []
    for sub_coil in coil['element']:
        filament_locations.append([sub_coil['geometry']['annulus']['r'], sub_coil['geometry']['annulus']['z']])
    coil_dict[coil['name']] = filament_locations

with open("SPARC_public_simple.json", "w+") as file:
    json.dump({
        'vv': {
            'inner': {
                'pts': vv_inner.tolist(),
                'thickness': vv_inner_thickness,
                'eta': vv_inner_obj['resistivity']
            },
            'outer': {
                'pts': vv_outer.tolist(),
                'thickness': vv_outer_thickness,
                'eta': vv_inner_obj['resistivity']
            }
        },
        'coils': coil_dict
    }, file)