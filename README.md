# cv-cli

cv-cli is a project made to encapsulate computer vision algorithms in a simple cli for fun pourposes.

### Roadmap

- Improve gender detection accuracy
- Add custom training functionallity

### Install it in your system

There is no installation script at this moment. Just clone the repo and execute the cli.py script.

You will need:

- python (3.x)
- pip
- pipenv

And some pip dependencies :
	
	cd [project_folder]
	pipenv install --ignore-pipfile


### Usage

	pipenv run python cv_cli.py --command gender-detection \
		--input $(pwd)/data/images/people/woman_frontal.jpg --output image


## Developing 

### Testing

Execute tests with the following command from root project dir.

	pipenv run python -m pytest 

Pytest will execute all tests inside modules matching the regular expression [Tt]est[-_]*.

If coverage package is installed you can get the report result

	pipenv run python -m coverage run --source $(pwd) cv_cli.py --command gender-detection --input $(pwd)/data/images/people/woman_frontal.jpg --output image
	pipenv run python -m coverage report


### Git flow



### Additional resources

- pip -> 
- pipenv -> 
- opencv ->
- 