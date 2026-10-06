"""Every total the prose states, derived from the model. No document sentence may
contain a written-out total that is not produced here."""
import json

M = json.load(open('model.json', encoding='utf-8'))

UCS = M['use_cases']
USE_CASES = len(UCS)
PACKAGES = len([p for p in M['packages'] if p['members']])
PRIMARY = [a for a in M['actors'] if a['kind'] == 'primary']
PEOPLE = [a for a in PRIMARY if a['person'] == 'yes']
STARTERS = [a for a in PRIMARY if a['person'] != 'yes']       # clocks, devices and systems that start work
SUPPORTING = [a for a in M['actors'] if a['kind'] == 'supporting']
OFFSTAGE = [a for a in M['actors'] if a['kind'] == 'offstage']
ACTORS_NAMED = len(PRIMARY) + len(SUPPORTING)
ACTORS_OFFSTAGE = len(OFFSTAGE)


def _distinct(xs):
    return list(dict.fromkeys(xs))


ENTITY_NAMES = _distinct(e for u in UCS for e in u['entities'].get('changes', []) + u['entities'].get('reads', []))
ENTITIES = len(ENTITY_NAMES)
RULE_IDS = _distinct(r for u in UCS for r in u['rules'])
RULES = len(RULE_IDS)
REQUIREMENT_IDS = _distinct(r for u in UCS for r in u['requirements'])
REQUIREMENTS = len(REQUIREMENT_IDS)
INCLUDES = sum(len(u['relationships']['includes']) for u in UCS)
EXTENDS = sum(len(u['relationships']['extends']) for u in UCS)
_settings = M['named'].get('settings') or {}
SETTING_NAMES = list(_settings.get('entries') or [])
SETTINGS = len(SETTING_NAMES)

_W = {0: 'no', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
      7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
      13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
      17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
_T = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
      7: 'seventy', 8: 'eighty', 9: 'ninety'}


def words(n):
    """Spell a total out, so no figure is ever typed into a sentence by hand."""
    n = int(n)
    if n < 20:
        return _W[n]
    if n < 100:
        t, u = divmod(n, 10)
        return _T[t] + ('-' + _W[u] if u else '')
    h, r = divmod(n, 100)
    s = _W[h] + ' hundred'
    if r:
        s += ' and ' + words(r)
    return s


def cap(n):
    w = words(n)
    return w[0].upper() + w[1:]
