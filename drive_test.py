from drive.tokenmanager import TokenManager as TM
from drive.logger_conf import get_logger
from googleapiclient.discovery import build
# from job import Job
from drive.drive import Gdrive
import dateutil.parser
import os
import json
import sys
# import boto3
# import pandas as pd
import pprint

logger = get_logger()
scopes = ['https://www.googleapis.com/auth/drive.readonly',
          'https://www.googleapis.com/auth/spreadsheets.readonly']


def prepare_creds(token):
    logger.info("Gdrive: Authenticating...")
    token_manager = TM(scopes=scopes)
    token_manager.read_from_dict(token)
    logger.info("Gdrive: Authentication Done")
    return token_manager.creds


def main():
    # job_id = sys.argv[1]

    j = "47"
    config = {"gdrive-dir-id": "1SpVOU7IdDQhPu_9O0IDfC9ild3-7xPNQ", "mime-types": ["application/pdf"], "bucket-name": "gfg-de-risk", "bucket-path": "file_storage_sync/invoice_ocr/","drive-id": "0AJkVUYUoY-rEUk9PVA","regex-scanpath":"^inv.*[0-9]$/.*"}
    token = {"token": "ya29.a0AfH6SMDJLEJgTUC0UI1NdviNbBlEM1W5hHHQVBvQt5QtFGbNGB7Uqmg92L-9zAdTOeo2qdvb_HHkE1oy1PSdV3eAyqHOmbe1rZWCJojRvdgxVCth6SbiMGfHT5KP42Hck3tiIY-IwctNTVfCfAwJYSlLHDuHd8hN6bk", "refresh_token": "1//0giZ-3xx31N5XCgYIARAAGBASNwF-L9Irr1wvbggQQM1ogBZ_AKjp-wgWYHGh6hrmGz1jIXdf0oLPHc6Qw8s8T6RquuK-KLGbhsU", "token_uri": "https://oauth2.googleapis.com/token", "client_id": "904688820986-12nf3bjcdj8e2a39l3cpb1blvj2m5cp7.apps.googleusercontent.com", "client_secret": "qQcXVNgKVFR8KjMSmeDLKlLg", "scopes": ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.readonly", "openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/spreadsheets.readonly"]}

    creds = prepare_creds(token)
    service = build('drive', 'v3', credentials=creds)
    # s3 = boto3.resource('s3')
    s3Prefix = config['bucket-path']

    DOWNLOAD_DIR = "filedownload"
    ensure_dir(DOWNLOAD_DIR)

    gd = Gdrive(service, base_dir="./" + DOWNLOAD_DIR, drive_id=config.get('drive-id', ""))
    writepath = config.get('writepath', "parent_id/file_name")
    fetch_method = config.get('fetch-method', "scan")
    if fetch_method == "scan":
        scanpath = config.get('regex-scanpath', ".*/.*")
        files = gd.get_files_by_regex_path(scanpath, {config['gdrive-dir-id']: {}}, mime_types=config['mime-types'])
    # elif fetch_method == "s3_id_list":
    #     list_files = config["s3_id_list_files"]
    #     file_ids = []
    #     for f in list_files:
    #         df = pd.read_parquet(f["path"])
    #         file_ids.extend(df[f["column_name"]].to_list())
    #     files = gd.get_files_by_ids(file_ids=file_ids)

    # jobstate = j.get_job_state()

    # files_to_fetch = get_unfetched_files(jobstate, files)

    # for file_id in files_to_fetch:
    #     f = files[file_id]
    #
    #     logger.info("printing F")
    #     pprint.pprint(f)
    #
    #     if type(f) is not dict:
    #         logger.info("ignored file_id:{}".format(file_id))
    #         continue
    #
    #     logger.info("processing file_id:{}".format(file_id))
    #
    #     replacemap = {
    #         "parent_id": f['parents'][0],
    #         "file_name": f['name'],
    #         "file_id": file_id
    #     }
    #
    #     logger.info("printing replacemap")
    #     pprint.pprint(replacemap)
    #     target_filename = writepath
    #
    #     for k, v in replacemap.items():
    #         logger.info(target_filename)
    #         target_filename = target_filename.replace(k, v)
    #
    #     ensure_dir(DOWNLOAD_DIR + "/" + target_filename.rsplit("/", 1)[0])
    #     gd.download(file_id, f, target_filename=target_filename)
    #     formatted_time = dateutil.parser.parse(f['modifiedTime']).strftime("%Y-%m-%d %H:%M:%S")
    #     target_filepath = os.path.join(s3Prefix, target_filename)
    #     s3.Object(config['bucket-name'], target_filepath).put(
    #         Body=open(os.path.join(DOWNLOAD_DIR, target_filename), 'rb'))
    #     j.put_state(file_id, formatted_time)


def ensure_dir(dirpath):
    try:
        os.mkdir(dirpath)
    except:
        print("dir already exists")


def get_unfetched_files(jobstate, files):
    jobstate_ids = []
    for state in jobstate:
        jobstate_ids.append(state['file_id'])
    file_ids = []
    for key, file in files.items():
        file_ids.append(key)
    return list(set(file_ids) - set(jobstate_ids))


if __name__ == "__main__":
    main()
