import json

try:
    import xmltodict
except ImportError:
    raise ImportError('A module required is not installed on your system, please run this command in your terminal: pip install xmltodict')

from numpy import deg2rad


# Dynamixel torque limit (N.m)
DXL2EFFORT = {
    'MX-28': 3.1,
    'MX-64': 7.3,
    'AX-12': 1.8
}

# Dynamixel velocity (rad/s)
DXL2VEL = {
    'MX-28': 7.,
    'MX-64': 8.2,
    'AX-12': 10.
}

# Robot color
COLOR = '0.9 0.9 0.9 1.0'  # RGB Alpha


def update_URDF_from_config(urdf_path, config_path):
    with open(urdf_path) as f:
        urdf = xmltodict.parse(f.read())

    with open(config_path) as f:
        conf = json.load(f)

    confmotors = conf['motors']
    joints = urdf['robot']['joint']
    links = urdf['robot']['link']

    # Update joint properties
    for j in joints:
        name = j['@name']
        dxl = confmotors[name]['type']
        ll, ul = confmotors[name]['angle_limit']

        j['limit']['@lower'] = str(deg2rad(ll))
        j['limit']['@upper'] = str(deg2rad(ul))
        j['limit']['@effort'] = str(DXL2EFFORT[dxl])
        j['limit']['@velocity'] = str(DXL2VEL[dxl])

    # Update link properties
    for l in links:
        l['visual']['material']['color']['@rgba'] = COLOR

    new_urdf = xmltodict.unparse(urdf, pretty=True)

    with open(urdf_path, 'w') as f:
        f.write(new_urdf)


if __name__ == '__main__':

    urdf_path = './robots/Poppy_Humanoid.URDF'
    config_path = '../../software/poppy_humanoid/configuration/poppy_humanoid.json'

    update_URDF_from_config(urdf_path, config_path)
