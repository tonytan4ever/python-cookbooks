import glob
import logging
import logging.handlers
import sys

log = logging.getLogger()


def main(input_file_path, size=2**20*15):
    file_name = os.path.basename(input_file_path)
    fh = logging.handlers.RotatingFileHandler(f"/tmp/{file_name}", 
                                              maxBytes=size, backupCount=100)
    log.addHandler(fh)
    log.setLevel(logging.INFO)
    with open(input_file_path) as f:
        while True:
            log.info(f.readline().strip())
    print("File split completed:")
    print(glob.glob(f"/tmp/{file_name}*"))
    

if __name__ == '__main__':
    input_file_path = sys.args[1]
    main(input_file_path)