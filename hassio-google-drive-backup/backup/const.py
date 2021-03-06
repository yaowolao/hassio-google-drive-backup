
SOURCE_GOOGLE_DRIVE = "GoogleDrive"
SOURCE_HA = "HomeAssistant"

ERROR_PLEASE_WAIT = "please_wait"
ERROR_NOT_UPLOADABLE = "not_uploadable"
ERROR_NO_SNAPSHOT = "invalid_slug"
ERROR_CREDS_EXPIRED = "creds_bad"
ERROR_UPLOAD_FAILED = "upload_failed"
ERROR_BAD_PASSWORD_KEY = "password_key_invalid"
ERROR_SNAPSHOT_IN_PROGRESS = "snapshot_in_progress"
ERROR_PROTOCOL = "protocol_error"
ERROR_LOGIC = "logic_error"
ERROR_INVALID_CONFIG = "illegal_config"
ERROR_DRIVE_FULL = "drive_full"
ERROR_GOOGLE_DNS = "google_dns"
ERROR_GOOGLE_CONNECT = "google_cant_connect"
ERROR_GOOGLE_INTERNAL = "google_server_error"
ERROR_GOOGLE_SESSION = "google_session_expired"
ERROR_GOOGLE_TIMEOUT = "google_timeout"
ERROR_GOOGLE_UNEXPECTED = "google_unexpected"
ERROR_HA_DELETE_ERROR = "delete_error"
ERROR_MULTIPLE_DELETES = "multiple_deletes"
ERROR_SUPERVISOR_UNEXPECTED = "supervisor_unexpected"
ERROR_SUPERVISOR_TIMEOUT = "supervisor_timeout"

ERROR_EXISTING_FOLDER = "existing_backup_folder"
ERROR_BACKUP_FOLDER_MISSING = "backup_folder_missing"
CHOOSE_BACKUP_FOLDER = "choose_backup_folder"
ERROR_BACKUP_FOLDER_INACCESSIBLE = "backup_folder_inaccessible"
ERROR_LOW_SPACE = "low_space"
LOG_IN_TO_DRIVE = "log_in_to_drive"
SUPERVISOR_PERMISSION = "supervisor_permission"

DRIVE_FOLDER_URL_FORMAT = "https://drive.google.com/drive/u/0/folders/{0}"
GITHUB_ISSUE_URL = "https://github.com/sabeechen/hassio-google-drive-backup/issues/new?labels[]=People%20Management&labels[]=[Type]%20Bug&title={title}&assignee=sabeechen&body={body}"
GITHUB_BUG_TEMPLATE = """
###### Description:
```
If you have anything else that could help explain what happened, click "Markdown" above and write it here.
```

 Addon version: `{version}`
 Home Assistant Version: `{ha_version}`
 Supervisor Version: `{super_version}`
 Supervisor Channel: `{supervisor_channel}`
 Hassos Version: `{hassos_version}`
 Docker Version: `{docker_version}`
 Architecture: `{arch}`
 Machine: `{machine}`
 Date: `{time}`
 Timezone: `{timezone}`
 Failure Time: `{failure_time}`
 Last Good Sync: `{sync_last_start}`
 ###### Exception:
 ```
 {error}
 ```
 Snapshots:
 ```
 {snapshots}
 ```
 ###### Config:
 ```
 {config}
 ```
 ###### Addon Logs:
 ```
 {addon_logs}
 ```
 ###### Supervisor Logs:
 ```
 {super_logs}
 ```
 ###### Home Assistant Core Logs:
 ```
 {core_logs}
 ```
 """

FOLDERS = [
    {
        'slug': "homeassistant",
        'id': "folder_homeassistant",
        'name': "Home Assistant Configuration",
        'description': 'Backup the files and folders from your Home Assistant config directory, eg configuration.yaml'
    },
    {
        'slug': "media",
        'id': "folder_media",
        'name': "Media",
        'description': 'Backup your "/media" directory.'
    },
    {
        'slug': "ssl",
        'id': "folder_ssl",
        'name': "SSL",
        'description': 'Backup your "/ssl" directory, where your certfile and keyfile are typically stored.'
    },
    {
        'slug': "share",
        'id': "folder_share",
        'name': "Share",
        'description': 'Backup your "/share" directory.'
    },
    {
        'slug': "addons/local",
        'id': "folder_addons",
        'name': "Local Addons",
        'description': 'Backup your local addons directory. This directory will be empty unless you use it for add-on development.'
    }
]