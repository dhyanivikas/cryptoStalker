# cryptoStalker
This is a crypto currencies tracking pure Python project.
It tracks cryptocurrencies of your interest and capable generating notications based on currency prices and suggest
the buying and selling positions based on your preferences and positions.

Right now, the positions need to be stored in DB and rules are enmbedded in business logic
but in future, I plan to make it more sophisticated based on Neural network outputs


You'll need to add the secrets.yaml file in resources folder by yourselves and put following entries:

{"x-rapidapi-key": "YOUR_RAPIDAPI_KEY", "x-rapidapi-host": "YOUR_CHOSEN_RAPIDAPI_HOST"}

I've put that file into gitignore list for obvious reasons.
