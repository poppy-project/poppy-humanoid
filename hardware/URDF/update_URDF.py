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


# Masses (kg)
MASS = {
    'pelvis': 0.18508,
    'r_hip': 0.08433,
    'r_hip_motor': 0.13848,
    'r_thigh': 0.12066,
    'r_shin': 0.11169,
    'r_foot': 0.04674,
    'l_hip': 0.08434,
    'l_hip_motor': 0.13848,
    'l_thigh': 0.12152,
    'l_shin': 0.11169,
    'l_foot': 0.04678,
    'abs_motors': 0.27838,
    'abdomen': 0.03839,
    'spine': 0.09264,
    'bust_motors': 0.15889,
    'chest': 0.27528,
    'neck': 0.00588,
    'head': 0.21260,
    'l_shoulder': 0.00838,
    'l_shoulder_motor': 0.08288,
    'l_upper_arm': 0.16814,
    'l_forearm': 0.04863,
    'r_shoulder': 0.00838,
    'r_shoulder_motor': 0.08288,
    'r_upper_arm': 0.16814,
    'r_forearm': 0.04863
}


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
        name = l['@name']
        l['visual']['material']['color']['@rgba'] = COLOR
        l['mass'] = MASS[name]

    new_urdf = xmltodict.unparse(urdf, pretty=True)

    with open(urdf_path, 'w') as f:
        f.write(new_urdf)


if __name__ == '__main__':

    urdf_path = './robots/Poppy_Humanoid.URDF'
    config_path = '../../software/poppy_humanoid/configuration/poppy_humanoid.json'

    update_URDF_from_config(urdf_path, config_path)
