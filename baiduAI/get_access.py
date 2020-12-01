# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=tbmHP2VwVQpvmKVj5rWWFI5E&client_secret=7L1KSEt87xESYeNQ5bqP3Ez4ogzZRqV1'
response = requests.get(host)
if response:
    print(response.json())

'''
{'refresh_token': '25.e4277027e5595cca1a828d0a2fb0c22e.315360000.1921887362.282335-23057366', 
'expires_in': 2592000, 
'session_key': '9mzdCSKO9nNg/oT/caoIfB2mbbBtLyLhfwPgR+7cEKJpJwCsMOjS2Ec/DevwQDjIvZtP7g+BqWywhjZcEvzB4JVCBEfP/A==', 
'access_token': '24.242e7e4428c9b54d6c203fd133b877d8.2592000.1609119362.282335-23057366', 
'scope': 'public brain_all_scope brain_body_analysis brain_body_attr brain_body_number brain_driver_behavior brain_body_seg brain_gesture_detect brain_body_tracking brain_hand_analysis wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base smartapp_mapp_dev_manage iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理 smartapp_component smartapp_cserver_meta', 
'session_secret': '0d8187681792bfbc9e0c626848a1807e'}

'''