from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pprint import pprint

class MySubscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        pass

    def presence(self, pubnub, presence):
        pprint(presence.__dict__)

    def message(self, pubnub, message):
        pprint(message.__dict__)

def my_publish_callback(envelope, status):
    print(envelope, status)

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-3afbdbfe-ddee-11e9-9fd1-52d10f2427f8"
pnconfig.publish_key = "pub-c-65161fdf-1944-4938-b9ce-50f0fd2be583"

pubnub = PubNub(pnconfig)

pubnub.add_listener(MySubscribeCallback())

pubnub.subscribe()\
    .channels("pubnub_onboarding_channel")\
    .with_presence()\
    .execute()\

pubnub.publish()\
    .channel("pubnub_onboarding_channel")\
    .message({"sender": pnconfig.uuid, "content": "Hello From Python SDK"})\
    .pn_async(my_publish_callback)