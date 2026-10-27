#!/usr/bin/env python3
# @noindex
"""Validate ReaCrusher's distributable without third-party dependencies."""
from pathlib import Path
import base64
import re
import struct

root = Path(__file__).resolve().parents[1]
code = (root / 'Effects/ReaCrusher.jsfx').read_text()
assert re.search(r'^// @version \d[^\n]*$', code, re.M)
assert '// @author Mannix Squared' in code
assert 'SPDX-License-Identifier: GPL-3.0-or-later' in code
assert 'GNU GENERAL PUBLIC LICENSE' in (root / 'LICENSE').read_text()
assert not re.search(r'^import\s|^filename:', code, re.M), 'Unexpected external asset dependency'
assert len(re.findall(r'^slider\d+:', code, re.M)) == 12
assert sorted(map(int, re.findall(r'(?:knob|toggle)\((\d+),', code))) == list(range(1, 13))
stripped = re.sub(r'//[^\n]*|"(?:[^"\\]|\\.)*"', '', code)
stack = []
for char in stripped:
    if char in '([':
        stack.append(char)
    elif char in ')]':
        assert stack and stack.pop() == {')': '(', ']': '['}[char], 'Unbalanced code'
assert not stack
bank = (root / 'Effects/ReaCrusher.jsfx.rpl').read_text()
entries = re.findall(r'<PRESET `([^`]+)`\s+([A-Za-z0-9+/=\s]+?)\s+>', bank)
assert len(entries) == 21
assert len({name for name, _ in entries}) == 21
boolean_slots = {0, 3, 6, 8, 9}
for name, data in entries:
    payload = base64.b64decode(''.join(data.split()), validate=True)
    assert payload[-5] == 0
    assert struct.unpack('<f', payload[-4:])[0] == 1.0
    state, preset_name = payload[:-5].decode().rsplit(' "', 1)
    assert preset_name == name + '"'
    values = state.split()
    assert len(values) == 64 and values[12:] == ['-'] * 52
    for index, value in enumerate(values[:12]):
        value = float(value)
        assert 0 <= value <= 1, (name, index, value)
        if index in boolean_slots:
            assert value in (0, 1), (name, index, value)
assert entries[0][0] == 'Clear'
print('PASS: metadata, GPL license, all 12 UI bindings, code delimiters and all 21 RPL presets.')
