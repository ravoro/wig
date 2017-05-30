#!/bin/bash
# The script takes 2 possible sets of values:
#     1) Specific module, class or method (based on: https://docs.python.org/3/library/unittest.html#command-line-interface)
#     2) Specific package (requires use of additional "discover" argument) (based on: https://docs.python.org/3/library/unittest.html#test-discovery)
#
# Examples:
#     * Execute a test method:  "./scripts/test.sh tests.scrapers.basic.test_get_page_meta_title.Test.test_return_page_title"
#     * Execute a test class:   "./scripts/test.sh tests.scrapers.basic.test_get_page_meta_title.Test"
#     * Execute a test module:  "./scripts/test.sh tests.scrapers.basic.test_get_page_meta_title"
#     *        ...alternative:  "./scripts/test.sh tests/scrapers/basic/test_get_page_meta_title.py"
#     * Execute a test package: "./scripts/test.sh discover tests.scrapers" (note the additional `discover` argument)
#
# Default functionality:
#     Execute all tests within the "tests" package (i.e. "./scripts/test.sh" will ultimately run "./scripts/test.sh discover tests")


EXEC_TESTS="discover tests"
if [ "$#" -ne 0 ]; then
    EXEC_TESTS="$@"
fi

python -m unittest ${EXEC_TESTS}
