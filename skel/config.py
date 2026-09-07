import os

package_directory = os.path.dirname(os.path.abspath(__file__))

skel_folder = os.path.expanduser(
    os.environ.get(
        "SKEL_MODEL_PATH",
        os.path.join(package_directory, "../data/skel"),
    )
)

smpl_folder = os.path.expanduser(
    os.environ.get(
        "SMPL_MODEL_PATH",
        os.path.join(package_directory, "../data"),
    )
)

fitting_mask_file = os.path.join(
    package_directory,
    "alignment/riggid_parts_mask.pkl",
)

default_config_file = os.path.join(
    package_directory,
    "alignment/config.yaml",
)
