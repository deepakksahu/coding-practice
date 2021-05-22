def regex_x(regex_path,delim):
    if regex_path == "/":
        regex_path = ".*"
    elif regex_path == "" or regex_path[-1] == delim:
        regex_path += ".*"

    regex_patterns = regex_path.split(delim)
    print(regex_patterns)

regex_x("^inv_*/.*","/")

import os
import copy
import re
import time
import io

from googleapiclient.http import MediaIoBaseDownload

from drive.utils import _retry_
from drive.logger_conf import get_logger

logger = get_logger()


# https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/drive_v3.files.html
# class Gdrive(object):
#     """This class will hold the file structure of given Drive Id"""
#     __MAX_PAGE_SIZE = 1000
#     __FOLDER_MIMETYPE = "application/vnd.google-apps.folder"
#
#     def __init__(self, service, drive_id=None, drive_name="root", base_dir="/tmp"):
#         self.files = {}  # {'file-id': [list of childs with child-id]}
#         self.drive_id = drive_id if drive_id else "my-drive"
#         print(self.drive_id)
#         self.drive_name = drive_name
#         self.service = service
#         self.base_dir = base_dir
#
#     # NOTE: only 10MB files are supported...
#     def export(self, file_id, to_mime_type, file_context, **kwargs):
#         file_path = os.path.join(self.base_dir,
#                                  self.drive_id + "-split-" + file_id + "-split-" + file_context["modifiedTime"])
#         if 'target_filename' in kwargs:
#             file_path = os.path.join(self.base_dir, kwargs.get('target_filename'))
#
#         if os.path.exists(file_path):
#             logger.info("File Already Exists: " + file_path)
#             return file_path
#         request = self.service.files().export_media(fileId=file_id,
#                                                     mimeType=to_mime_type)
#         with open(file_path, 'wb') as f:
#             f.write(request.execute())
#
#     def download(self, file_id, file_context, **kwargs):
#         file_path = os.path.join(self.base_dir,
#                                  self.drive_id + "-split-" + file_id + "-split-" + file_context["modifiedTime"])
#         if 'target_filename' in kwargs:
#             file_path = os.path.join(self.base_dir, kwargs.get('target_filename'))
#         if os.path.exists(file_path):
#             logger.info("File Already Exists: " + file_path)
#             return file_path
#
#         request = self.service.files().get_media(fileId=file_id)
#         fh = io.FileIO(file_path, 'wb')
#         downloader = MediaIoBaseDownload(fh, request)
#         done = False
#         while done is False:
#             status, done = downloader.next_chunk()
#             print("Download %d%%." % int(status.progress() * 100))
#
#         return file_path
#
#     def get_file_path(self, file_id, file_context):
#         file_path = os.path.join(self.base_dir,
#                                  self.drive_id + "-split-" + file_id + "-split-" + file_context["modifiedTime"])
#         return file_path
#
#     @_retry_
#     def _get_files_from_my_drive(self, directory_id, page_token=None):
#         if page_token:
#             return self.service.files().list(
#                 pageToken=page_token,
#                 pageSize=self.__MAX_PAGE_SIZE,
#                 fields="files(id, name, parents, mimeType, modifiedTime), nextPageToken",
#                 q="'%s' in parents" % (str(directory_id)),
#                 spaces="drive").execute()
#         else:
#             return self.service.files().list(
#                 pageSize=self.__MAX_PAGE_SIZE,
#                 fields="files(id, name, parents, mimeType, modifiedTime), nextPageToken",
#                 q="'%s' in parents" % (str(directory_id)),
#                 spaces="drive").execute()
#
#     @_retry_
#     def _get_files_from_shared_drive(self, directory_id, page_token=None):
#         if page_token:
#             return self.service.files().list(
#                 corpora="drive",
#                 driveId=self.drive_id,
#                 pageToken=results["nextPageToken"],
#                 pageSize=self.__MAX_PAGE_SIZE,
#                 fields="files(id, name, parents, mimeType, modifiedTime), nextPageToken",
#                 q="'%s' in parents" % (str(directory_id)),
#                 supportsAllDrives=True,
#                 includeItemsFromAllDrives=True).execute()
#         else:
#             return self.service.files().list(
#                 corpora="drive",
#                 driveId=self.drive_id,
#                 pageSize=self.__MAX_PAGE_SIZE,
#                 fields="files(id, name, parents, mimeType, modifiedTime), nextPageToken",
#                 q="'%s' in parents" % (str(directory_id)),
#                 supportsAllDrives=True,
#                 includeItemsFromAllDrives=True).execute()
#
#     @_retry_
#     def _get_files_from_fileid(self, file_id):
#         return self.service.files().get(
#             fileId=file_id,
#             fields="id,name,parents,mimeType,modifiedTime",
#             supportsTeamDrives=True,
#             supportsAllDrives=True).execute()
#
#     def _get_files_from_drive_api(self, directory_id):
#         response = []
#         if self.drive_id == "my-drive":  # SEARCH IN MYDRIVE
#             logger.info("searching in my-drive")
#             results = self._get_files_from_my_drive(directory_id)
#             response.extend(results.get("files", []))
#
#             while results.get("nextPageToken"):  # iterate more
#                 results = self._get_files_from_my_drive(directory_id, page_token=results["nextPageToken"])
#                 response.extend(results.get("files", []))
#
#         else:  # SEARCH IN SHARED DRIVE
#             logger.info("searching in share drive %s - %s" % (str(self.drive_id), str(directory_id)))
#             results = self._get_files_from_shared_drive(directory_id)
#
#             response.extend(results.get("files", []))
#             while results.get("nextPageToken"):  # iterate more
#                 results = self._get_files_from_shared_drive(directory_id, page_token=results["nextPageToken"])
#                 response.extend(results.get("files", []))
#
#         return response
#
#     def get_files_in_directory(self, directory_id):
#         if directory_id in self.files:
#             return self.files[directory_id]
#         else:
#             self.files[directory_id] = self._get_files_from_drive_api(directory_id)
#
#         return self.files[directory_id]
#
#     def _get_parent_id(self, file):
#         return file['parents'][0]
#
#     """
#         regex_path = "/" => returns all files in given parent_ids or self.drive_id whichever is passed
#         regex_path = "" => same as "/"
#         regex_path = "a/b/c" => will return all nested files from  a/b directory
#         regex_path = "a/b/c/" => will return files in a/b/c directory
#
#         parents = {'234324dsdsfasdf': {'name': 'drive'}, '123233443': {'name': 'drive2'}}
#     """
#
#     def get_files_by_regex_path(self, regex_path, parents=None, mime_types=None, delim="/"):
#         if self.drive_id == "my-drive" and not parents:
#             raise Exception("parent_ids are must to start the lookup for my-drive, either get the my-drive id"
#                             " or lookup from a folder id")
#
#         logger.info("Regex Path : " + str(regex_path))
#         logger.info("Parents : " + str(parents))
#         logger.info("Drive ID: " + str(self.drive_id))
#         logger.info("Mime Types: " + str(mime_types))
#
#         if regex_path == "/":
#             regex_path = ".*"
#         elif regex_path == "" or regex_path[-1] == delim:
#             regex_path += ".*"
#
#         regex_patterns = regex_path.split(delim)
#
#         assert len(regex_patterns) >= 1
#
#         parents = {self.drive_id: {'name': self.drive_name}} if parents is None else parents
#
#         for level, regex_pattern in enumerate(regex_patterns):
#             childs = []  # Get the current level childs
#             for parent_id, parent_ctx in parents.items():
#                 childs.extend(self.get_files_in_directory(parent_id))
#
#             filtered_childs = {}  # Filtered childs to go into next lookup with parents context setup
#             for idx, file in enumerate(childs):
#                 # Set context of all childs
#                 file['gdrive_parentcontext'] = parents.get(self._get_parent_id(file))
#
#                 # Filter next parents or base level files
#                 if re.match(regex_pattern, file["name"]):
#                     if level == len(regex_patterns) - 1:  # last level, add filtering by mimeType
#                         if mime_types:  # If there is any mime_type filter
#                             if file["mimeType"] in mime_types:
#                                 filtered_childs[file['id']] = file
#                         else:
#                             filtered_childs[file['id']] = file
#
#                     else:  # Need to go more deep, only go into folders
#                         if file["mimeType"] != self.__FOLDER_MIMETYPE:
#                             raise Exception(
#                                 "Regex path is trying to look inside a file, Either correct regex or file structure")
#                         filtered_childs[file['id']] = file
#             parents = filtered_childs
#
#         return filtered_childs
#
#     def get_files_by_ids(self, file_ids):
#         files = {}
#         for file_id in file_ids:
#             files[file_id] = self._get_files_from_fileid(file_id)
#         return files
#
# gdrive=Gdrive(service, drive_id=None, drive_name="root", base_dir="/tmp")
#
# gdrive.get_files_by_regex_path(self,".*/.*", parents= "1-zoL9zfftQT1dHn2BJwSUDo2l2VH-bi4", mime_types="['application/pdf']", delim="/")