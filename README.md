# Python flask alpine image
Simple python app (flask + sqlite + logger), that can be build into an alpine docker image.

# Usage
**1)** docker build . -t python_alpine:1.0.0

**2)** docker run -d -p 5003:5003 <IMAGE_ID>

**3)** Go to 127.0.0.1:5003 to check if app is running.

# Endpoints
- **/** and **/index** - select last user from database.
- **/insert_to_db** - name speaks for itself, use headers to redefine values.
- **/select_from_db** - again use headers to redefine values.
