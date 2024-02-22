from typing import List

MOVE_GROUP_ARM: str = "ur_manipulator"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [0.04, 0.04]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [0.0, 0.0]

def move_group_arm(prefix="", robot_name="ur"):
    return f"{prefix}{robot_name}_manipulator"

def joint_names(prefix="") -> List[str]:
    return [
        f"{prefix}shoulder_pan_joint",
        f"{prefix}shoulder_lift_joint",
        f"{prefix}elbow_joint",
        f"{prefix}wrist_1_joint",
        f"{prefix}wrist_2_joint",
        f"{prefix}wrist_3_joint"
    ]


def base_link_name(prefix="") -> str:
    return f"{prefix}base_link"


def end_effector_name(prefix="") -> str:
    return f"{prefix}tool0"


def gripper_joint_names() -> List[str]:
    return []
