# factorization

factorization exercises generator made by using flask and staring at coefficients for too much time

this could probably be a single file client side js site but i won't have as much fun typing typescript/javascript as doing it in python for anything longer than 100 lines

and also i can make an api out of this if i wanted to in the future (not that anyone would actually use a factorization generator api lol)

link: https://factorization-generator.vercel.app/

## factorization types supported

- identities
   - 3 squares
   - 2 squares (diff sign)
   - 2 squares (same sign)
   - difference of squares
   - perfect squares
- common factors only
   - no squares
   - degree one common factors (supports flipping signs: e.g. (x-2y) = -(2y-x))
 
## local python file usage

the code for the generator ([generator.py](https://github.com/ducky4life/factorization/blob/main/generator.py)) can be used without the web interface (no dependencies are needed). there are examples provided at the end of the file for usage.

make sure you have [python](https://www.python.org/downloads/) installed.

1. clone the repository/copy generator.py to a python file
   ```
   git clone https://github.com/ducky4life/factorization.git
   cd factorization
   ```
2. run the included examples
   ```
   python generator.py
   ```

## local site usage

deploying to vercel is always the fastest, but there are local options

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/ducky4life/factorization)

### python

make sure you have [python](https://www.python.org/downloads/) installed.

1. clone the repository
   ```
   git clone https://github.com/ducky4life/factorization.git
   ```
2. move into directory
   ```
   cd factorization
   ```
3. install dependencies
   ```
   pip install -r requirements.txt
   ```
4. run the app
   ```
   python app.py
   ```
5. go to http://localhost:8080/

### docker

make sure you have [docker](https://www.docker.com) installed.

[building from source](https://github.com/ducky4life/factorization#building-the-images-from-source-recommended) is recommended since it is how i mainly test the packages and you get the most up to date dependencies.

amd64 packages are not tested since i only have an arm64 rasp pi with docker.

#### using pre-built images

1. get the correct package for your archetecture

   [amd64](https://github.com/ducky4life/factorization/pkgs/container/factorization%2Ffactorization-generator-amd64):
   ```
   docker pull ghcr.io/ducky4life/factorization/factorization-generator-amd64:latest
   ```
   [arm64](https://github.com/ducky4life/factorization/pkgs/container/factorization%2Ffactorization-generator-arm64):
   ```
   docker pull ghcr.io/ducky4life/factorization/factorization-generator-arm64:latest
   ```
2. run the docker container

   amd64:
   ```
   docker run -p 8080:8080 --name factorization-generator ghcr.io/ducky4life/factorization/factorization-generator-amd64:latest
   ```
   arm64:
   ```
   docker run -p 8080:8080 --name factorization-generator ghcr.io/ducky4life/factorization/factorization-generator-arm64:latest
   ```
3. go to http://localhost:8080/

#### building the images from source (recommended)

1. clone the repository
   ```
   git clone https://github.com/ducky4life/factorization.git
   ```
2. move into directory
   ```
   cd factorization
   ```
3. build the docker image for your archetecture

   amd64:
   ```
   docker build -t factorization-generator:latest -f amd64.Dockerfile .
   ```
   arm64:
   ```
   docker build -t factorization-generator:latest -f arm64.Dockerfile .
   ```
4. run the docker container
   ```
   docker run -p 8080:8080 --name factorization-generator factorization-generator:latest
   ```
5. go to http://localhost:8080/


## to do list

- [ ] toggle including answers
- [x] 0/1 square terms
- [x] swapping signs function
- [x] actually implement swapping signs
- [ ] insanity mode for max coefficients
- [ ] api if i'm feeling really bored
- [ ] increase probability for squared terms for deg 1 c.f.
- make sure all terms in the polynomial don't share the same common factor lol (check for negative coefficients)
   - [x] 3 sq
   - [x] 2 sq diff
   - [x] 2 sq same
   - [x] no sq
   - [x] diff of sq
   - [x] perf sq (common factor intentionally included)
   - [ ] deg 1 c.f. flip
   - [ ] deg 1 c.f. no flip
