find test/data/facts/ -type f -name "*.xml" -print0 | xargs -n1 -0 model/build

git diff --no-patch --exit-code data/facts || {
	git checkout test/data/facts
	exit 1
}
