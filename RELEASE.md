- To release a new version of ipyfetch on PyPI:

Update _version.py (set release version, remove 'dev')
Update version also in `js/package.json`
git add the _version.py file and git commit
`python setup.py sdist bdist_wheel`
`twine upload dist/*`
`git tag -a X.X.X -m 'comment'`
Update _version.py (add 'dev' and increment minor)
git add and git commit
git push
git push --tags

- To release a new version of ipyfetch on NPM:

Update `js/package.json` with new npm package version

```
# clean out the `dist` and `node_modules` directories
make clean
cd js
npm install
npm publish
```