from fast_dash import FastDash
from fast_dash.Components import Image, UploadImage

# 1. Inference function
def image_to_image(image):
    return image

# 2. Define components and initialize app
app = FastDash(callback_fn=image_to_image, 
               inputs=UploadImage, 
               outputs=Image,
               title='Simple image to image',
               title_image_path='https://tinyurl.com/mr44nn5y',
               subheader='Build ML prototypes lightning fast!',
               github_url='https://github.com/dkedar7/fast_dash/',
               linkedin_url='https://linkedin.com/in/dkedar7/',
               twitter_url='https://twitter.com/dkedar7/',
               theme='FLATLY')

# 3. Deploy!
app.run()