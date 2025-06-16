import yaml
import sys

def load_yaml(my_yaml):
    with open(my_yaml) as fileStream:
        try:
            loaded = yaml.safe_load(fileStream)
        except yaml.YAMLError as exception:
            print(exception)
            sys.exit(0)
    if loaded:
        return loaded


def find_match(art=None, typ=None, has_partner=None):
    rules = load_yaml("rules_v2.yaml")
    if rules:
        for rule in rules:
            match = rule.get('match', {})

            # Vergleich für art
            if art is not None:
                if 'art' not in match or art not in match['art']:
                    continue

            # Vergleich für typ
            if typ is not None:
                if 'typ' not in match or typ not in match['typ']:
                    continue
            elif 'typ' in match:
                # Regel verlangt typ, aber keiner wurde übergeben → kein Match
                continue

            # Vergleich für has_partner
            if has_partner is not None:
                if 'has_partner' not in match or match['has_partner'] != has_partner:
                    continue

            return rule.get('out')  # Erfolgreicher Treffer

        return None  # Kein passender Eintrag gefunden


print(find_match(art="DVOMA", typ="Vollstreckungsmaßnahme", has_partner=True))
assert(find_match(art="DVOMA", typ="Vollstreckungsmaßnahme", has_partner=True)) == {"postverteilung": "VM_GPK"}

print(find_match(art="DVOMA", typ=None, has_partner=True))
assert(find_match(art="DVOMA", typ=None, has_partner=True)) == {"postverteilung": "Firmenkunden"}

print(find_match(art="DAAG", typ=None, has_partner=True))
assert(find_match(art="DAAG", typ=None, has_partner=True)) == {"postverteilung": "Firmenkunden"}

print(find_match(art="DHKPF", typ=None, has_partner=True))
assert(find_match(art="DHKPF", typ=None, has_partner=True)) == {"postverteilung": "Häusliche Krankenpflege"}

print(find_match(art="DHIMI", typ=None, has_partner=True))
assert(find_match(art="DHIMI", typ=None, has_partner=True)) == {"postverteilung": "Hilfsmittel"}

print(find_match(art="DCLVM", typ=None, has_partner=None))
assert(find_match(art="DCLVM", typ=None, has_partner=None)) == {"postverteilung": "VM_GPK"}
