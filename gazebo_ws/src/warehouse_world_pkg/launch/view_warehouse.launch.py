import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    # This is the package name you created in Step 2
    pkg_name = 'warehouse_world_pkg'

    # Get the path to the package's share directory
    pkg_share = get_package_share_directory(pkg_name)

    # --- THIS IS THE CRITICAL PART ---
    # Get the path to the package's 'models' directory
    model_path = os.path.join(pkg_share, 'models')

    # Tell Gazebo where to find your custom models
    set_model_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=model_path
    )
    # --- END CRITICAL PART ---

    # Path to your world file
    world_file = os.path.join(pkg_share, 'worlds', 'my_warehouse.world')

    # Get the path to the ros_gz_sim launch file
    gz_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch'),
            '/gz_sim.launch.py'
        ]),
        # Pass your world file to Gazebo
        launch_arguments={'gz_args': f'-r {world_file}'}.items()
    )

    return LaunchDescription([
        set_model_path,  # Set the model path environment variable
        gz_sim_launch    # Launch Gazebo
    ])