# Cloud One CSV Computer *Manager* Example

- [Cloud One CSV Computer *Manager* Example](#cloud-one-csv-computer-manager-example)
  - [Setup](#setup)
  - [Support](#support)
  - [Contribute](#contribute)

Based on a given CSV file, this little example script can modify settings on the computer objects in Workload Security. The same principle can be applied to all other classes within Workload Security.

> ***Note:*** This script is at *ALPHA* stage which means, that not all required functionalities are implemented yet. Additionally it is *NOT* tested in production environments as of now.

## Setup

1. Ensure to have the dependencies satisfied

    ```sh
    pip install -r requirements.txt
    ```

2. Create a api endpoint url and api key configuration.

    ```sh
    $ sudo bash -c 'echo "<YOUR CLOUD ONE REGION>.cloudone.trendmicro.com" > /etc/cloudone-credentials/c1_url'
    $ sudo bash -c 'echo "<YOUR CLOUD ONE API KEY>" > /etc/cloudone-credentials/api_key'
    ```

3. Place the csv file next to the python script. Currently the file name is hardcoded to `ips_status.csv`

    ```csv
    id;state;events
    1090;on, detect;0
    4711;on, detect;5
    ```

4. Run the script by

    ```sh
    python3 mgr.py
    ```

The script will automatically enable IPS in prevent mode on the listed computers if the column events is `0`.

## Support

This is an Open Source community project. Project contributors may be able to help, depending on their time and availability. Please be specific about what you're trying to do, your system, and steps to reproduce the problem.

For bug reports or feature requests, please [open an issue](../../issues). You are welcome to [contribute](#contribute).

Official support from Trend Micro is not available. Individual contributors may be Trend Micro employees, but are not official support.

## Contribute

I do accept contributions from the community. To submit changes:

1. Fork this repository.
1. Create a new feature branch.
1. Make your changes.
1. Submit a pull request with an explanation of your changes or additions.

I will review and work with you to release the code.
