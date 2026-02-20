1. What does the @app.route() decorator actually do?
its flask’s way of mapping URLs to Python functions
2. How does Flask know which function to call when a request arrives?
by  using the URL router 
3. What's the difference between route parameters (<name>) and query parameters (?key=value)?
part of the URL path itself,  come after the ? in the URL and are not part of the route.
4. Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?
GET and POST send data in completely different places, and Flask reads them from different parts of the HTTP request.
5. What happens if you try to access request.args outside of a request context?
will throw a RuntimeError