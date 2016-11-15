from avi.sdk.avi_api import ApiSession
import logging
from flask import json
import os

LOG = logging.getLogger(__name__)


def upload_config_to_controller(avi_config_dict, controller_ip,
                                username, password, tenant):
    LOG.debug("Uploading config to controller")
    session = ApiSession.get_session(controller_ip, username,
                                     password=password, tenant=tenant)
    try:
        d = {'configuration': avi_config_dict}
        path = 'configuration/import'
        resp = session.post(path, data=d)
        if resp.status_code < 300:
            LOG.info("Config uploaded to controller successfully")
        else:
            LOG.error("Upload error response:"+resp.text)
        print 'Log of upload config : %s' % resp.text
    except:
        LOG.error("Failed config upload", exc_info=True)
        print "Error"

if __name__ == "__main__":
    upload_config_to_controller(json.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'output/Output.json')))), "10.10.26.73", "admin", "avi123$%", "admin")