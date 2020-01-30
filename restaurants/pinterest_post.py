import base64
import json
import requests

class Pinterest:
#TODO: CRIO_TASK_MODULE_PINTEREST_SHARE
# As part of this module you are expected to complete the publish_photo_msg function
# Tasks:
# 1) You need to register as pinterest developer to obtain app_id & app_secret
# 2) Obtain an access token using Postman method and store it in access_tokens.sh
# 3) Obtain Pinterest board ID by creating a Pinterest Board using the Pinterest Create Board API
#    (https://developers.pinterest.com/docs/api/boards/) and store it in access_tokens.sh
# 4) Enter board_id & access_token in access_tokens.sh - IMPORTANT step
#    PINTEREST_BOARD_ID=board_id
#    PINTEREST_ACCESS_TOKEN=access_token
# 5) Complete the publish_photo_msg() function. This function should publish a pin with
#    the given message and photo. The post should be published to the board you have created
#    in the earlier step
# 6) Manually verify the pin created and submit the code
#
# NOTE: The Pinterest API has a rate limit of 10 requests/hour. If you exceed
#       this limit, you can either wait until the rate counter resets or create
#       a new board and use it to test your implementation.

# Args:
#   1) message   -> string message to be posted
#   2) image_url -> publicly accessible url of the image to be posted

# write your code below
    def publish_photo_msg(self, message, image_url):
        

