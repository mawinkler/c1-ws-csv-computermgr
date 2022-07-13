import csv
import logging
import sys
from pprint import pprint as pp

from connector import CloudOneConnector

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s (%(threadName)s) [%(funcName)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

connector = CloudOneConnector()

with open("ips_status.csv") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=";")
    ips_status = {}
    keys = []
    first_line = True

    for row in csv_reader:
        if first_line:
            first_line = False
            for col in row:
                keys.append(col)
        else:
            ips_status[row[0]] = dict(zip(keys, row))

    pp(ips_status)
    print()
    
    for id in ips_status:
        if int(ips_status.get(id).get("events")) == 0:
            _LOGGER.info(f"enabling IPS for {id}")
            body = {"intrusionPrevention": {"state": "prevent"}}
            # _LOGGER.info(f"change policy for {ips_status.get(id)}")
            # body = {"policyID": 34}
            connector.post("computers", variable=str(id), data=body)
