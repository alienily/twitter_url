# twitter_url

This is a microservice to generate a twitter url. 

It communicates with other programs through the 'signal.txt' file located in this directory. 

The final url will be stored in the output.txt file. 

Example Request: If you wish to make a request, write the following to the 'signal.txt' file: 

the word "tweet" a "|" character, then whatever content you want to autofill in the tweet box. 

example: 

"tweet | hello world "

