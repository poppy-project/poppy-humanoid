import os

# Remove parts that should not be 3D printed:
JUNK = ['dynamixel_AX', 'dynamixel_x28', 'dynamixel_x64',
        'BIOLOID', 'SMPS2Dyn',
        'AX12_horn', 'trust_washer', 'HN07-N1', 'HN07-i1', 'HN05-N1', 'HN05-i1', 'HN05-T1',
        'BHS_M2', 'MF1', 'CAP', 'WB', '1226T',
        'Videw', 'Visaton', 'Odroid']

# sort and rename parts to be 3D printed
TRUNK_PARTS_FOLDER = 'trunk'
TRUNK_NAME_MAPPING = {
    'double_rotation-1 double_rotation_link-1': 'MX64_double_rotation_link',
    'double_rotation-1 i101-Set_to_MX_link': 'i101_to_MX64_link',
    'abdomen-1':'abdomen',
    'spine-1': 'spine',
    'double_rotation-2 double_rotation_link-1': 'MX28_double_rotation_link',
    'double_rotation-2 i101-Set_to_MX_link': 'i101_to_MX28_link',
    'chest-1': 'chest',
}

ARMS_PARTS_FOLDER = 'arms'
ARMS_NAME_MAPPING = {
    'forearm-1 hand-1': 'hand_left',
    'forearm-1 forearm-1': 'forearm_left',
    'shoulder-1' : 'shoulder_left',
    'forearm-2 hand-1': 'hand_right',
    'forearm-2 forearm-1': 'forearm_right',
    'shoulder-2' : 'shoulder_right',
    'shoulder_x-1 arm_connector-1': 'arm_connector',
    'upper_arm-1 upper_arm-1': 'upper_arm',
}

LEGS_PARTS_FOLDER = 'legs'
LEGS_NAME_MAPPING = {
    'hip_main_motor-1 hip_z_to_hip_y': 'hip_z_to_hip_y-connector',
    'hip-1 hip-1': 'hip_left',
    'thigh-1 thigh-1': 'thigh_left',
    'simple_foot-1': 'simple_foot_left',
    'hip-2 hip-1': 'hip_right',
    'thigh-2 thigh-1': 'thigh_right',
    'simple_foot-2': 'simple_foot_right',
    'shin-1 shin-1': 'shin',
    'pelvis-1 pelvis-1' : 'pelvis'
}

HEAD_PARTS_FOLDER = 'head'
HEAD_NAME_MAPPING = {
    'neck-1': 'neck',
    'camera_support': 'camera_support',
    'screen_support': 'screen_support',
    'head-1 screen-1' : 'screen',
    'speaker_left': 'speaker_left',
    'speaker_right': 'speaker_right',
    'head_back': 'head_back',
    'head_face': 'head_face',
    'fake_manga_screen': 'fake_manga_screen',
}


def delete_stl_files(stl_folder_path, pattern_to_delete):
    exported_stl_files = os.listdir(stl_folder_path)

    for filename in exported_stl_files:
        for name in pattern_to_delete:
            if name in filename:
                # try:
                os.remove(os.path.join(stl_path, filename))
                print '{} removed'.format(filename)
                # except OSError:
                #     raise 'A problem occured during the removing of {}'.format(filename)


def rename_stl_files(stl_folder_path, name_mapping, dest_path=None, specific_folder=None):
    if dest_path is None:
        dest_path = '.'

    if specific_folder is None:
        specific_folder = '.'

    exported_stl_files = os.listdir(stl_folder_path)
    destination_path = os.path.join(stl_folder_path, dest_path, specific_folder)

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    for filename in exported_stl_files:
        for name, new_name in name_mapping.iteritems():
            if name in filename:
                # try:
                print '{} moved'.format(new_name)
                os.rename(os.path.join(stl_folder_path, filename), os.path.join(destination_path, new_name + '.STL'))
                # except OSError as err:
                #     print("OS error: {0}".format(err))

if __name__ == '__main__':
    RAW_STL_FOLDER = '.'
    OUTPUT_STL_FOLDER = 'STL_3D_printed_parts'

    stl_path = os.path.join('.', RAW_STL_FOLDER)

    delete_stl_files(stl_path, JUNK)

    rename_stl_files(stl_path, TRUNK_NAME_MAPPING, OUTPUT_STL_FOLDER, TRUNK_PARTS_FOLDER)
    rename_stl_files(stl_path, ARMS_NAME_MAPPING, OUTPUT_STL_FOLDER, ARMS_PARTS_FOLDER)
    rename_stl_files(stl_path, LEGS_NAME_MAPPING, OUTPUT_STL_FOLDER, LEGS_PARTS_FOLDER)
    rename_stl_files(stl_path, HEAD_NAME_MAPPING, OUTPUT_STL_FOLDER, HEAD_PARTS_FOLDER)

    delete_stl_files(stl_path, ['.STL', ])
