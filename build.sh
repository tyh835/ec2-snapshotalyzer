# clean-up step
rm -rf build dist snappy.egg-info
pip3 uninstall snappy -y

# build
pipenv run python setup.py bdist_wheel

# install
pip3 install dist/*.whl