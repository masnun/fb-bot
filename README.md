## Facebook Messenger EchoBot Example


#### Install Dependencies

Install flask & requests using `pip`:

		pip install Flask
		pip install requests
		
Install ngrok from - <a href="https://ngrok.com/">https://ngrok.com/</a>.

#### Run Server & Tunnel Connection

Run the dev server using: 

	python server.py

Use `ngrok` to tunnel the connection. 

	ngrok http 5000

You shall see the url for your local server. Something like: `https://6cecffb8.ngrok.io`. 

#### Setup Facebook App & Access Token

* Create a Facebook App.
* Add the `Messenger` Product.
* Enable webhooks. Use the above URL as the callback webhook URL. 
* Once the callback is verified, subscribe the app to one of your pages. 
* Also generate a page access token for that page. 
*  Edit `server.py` and update the `ACCESS_TOKEN` with the new token we got.

	

