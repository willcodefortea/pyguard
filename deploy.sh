version=`python -c "from pyguard import VERSION; print VERSION"`
# Create a tag and push it
git tag $version -m "$version"
git push
git push --tags

# Deploy to pypi
python setup.py register -r pypi
python setup.py sdist upload -r pypi
