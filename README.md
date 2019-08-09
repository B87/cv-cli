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
	pipenv install pytest
	pipenv install numpy
	pipenv install cv2
	pìpenv install nptyping

### Usage

	pipenv python cv-cli.py --command gender-detection \
		--input $(pwd)/data/images/woman_frontal.jpg


## Developing 

### Testing

Execute tests with the following command from root project dir.

	pipenv run python -m pytest 

Pytest will execute all tests inside modules matching the regular expression [Tt]est[-_]*.

### Git flow



### Additional resources
