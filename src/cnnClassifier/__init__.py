import os
import sys
import logging

loggin_str = "[%(asctime)s: %(levelname)s: %(modules)s: %(message)s]"

log_dir = "logs"
log_filePath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loggin_str,
    handlers=[logging.FileHandler(log_filePath), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("cnnClassifierLogger")
