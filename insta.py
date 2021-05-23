# import instaloader

# test = instaloader.Instaloader()

# acc = input('Enter the Account Username: ')

# test.download_profile (acc, profile_pic_only = True)

from flask import Flask, request, render_template
import instaloader
from instaloader import Profile, Post


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download',methods=['POST'])
def download():
    instance = instaloader.Instaloader()
    
    instance.download_profile(profile_name= request.form.get("username"))
    

    return render_template('index.html', prediction_text='Downloaded Successfully')


if __name__== "__main__":
    app.run(debug=True)




