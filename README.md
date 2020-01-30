# QEats Sneak Peek: Social Review
## Theme Problem: 
QEats is a popular food ordering app. It gives users a list of nearby restaurants and popular dishes. Users can use the app to order their favourite dishes from restaurants of their choice. Millions of users across the country have been using the QEats app to satisfy their hunger and taste buds. 
#### Now 
The most requested feature on QEats is the ability to share reviews on past orders on QEats' social media pages.
1. Users want to click a photo of the orders they have received, write eye-catching captions and add relevant tags to make their reviews easily discoverable.
2. The QEats team is relying on your expertise to implement this Reviews feature.
This is the backend of Qeats Food Ordering android app. It is a microexperience program in which we have to add certain features in the app.

## Solution 
##### Task 1 : Publish a message to Facebook page (#Git #Facebook Share API)
##### Context 
The QEats backend provides all the necessary functionality required to enable users to order their favorite dishes from nearby restaurants. The following is the overall architecture of the QEats platform. Please study it carefully and understand all the individual components.

<img src="photos/first.png" >

##### Primary Goals
1. Clone QEats Sneak Peek code repository.
2. Install any required python libraries.
3. Use the python requests module to publish posts to a Facebook page.

```python
def publish_photo_msg(self, message, image_url):
        # write your code here
            data = {
                'url': image_url,
                'caption':message,
                'published': 'true',
                'access_token':self.page_access_token,
                'id': self.page_id
            }
            response=requests.post('https://graph.facebook.com/me/photos', data=data)
            return
```

##### Task 2 : Share a Review from the App to Facebook (#REST #API #cURL #JSON #HTTP Error Codes)
##### Context
You  published a message to a Facebook page using the python requests module. It is now time to run the full QEats backend server. The code you wrote in the previous module will be used here to publish reviews coming from the QEats Android app.
##### To-do
To write a review for an order, the QEats Android app will prompt users to first take a picture (or select one from their image gallery). They can then add a description and some #hashtags
 
 <img src ="photos/second1.png">

To post reviews to the QEats Facebook page,you have to start the QEats backend server and configure the Android app to connect to it. You can then post QEats reviews from your phone to the QEats Facebook page.

##### Primary Goals
1. Install the QEats app.
2. Run the QEats backend server.
3. Use share_review.py to publish a photo message to the QEats Review Facebook page from the command line.
4. Use the QEats app to share a review directly to the QEats eview Facebook page.

```python
def share_review(msg, file_name):
    """Shares the given image and the message to facebook/pinterest share."""
    data = {
        'imgBase64': file_path_to_img64(file_name),
        'text': msg,
        'tags': '',
        'orderId': '',
        'share': ['Facebook']
    }
    try:
        resp = requests.post(
            data=data, url='http://localhost:8081/qeats/v1/review/share')
        print("Response Status Code: " + str(resp.status_code))
    except requests.exceptions.ConnectionError:
        print(
            '\n\nError: Could not post review. Make sure you have started the server!!!\n\n')
```
##### Task 3 : Share a Review on Pinterest (#Pinterest Share API #Postman)
##### Context 
Take reviews to a wider audience by sharing them on Pinterest.
##### To-do
You will extend support in the QEats backend to enable posting reviews to a Pinterest board. To post user reviews on Pinterest, you have to first obtain the necessary authentication credentials. You will then use Pinterest’s POST API to post user reviews.

<img src="photos/third1.png">


##### Primary Goals
1. Use Postman to create a new Pinterest board (QEats Reviews) and get an access token.
2. Use the Pinterest API in the QEats backend to post reviews to the QEats Reviews board.

```python
class Pinterest:

# Args:
#   1) message   -> string message to be posted
#   2) image_url -> publicly accessible url of the image to be posted

# write your code below
    def publish_photo_msg(self, message, image_url):
```

##### Task 4 : Suggest a list of review tags using an AI Service (#Clarifai Predict API)
##### Context 
Computer vision and AI have enabled us to cluster and categorize images at an unprecedented scale. We will use one such classifier today called Clarifai.ai . Clarifai has used millions of images available on the internet to generate clusters (a.k.a. models.) We can use these models to categorize new images. Such categorizations vary in their accuracy depending on how close the test image is to the training set used
##### To-do
You will send the QEats review image to Clarifai and receive a list of potential category matches. You will then send this category list as suggested #hashtags for the user to choose from and add to their reviews.
##### Primary Goal
Use the Clarifai Predict API to categorize review images and send #hashtag suggestions to users
```python
# Parameters
# ----------
# api_key : string
#     API Key for Clarifai
# image_url : string
#     publicly accessible URL of the image to get tag suggestions
# Return Type: list()
#   return a list of tags provided by the Clarifai API
def get_tags_suggestions(api_key, image_url):
    # write your code here
    headers = {
    'Authorization': "Key "+'6e29581ac9dd456abe896de261a59f6f',
    'Content-Type': 'application/json'
    }
    data = '{"inputs": [{"data": {"image": {"url": "https://samples.clarifai.com/food.jpg" } } } ]  }'
    response = requests.post('https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs', headers=headers, data=data)
    output=response.json()
    # print(output)
    tags=[]
    for x in output['outputs'][0]['data']['concepts']:
        tags.append(x['name'])
    return tags
```
