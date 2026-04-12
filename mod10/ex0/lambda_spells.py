# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lambda_spells.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chrilomb <chrilomb@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/10 18:25:49 by chrilomb          #+#    #+#              #
#    Updated: 2026/04/10 19:41:12 by chrilomb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: x.get('power', 0)))

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage.get('power', 0) > min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "*" + spell + "*", spells))

def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    som = lambda mages: sum(mage.get('power', 0) for mage in mages)
    min_ = lambda mages: min(mage.get('power', 0) for mage in mages)
    max_ = lambda mages: max(mage.get('power', 0) for mage in mages)
    avg = lambda mages: som(mages) / len(mages)
    return {
        'max_power': max_(mages),
        'min_power': min_(mages),
        'avg_power': avg(mages)
    }

if __name__ == "__main__":
    artifacts = [
        {'name': 'Amulet of Power', 'power': 50},
        {'name': 'Ring of Strength', 'power': 30},
        {'name': 'Cloak of Invisibility', 'power': 20}
    ]
    mages = [
        {'name': 'Gandalf', 'power': 100},
        {'name': 'Merlin', 'power': 80},
        {'name': 'Saruman', 'power': 90}
    ]
    spells = ['Fireball', 'Lightning Bolt', 'Heal']

    sorted_artifacts = artifact_sorter(artifacts)
    powerful_mages = power_filter(mages, 85)
    transformed_spells = spell_transformer(spells)
    mage_power_stats = mage_stats(mages)

    print("\nSorted Artifacts:", sorted_artifacts)
    print("\nPowerful Mages:", powerful_mages)
    print("\nTransformed Spells:", transformed_spells)
    print("\nMage Power Stats:", mage_power_stats)
