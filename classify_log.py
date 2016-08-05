#!/usr/bin/env python
#
# Copyright (C) 2016 Red Hat, Inc.
#
# Author: Frederic Lepied <frederic.lepied@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

'''
'''

import re
import sys

from classify_console import cleanup
from classify_console import first

error_regexp = re.compile(
    '\(.*?\) \(.*?"(.*?)"'
    '|Exception (.*?):'
    '|/([^/]+: No such file or directory)'
    '|Went to status ERROR due to "Message: ([^.]+).*Code: 500"'
    '|CREATE_FAILED (Create timed out)'
)


def classify(data):
    lines = data.split('\n')
    for line in lines:
        res = error_regexp.search(line)
        if res:
            return ('-'.join(cleanup(first(res.groups())).split(' ')), )
    return ('unknown',)

if __name__ == "__main__":
    print ' '.join(classify(sys.stdin.read(-1)))

# classify_log.py ends here
