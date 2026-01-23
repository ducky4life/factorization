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
   - perfect squares of (ax-by) with forced common factor after factorizing
- common factors only
   - no squares
   - degree 1-4 common factors (supports flipping signs: e.g. (x-2y) = -(2y-x))
 
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

## to do list

- [ ] toggle including answers: make something to access the coefficients
    - you can probably make an answer validator if you do this
- [x] 0/1 square terms
- [x] swapping signs function
- [x] actually implement swapping signs
- [ ] perfect square (linear): force common factor
- [ ] insanity mode for max coefficients (maybe a global toggle for the random generator function instead of manually setting every limit)
- [ ] api if i'm feeling really bored
- [x] increase probability for squared terms for deg 1 c.f.
- [ ] randomize common factor terms order
- [x] flip for degree 2-4
- make sure all terms in the polynomial don't share the same constant common factor lol (check for negative coefficients)
   - [x] 3 sq
   - [x] 2 sq diff
   - [x] 2 sq same
   - [x] no sq
   - [x] diff of sq
   - [x] perf sq (common factor intentionally included)
   - [ ] deg 1 c.f. flip
   - [ ] deg 1 c.f. no flip
   - [x] higher deg c.f. flip (intentional)
   - [x] higher deg c.f. noflip (intentional)

## api usage

api endpoint: `https://factorization-generator.vercel.app/api`

by default, the api is started from app.py. you can host the api as standalone app by adding the stuff in app.py before and after `main_route()` to api.py

only polynomial_type is a required argument. the rest is optional and can be excluded. arguments can also be combined as shown [here](https://github.com/ducky4life/factorization?tab=readme-ov-file#exporting-to-file).

note that LaTeX mode is the only output form.

### arguments

`polynomial_type` (required) - type of polynomial to be generated.

available options: 0_sq, 2_sq_same, 2_sq_diff, 3_sq,
   perf_sq_1 (expanded), perf_sq_2, diff_sq,
   deg_1_cf_flip, deg_1_cf_noflip, higher_deg_cf_flip, higher_deg_cf_noflip

randomized options: mixed_all, mixed_identities_only, mixed_no_identities

`amount` - the amount of polynomials to be generated. defaults to 1.

`x_unk` - the name for the 'x' unknown.

`y_unk` - the name for the 'y' unknown. you can enter a space character for constants (no unknown).

`sq_unk` - the name for the extra square term unknown. only used for 3 square terms.

`shuffle_terms` - whether to shuffle the different terms in the polynomial. defaults to false.

## api examples

you can use this command to show a help message:

```sh
curl -d 'help' https://factorization-generator.vercel.app/api
```

or just `curl https://factorization-generator.vercel.app/api`

### example query with all arguments:

```sh
curl -d 'polynomial_type=3_sq' -d 'amount=3' -d 'x_unk=a' -d 'y_unk= ' -d 'sq_unk=b' -d 'shuffle_terms=true' -d 'prettify=false' https://factorization-generator.vercel.app/api
```

returns:

> {"polynomial_1":"$-16+8a-a^2+64b^2$","polynomial_2":"$36b^2-30a-9-25a^2$","polynomial_3":"$a^2+2a+1-49b^2$"}

### exporting to file

use the redirection operator `>>`

example:

```sh
curl -d 'polynomial_type=mixed_all&prettify=True&amount=3' https://factorization_generator.vercel.app/api >> output.json
```

```json
{
  "polynomial_1": "$25x^2+60xy+36y^2-4$",
  "polynomial_2": "$-4(5x+y)(3y-x)+8(-x+5y)(3y-x)$",
  "polynomial_3": "$16x^2+4x-5y-25y^2$"
}
```

## local site usage

deploying to vercel is always the fastest, but there are local options

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/ducky4life/factorization)

### python

make sure you have [python](https://www.python.org/downloads/) installed.

1. clone the repository
   ```
   git clone https://github.com/ducky4life/factorization.git
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

#### pre-built images

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
   cd factorization
   ```
2. build docker image

   amd64:
   ```
   docker build -t factorization-generator:latest -f amd64.Dockerfile .
   ```
   arm64:
   ```
   docker build -t factorization-generator:latest -f arm64.Dockerfile .
   ```
4. run docker container
   ```
   docker run -p 8080:8080 --name factorization-generator factorization-generator:latest
   ```
5. go to http://localhost:8080/
