import json
from time import time
from utils import Process, Logger

_start_time = time()
Logger.info("Running [blue]LaunchIt[/blue]")

processes_json = "./processes.json"
Logger.info(f"Loading processes_data from {processes_json}")
with open(processes_json, "r", encoding="UTF-8") as json_file:
    processes_data = json.load(json_file)
process_count = len(processes_data)

Logger.info(f"Loading {process_count} processes")
for process_data in processes_data:
    name = process_data["name"]
    start_cmd = process_data["start_cmd"]
    directory_path = process_data["directory_path"]
    auto_start = process_data["auto_start"]

    Logger.info(f"Loading {name} with auto_start {auto_start}")
    process = Process(name=name, start_cmd=start_cmd, directory_path=directory_path, auto_start=auto_start)


_end_time = time()
_total_runtime = _end_time - _start_time
_total_runtime_ms = round(_total_runtime * 1000)
Logger.info("Finished running [blue]LaunchIt[/blue]")
Logger.debug(f"Elapsed Time: {_total_runtime_ms} ms")
