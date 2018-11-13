# clean-up step
rm -rf build dist snappy.egg-info

# build
pipenv run python setup.py bdist_wheel