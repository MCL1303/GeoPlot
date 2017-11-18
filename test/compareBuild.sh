find test/data/facts/ -type f -name "*.xml" -print0 | xargs -n1 -0 model/build

git diff --no-patch --exit-code model/models || {
	git checkout model/models
	exit 1
}
