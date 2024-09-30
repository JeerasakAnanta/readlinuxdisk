import os

def read_disk_linux(mount_point):
    """
    This function reads the total, used and available disk space on Linux.

    It uses the os.statvfs() function to get the disk stats from the root
    partition. The result is returned as a tuple of three values: the
    percentage of the disk that is used, the total number of bytes that can
    be stored on the disk, and the number of bytes that are available.

    :param str mount_point: The mount point of the partition to be read.
    :return: A tuple of (percent, capacity, available)
    :rtype: tuple
    """

    # Get the stats of the disk
    disk = os.statvfs(mount_point)

    # Calculate the total capacity of the disk
    capacity = disk.f_bsize * disk.f_blocks

    # Calculate the available disk space
    available = disk.f_bsize * disk.f_bavail

    # Calculate the used disk space
    used = capacity - available

    # Calculate the percentage of the disk that is used
    percent = (used / capacity) * 100

    # Round the percentage to two decimal places
    percent = round(percent, 2)

    # Return the percentage of the disk that is used, the total capacity of the
    # disk, and the available disk space as a tuple
    return percent, capacity, available


print(read_disk_linux("/")) 

