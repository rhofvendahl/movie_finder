# Movie Finder API

#### By Sarthak Agrawal and Russell Hofvendahl

## About
This is the Movie Finder API repository.

## Setup
1. Clone this repo and navigate to the root directory.
```
git clone https://github.com/rhofvendahl/movie_finder_api
cd movie_finder_api
```

2. Set up a virtual environment and install dependencies.
```
pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the local server.
```
flask run
```

## Collaboration
1. Pull latest changes.
```
git pull origin
```
If there are conflicts, fix each file and commit the fix.

2. Start a new feature branch.
```
git branch new_feature
git checkout new_feature
```

3. Commit frequently as you work, with descriptive messages.

4. When ready, go back to master and pull the latest changes from the server.
```
git checkout master
git pull origin
```

5. Merge your local feature branch onto the master.
```
git merge new_feature
```

6. If any conflicts, fix and commit.

7. Push your changes to the remote server.
```
git push
```

## License

Copyright (c) 2021 Sarthak Agrawal and Russell Hofvendahl

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
