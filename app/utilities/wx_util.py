import hashlib
import requests
import json


class WxUtils:
    def __init__(self, app_id, app_secret) -> None:
        self._app_id = app_id
        self._app_secret = app_secret

    def checkSignature(self, data):
        TOKEN = "tisteryu"
        signature = data.get("signature")
        timestamp = data.get("timestamp")
        nonce = data.get("nonce")
        if not signature or not timestamp or not nonce:
            return False
        tmp_str = "".join(sorted([TOKEN, timestamp, nonce]))
        tmp_str = hashlib.sha1(tmp_str.encode("UTF-8")).hexdigest()
        if tmp_str == signature:
            return True
        else:
            return False

    def get_openid(self, code):
        appid = self._app_id
        secret = self._app_secret
        url = (
            "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=%s"
            % (appid, secret, code, "authorization_code")
        )
        res = requests.get(url)
        if res.status_code == 200 or res.status_code == 206:
            return res.json()

    def get_wx_token(self):
        appid = self._app_id
        secret = self._app_secret
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
        response = requests.get(url)
        data = response.json()
        access_token = data.get("access_token")
        return access_token

    def send_message(self, wxid, template_id, data):
        at = self.get_wx_token()
        req = {
            "template_id": template_id,
            "touser": wxid,
            "data": data,
        }
        res = requests.post('https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=' + at, data=json.dumps(req))
        print(res.text)