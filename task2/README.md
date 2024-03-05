# Using Postman to make API requests
Use Postman to fetch data from `https://jsonplaceholder.typicode.com`


## Summary

Starting simple, the same request was made as was done using `curl`.  Exporting the data for the "Collection" initially yielded no headers for the post or response.  This led me to the "save as example" icon above the results.  This added the headers and response that I didn't initially see.


## Challenges
Postman has it's own json structure and thus required a bit of inspection.  Addionally it was not obvious how to export the collection, nor that saving an example was necessary.  Furthermore, the custom headers that were set were not included in the request block of json as I would have expected it to appear.  Postman seems to have segregated these headers into a seperate section.  I suspect there is a reason for this, but I have no idea what it is.


## Things learned
How to navigate Postmane GUI.  Some of the gotchas with setting headers, how they manifest, and how they are exported/saved to json.

