# Interacting with JSONPlaceholder using curl
Use curl to fetch data from `https://jsonplaceholder.typicode.com`


## Summary

Initially approach was using `curl` to simply fetch the url.  This yielded a lot of html on the main page.

Further inspection led to the guide page where jsonplaceholder talked about their API calls.  After changing the URL to one of the API calls, and changing GET to POST, there was a significant reduction in the amount of data returned.  I verified this to ensure there were no errors, but this short response that only included the id was the expected response for this type of request.

## Challenges
There were no issues installing or using curl.  I had to read the man page to figure out the flags for headers and passing data, but these proved unnecessary for this type of HTTP request.

Some of the left over attempts to use POST data and headers are left as comments in the `post-request.sh` file for fun.

## Things learned
A review of the curl command.  This is something I was familar with previously.
