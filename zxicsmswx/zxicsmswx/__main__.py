import wx_sms_forwarder
import config_utils

if __name__ == '__main__':
    conf = config_utils.get_config('./config.json')
    forwarder = wx_sms_forwarder.WxSmsForwarder(conf)
    forwarder.start()
