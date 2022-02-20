# Étude du système de vote électronique de la primaire écolo

Avant propos :

Cet article vise à analyser **du point de vu d'un votant** un système de vote par internet utilisé lors d'une élection à caractère politique de premier plan.

De fait, comme le rappel la [délibération n° 2019-053 du 25 avril 2019 portant adoption d'une recommandation relative à la sécurité des systèmes de vote par correspondance électronique, notamment via Internet](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038661239/) :

> Au cours des travaux que la commission a menés depuis 2003 et compte tenu des menaces qui pèsent sur ces dispositifs, elle a, en effet, pu constater que les systèmes de vote existants ne fournissaient pas encore toutes les garanties exigées par les textes légaux. Dès lors et en particulier, compte-tenu des éléments précités, la commission reste réservée quant à l'utilisation de dispositifs de vote par correspondance électronique, notamment via Internet, pour des élections politiques.

Cet article vise notamment à évaluer la capacité d'un électeur à établir la prise en compte de son vote ainsi que la validité de l'urne, ainsi que les pré-requis de confiance à des tiers que cela implique.

Cet article a été communiqué à Neovote en amont de sa publication (le 05/10/2021, puis le 17/10/2021).

À la suite de cela, Neovote a demandé au titre de la propriété intellectuelle la suppression des copies d'écrans ainsi que des extraits du code source public de vérification des votes.
Nous avons maintenu les copies d'écrans et les reproductions de code source public au titre du droit de citation de l'article L.122-5 du Code de la propriété intellectuelle.

En outre Neovote s'est opposé à ce que tout extrait de leurs réponses par mail soit publié et n'a pas demandé l'inclusion d'un droit de réponse à cet article.

## I - Présentation du système Neovote

En septembre 2021 la primaire de l'écologie a vu la victoire de Yannick Jadot.

Grande première, cette élection du candidat à la présidence s'est déroulée entièrement en ligne via un service fournit par le prestataire [neovote](https:/neovote.com).

Ayant participé à cette primaire en tant qu'électeur, j'ai eu la curiosité de me pencher sur le système.

Neovote se présente comme "Solution homologuée par le Conseil d'État, le Sénat, le Ministère de l'intérieur et la DGSI".

| ![Site de Neovote](neovote_site_titre.png) |
|:------------------------------------------:|
| Crédits: Neovote                           |

L'expertise de la solution est mise à l'honneur.

| ![Description de l'expertise technique sur le site de Neovote](neovote_site_description_1.png) |
|:--:|
| Crédits: Neovote |

Le site reste peu loquace sur le fonctionnement du système ; seuls quelques concepts sont évoqués :

| ![Description du fonctionnement du système sur le site de Neovote ?](neovote_site_description_2.png) |
|:--:|
| Crédits: Neovote |

Après contact par mail de Neovote, nous avons obtenu plus d'informations.

De fait le système Neovote comprend deux parties:

- un site web permettant aux utilisateurs de voter ([primaire.neovote.com](https://primaire.neovote.com) dans le notre cas), chaque organisation de vote ayant son propre site
- un site web permettant à un utilisateur de vérifier l'urne ainsi que la prise en compte de son vote ([verifier-mon-vote.fr](https://verifier-mon-vote.fr), qui est commun à toutes les organisations de votes). Ce site est opéré par un huissier de justice indépendamment de Neovote.

D'un point de vu légal, Neovote s'appuie sur la [délibération CNIL n°2019-053](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038661239/) portant adoption d'une recommandation relative à la sécurité des systèmes de vote par correspondance électronique, notamment via Internet.

Cette recommandation contient notamment l'objectif de sécurité n° 3-02 (Permettre la transparence de l'urne pour tous les électeurs à partir d'outils tiers) qui est la finalité de la mise à disposition du site [verifier-mon-vote.fr](https://verifier-mon-vote.fr) ainsi que de son code source.

Cette recommandation n'oblige pas à rendre disponible à tout électeur une documentation technique sur le fonctionnement du système (notamment le rapport d'homologation approuvé par l'Autorité d'homologation du système ou bien le rapport d'expertise au sens le la recommandation). Une telle documentation permettrait pourtant de comprendre les modèles de risques pris en compte, car comme le rappel la recommandation dans son préambule :

> Devant l'extension continue du vote par Internet à tous types d'élections, la commission souhaite rappeler que le vote par correspondance électronique, notamment via Internet, présente des difficultés accrues [...] principalement à cause de l'opacité et de la technicité importante des solutions mises en œuvre, ainsi que de la très grande difficulté de s'assurer de l'identité et de la liberté de choix de la personne effectuant les opérations de vote à distance.

*Neovote a indiqué que seuls les exports indépendants habilités dans le périmètre II-900/IGI-1300 peuvent avoir accès à des précisions techniques sur le système.*

## II - Le vote et sa vérification

Le vote se fait sur le site [primaire.neovote.com](https://primaire.neovote.com) après s'être identifié. Afin de limiter les risques de vol d'identité, l'authentification et le vote se font via deux facteurs (SMS envoyé en avance de l'élection et requis pour voter).

(pas de captures d'écran, désolé ¯\\_(ツ)_/¯ )

Une fois le vote réalisé, deux éléments nous sont présentés:

- un numéro d'accusé de réception au sein de la liste d'émargement (par exemple `5WQR7A8N`)
- une preuve de vote, telle que :

```raw
5Ehjzb4WmzpEmKhhvXBEcTV3sSAyR\_62i5P1wqwCfcLnQKZW62UomrzyVuz5jeBv-oXSDpaW0kz-RjCAzpzV\_aEFiLkISVBamu88Ic7KravGCJNI6DHupQgPlmnYNEl2hZab-I2m80oQV\_nnUKoY7tlbIKj-fYXDCfgIwyvVfS7UmawjagkSYjO-ypF8Gazfv1RbVod0YxLlelLY0z65W1Fgvgxvgx4oFsHSQJzTPKqCw0fAgXfSRSoCWFwhlV4Qh0BtNRbOIQviDc2nOsRjSTiOoApai6IHupE\_VyfGD5UYyMGW0ViZNQhL4NspQzmhXSF7enOyv1A5NR5IdpRVCPJ84sZ6\_CsEQIlhRVqmbLImYIi2582Afj4RpdgwkW0N50RVBlwK3652Iom7poqhVpqdjIbx9doPX\_X2dczNx\_DFhiboNs7ULqXx74p7A\_sRWpL3kI\_Z6UzWQfgyhf1WNhL6\_Gb7QWDS8cDjccXLCdjEcu7OmmPOmXnwmr3KApCHNlS87HlIIcsLHXd9-1QR_w@@
```

Une fois les deux tours terminés, le site de vote permet de consulter les résultats de l'élection.

| ![neovote_resultats.png](neovote_resultats.png) |
|:-----------------------------------------------:|
| Crédits: Neovote                                |

Un mot de passe est fourni permettant de contrôler la validité des résultat ainsi que la présence de son vote depuis le site [verifier-mon-vote.fr](https://verifier-mon-vote.fr).

Selon sa mention légale, ce site est installé, publié et maintenu par la société SAS ID FACTO, Huissiers de Justice Associés.

| ![verification_vote_site.png](verification_vote_site.png) |
|:--:|
| Crédits: Neovote |

L'étape de vérification du vote crashe au bout de ~7mn.

| ![verification_vote_error_1.png](verification_vote_error_1.png) |
|:---------------------------------------------------------------:|
| Crédits: Neovote                                                |

En relançant la vérification plusieurs fois (le serveur conserve le travail effectué entre chaque tentative), on arrive à la fin du traitement et le résultat apparait :

| ![resultats_officiels_2eme_tour.png](resultats_officiels_2eme_tour.png) |
|:--:|
| Crédits: Neovote |

Le site propose de télécharger [le code source du script réalisant les vérifications](https://www.verifier-mon-vote.fr/index.php?downloadSource) (lien "Code Source" en bas à droite de la page).

Ce code va nous permettre d'en apprendre plus sur le fonctionnement du système ;-)

## III - Analyse de la preuve de vote

Comme dit plus haut, la preuve de vote se présente sous la forme suivante :
```raw
5Ehjzb4WmzpEmKhhvXBEcTV3sSAyR_62i5P1wqwCfcLnQKZW62UomrzyVuz5jeBv-oXSDpaW0kz-RjCAzpzV_aEFiLkISVBamu88Ic7KravGCJNI6DHupQgPlmnYNEl2hZab-I2m80oQV_nnUKoY7tlbIKj-fYXDCfgIwyvVfS7UmawjagkSYjO-ypF8Gazfv1RbVod0YxLlelLY0z65W1Fgvgxvgx4oFsHSQJzTPKqCw0fAgXfSRSoCWFwhlV4Qh0BtNRbOIQviDc2nOsRjSTiOoApai6IHupE_VyfGD5UYyMGW0ViZNQhL4NspQzmhXSF7enOyv1A5NR5IdpRVCPJ84sZ6_CsEQIlhRVqmbLImYIi2582Afj4RpdgwkW0N50RVBlwK3652Iom7poqhVpqdjIbx9doPX_X2dczNx_DFhiboNs7ULqXx74p7A_sRWpL3kI_Z6UzWQfgyhf1WNhL6_Gb7QWDS8cDjccXLCdjEcu7OmmPOmXnwmr3KApCHNlS87HlIIcsLHXd9-1QR_w@@
```

Il s'agit d'un message chiffré en [AES256-CBC](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard) (chiffrement symétrique) et encodé en base64 (avec certains caractères remplacés) .

La clé de déchiffrement est présente en dur dans le script :

| ![php_clee_aes.png](php_clee_aes.png) |
|:--:|
| Crédits: Neovote |

*Interrogé sur la raison la raison de l'utilisation de chiffrement symétrique AES sur la preuve de vote, étant donnée que cette clé est publique (et est toujours la même puisque en dur dans le code), Neovote répond que AES est utilisé dans ce cas non pas dans un but cryptographique mais uniquement de servir de padding.*

Le [padding](https://fr.wikipedia.org/wiki/Remplissage_(cryptographie)) est une opération cryptographique visant à donner une taille fix à des données de tailles variable. Toutefois ici les données sont toujours de la même taille (cf. ci-dessous). De plus AES256-CBC n'est pas un algorithme de padding (il utilise lui même [PKCS7](https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS#5_and_PKCS#7) pour ses propres besoin de padding). Enfin la raison d'avoir recours à du padding ici n'est pas évidente : la preuve de vote étant uniquement affichée à l'utilisateur votant.

La preuve de vote déchiffrée donne 5 hashes :

```raw
EIKBGEq_QpF3nAjHOZJvXdV6KTscq3qjAUDObdvSnm0CEDnNsu8JLHFFWW_1aM8VxEySINTJOzYkUfvN_zFi2A@@
8XqbwjZZwZjK5cOoh0jsGutQgzhZhiDA4Flu4ib6QSyTRAgkClM3wZE2bXwo5rRwJSVuaKBpLC-DRC81Jjb5_g@@
Dq1sNpv8rkqwWDZp7n1CMMtcRdZDpQEfyFxBojHNCIECbckGA5j8YnMWvIgzAe7oMUYOu9hsyInCM7wbA8gLkQ@@
e1aBpILgnEJbMM96G6ZVig87T2nRJ6fwtPPTsUPVt0fcLla9BUHe7IlkUP8cdQcfIZM1FWmR4CFPzsa-Nc2bXw@@
hpPE7r89WZNf9ThdQtHIANB2ywEN8rAWqjarNyb6L5wiLylsgsXR8X8_Hepbw6zKjk3pPu1w95Pt5lxR0V48Pw@@
```

Ces hashes correspondent à l'empreinte SHA512 de votes présents dans l'urne (comme nous le verrons plus loin).

Il est intéressant de noter que la preuve de vote est personnelle et propre à chaque tour, mais qu'elle fait toutefois référence à 5 votes différents.

*Neovote nous éclaire sur ce point en expliquant que le but est de permettre de valider que bulletin fait parti de l'urne sans pour autant révéler son contenu.*

Enfin, puisque la preuve de vote n'est pas signée cryptographiquement, il est trivial [d'en générer une arbitraire](https://github.com/touilleMan/neovote-primaire-ecolo/blob/master/generate_invalid_proof.py).

Ainsi une preuve de vote contenant un hash non présent dans l'urne peut être générée et présentée comme "preuve" que son vote n'a pas été pris en compte de manière régulière.

| ![verification_vote_preuve_invalide.png](verification_vote_preuve_invalide.png) |
|:--:|
| Crédits: Neovote |

Le corollaire étant bien sûr que toute personne de bonne foi dont la preuve de vote ne fonctionne pas peut se voir opposer qu'elle a très bien pu réaliser un faux...

## VI - Analyse de l'urne

L'urne de vote se compose de deux archives :

- une archive `BallotBoxExport.zip` contenant l'urne à proprement parler (i.e. les bulletins chiffrés) ainsi que des métadonnées
- une archive `BallotKeysExport.zip` contenant des clés servant à déchiffrer les bulletins

Les deux archives sont protégées par le mot de passe `biè2Rrwû_çb7TWQà`.

Or le format zip n'est pas fait pour supporter des [caractères non-ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange) dans le mot de passe, l'encodage à utiliser ne faisant pas partie de la spécificité du format, son choix dépend du logiciel de décompression utilisé, de la façon de le lancer, ainsi que du système d'exploitation…

Concrètement, la décompression des archives est rendu complexe pour un acteur tiers utilisant un outil classique, par exemple 7zip sous Windows 10 :

![archive_decompression_7z.png](archive_decompression_7z.png)

ou encore sous linux (testé sous Ubuntu 18.04 LTS et 20.10) :

```shell
$ 7za x BallotBoxExport.zip -pbiè2Rrwû_çb7TWQà

7-Zip (a) [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=C.UTF-8,Utf16=on,HugeFiles=on,64 bits,12 CPUs AMD Ryzen 5 2600 Six-Core Processor             (800F82),ASM,AES-NI)

Scanning the drive for archives:
1 file, 96732480 bytes (93 MiB)

Extracting archive: BallotBoxExport.zip
--
Path = BallotBoxExport.zip
Type = zip
Physical Size = 96732480

ERROR: Wrong password : election_names.csv
ERROR: Wrong password : ballot_names.csv
ERROR: Wrong password : 1M-9493O-5D-2B-1C-2T-8S/object_names.csv
ERROR: Wrong password : 1M-9493O-5D-2B-1C-2T-8S/ballot_data.csv
ERROR: Wrong password : 1M-9493O-5D-2B-1C-2T-8S/count_params.csv
ERROR: Wrong password : 1M-9493O-5D-2B-1C-1T-8S/object_names.csv
ERROR: Wrong password : 1M-9493O-5D-2B-1C-1T-8S/ballot_data.csv
ERROR: Wrong password : 1M-9493O-5D-2B-1C-1T-8S/count_params.csv
ERROR: Wrong password : extra_hashes.csv
ERROR: Wrong password : version.txt

Sub items Errors: 10

Archives with Errors: 1

Sub items Errors: 10
```

L'objectif de sécurité n° 3-02 : "Permettre la transparence de l'urne pour tous les électeurs à partir d'outils tiers" est rendu d'autant plus difficile.

*À ce sujet, Neovote maintient que l'archive zip fonctionne sans problème.*

### Les clés

D'un point de vu technique, l'archive `BallotBoxExport.zip` est protégée par le mot de passe encodé en UTF-8, là où dans `BallotKeysExport.zip` le même mot de passe est encodé en iso-8859-1. Ceci rend le déchiffrage des archives assez complexe, le script PHP de vérification n'étant d'ailleurs pas épargné :

| ![bad password, try again](php_encode_password.png) |
|:--:|
| Crédits: Neovote |

Une fois déchiffré on peut découvrir le contenu :

Le fichier `BallotKeysExport.zip` contient une clé privée RSA (3072bits) par tour de scrutin.
```raw
1M-9493O-5D-2B-1C-1T-8S.pem
1M-9493O-5D-2B-1C-2T-8S.pem
version.txt
```

Une clé RSA étant une suite d'octets arbitraires, elle n'est pas lisible par un être humain et est donc généralement sérialisée lors de son export (le fameux `-----BEGIN PRIVATE KEY-----` suivi d'une suite de caractères en base64).
Chose étrange ici, la clé a été par dessus à nouveaux encodée en base64 (on a donc `base64(base64(clé))`).

RSA est un algorithme de chiffrement asymétrique constitué d'une clé publique (clé pouvant être divulguée à n'importe qui et servant au chiffrement) ainsi que d'une clé privée (clé généralement connue que de son propriétaire et servant au déchiffrement).

L'utilisation de RSA ici semble venir d'une volonté d'empêcher le déchiffrement avant le dépouillement de l'urne.
Nous supposons que le fonctionnement est le suivant :

1) la clé RSA est générée, la partie publique est chargée sur le serveur de vote, la partie privée est gardée sous scellé
2) le poste client (navigateur web) chiffre le vote de l'utilisateur via la clé publique et transmet le résultat au serveur qui l'ajoute à l'urne
3) au moment du dépouillement de l'urne, la clé privée est sortie du scellé pour déchiffrer les votes afin d'établir les résultats

Comme pour la preuve de vote, ce fonctionnement ne fait pas intervenir de mécanisme de signature cryptographique. Une clé privée RSA contenant aussi sa partie publique, il est de fait parfaitement possible d'altérer l'urne.

En outre, RSA est ici utilisé en mode [RSAES-PKCS1-v1_5](https://www.rfc-editor.org/rfc/rfc3447#section-7.2) qui est semble être considéré comme un mécanisme de chiffrement [obsolescent selon l'ANSSI](https://www.ssi.gouv.fr/uploads/2021/03/anssi-guide-selection_crypto-1.0.pdf).

Notons enfin l'utilisation de RSA en mode [ECB](https://fr.wikipedia.org/wiki/Mode_d%27op%C3%A9ration_(cryptographie)#Exemple_avec_une_image) : RSA ne chiffrant que des messages de la même taille que sa clé, pour pouvoir chiffrer un message plus grand ECB consiste simplement à découper le message en morceaux et les chiffrer chacun séparément.

| ![php_rsa_decryption.png](php_rsa_decryption.png) |
|:--:|
| Crédits: Neovote |

ECB est notamment vulnérable aux attaques par ré-ordonnancement (i.e. il n'est pas possible de détecter si des blocks chiffrés ont été inversés, résultant en un message déchiffré considéré comme valide bien que différent de l'original).

*Néovote nous précise que RSA ECB n'est pas utilisé tant que le message à chiffrer est inférieur à la taille d'un bloc.*

Effectivement, *dans le cas du suffrage de la primaire écologique* tous les bulletins son chiffrés sur un seul bloc RSA et ce code n'est donc pas exécuté.

### L'urne

De son côté `BallotBoxExport.zip` contient un répertoire par tour de scrutin, ainsi que des fichiers de métadonnées:

```raw
1M-9493O-5D-2B-1C-1T-8S/
1M-9493O-5D-2B-1C-2T-8S/
ballot_names.csv
election_names.csv
extra_hashes.csv
version.txt 
```

Comme leurs noms laisse à penser, `ballot_names.csv` et `election_names.csv` ne servent qu'à documenter le nom de l’élection et des 2 tours.

Un répertoire de tour de scrutin est composé de :

```raw
ballot_data.csv
count_params.csv
object_names.csv
```

`count_params.csv` décrit le type de scrutin (scrutin uninominal dans notre cas) ce qui est utilisé par le script de vote pour savoir comment compter les résultats.

`object_names.csv` contient une correspondance entre le nom des candidats et leur identifiant tel qu'il est utilisé dans les bulletins.

Pour le second tour, ce fichier donne:

```raw
"1M-9493O-5D-2B-1C-2T-8S-3L";"fr";"Yannick JADOT"
"1M-9493O-5D-2B-1C-2T-8S-2L";"fr";"Sandrine ROUSSEAU"
"VOTEBLANC";"fr";"Vote blanc"
```

Le fichier `ballot_data.csv` est l'urne à proprement parler. Il est composé d'autant de ligne qu'il y a de votes, chacune composée de:

- le bulletin de vote chiffré par la clé RSA
- le hash du bulletin de vote (tel qu'il est présent dans la preuve de vote)

Enfin le fichier `extra_hashes.csv` contient une liste de hashes supplémentaires à prendre en compte lors de la vérification de la preuve de vote.

Nous supposons que le but de ces hashes est de permettre de toujours retourner une preuve de vote contenant 5 hashes, y compris pour les tout premiers votants : si il n'y a moins de 5 votes disponibles, le serveur créé des hashes additionnels et les ajoutes dans ce fichier.

Une fois déchiffré, le bulletin se présente sous la forme:

```raw
('1M-9493O-5D-2B-1C-2T-8S-3L')wmbrgqbycomsjcxqrvvgbfnejorvatbhakilvdpjbejvpvfqfwhuleoavgvstmfqekolmifrnycakxrmfumujcxvnjusdjxriocdxuhpceyxhllcmuarcqougnivjacksbhutmdjogiwmvhcocpakxivqeglavrhrajcmqucfhxwwdijiqukucuenkcfkseyfuvgpbwebbnjjkdphnngewollgbckjkuwwimtexgbyfacmxoelpaseohnulcearxiqpqhvajuotmdphgvqcavegggryoonqjpemobynpkqdmitmgndjahashodbjetgeualmeqayboxhnkadagrluqe
```

On peut voir qu'il est constitué d'une partie [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) (oui, le script fait des remplacement type `(` -> `[` pour ensuite passer le résultat à la fonction `json_decode` de PHP) ainsi que d'un longue chaîne de texte.

Le document JSON contient uniquement l'identifiant du candidat pour qui l'électeur a voté, la longue chaîne semble aléatoire et est ignorée par le script.

### Étude de l'aléa du bulletin

La longue chaîne aléatoire dans le bulletin n'étant pas utilisée, nous ne pouvons que spéculer sur son utilité.

Étant donné qu'elle est désignée comme "aléa" dans le code du script PHP, il est possible qu'elle a été mise en place
pour que les bulletins ayant le même vote n'ait la même valeur une fois chiffrés (pour éviter une
[attaque de type text clair connu](https://fr.wikipedia.org/wiki/Attaque_%C3%A0_texte_clair_connu)).

En analysant les occurrences statistiques des caractères composant l'aléa, on obtient ceci :

| ![bulletin_alea_plot.png](bulletin_alea_plot.png)                                                         |
|:---------------------------------------------------------------------------------------------------------:|
| Répartition des occurences des octets de l'ensemble des aléas des bulletins du 2nd tour (35978684 octets) |

La forme de la courbe peut se lire de la façon suivante :

- seuls les octets représentant les [caractères ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange#Table_des_128_caract%C3%A8res_ASCII) allant de `a` à `y` sont utilisés
- les octets représentant les caractères de `a` à `f` sont 10% plus représentés que ceux de `g` à `y`

Une telle distribution peut s'expliquer par l'utilisation d'un code du style :
```python
random_byte = generate_cryptographically_secure_random_byte()  # e.g. random_byte == 42
human_readable_but_less_random_character = chr(ord('a') + random_byte % 25)  # == 'r'
```

On aurait donc une transformation d'une génération aléatoire uniforme dans la plage [0, 256] vers une plage [a, y] non uniforme.

En outre, le format PKCS1-v1.5 (utilisé lors du chiffrement RSAES-PKCS1-v1_5 du bulletin avec notre clé RSA 3072 bits)
[spécifie déjà l'utilisation d'entre 8 et 373 octets aléatoires](https://www.rfc-editor.org/rfc/rfc3447#section-7.2.1)
(selon la taille du message à chiffrer).

De fait si cette longue chaine semblant aléatoire est bien un aléa, son ajout reviendrait à remplacer des octets
cryptographiquement sécure par d'autres de moins bonne qualité.

*Neovote nous précise que cette chaine n'a qu'un but de remplissage sans objectifs d'aléa particulier.*

## V - Analyse du code javascript de la page web de vote

### Bibliothèque cryptographique utilisée

Le code javascript de la page de vote transmise par le serveur neovote est transpilé (compilation typescript vers javascript), subie du "tree-shaking" (suppression des parties du code source n'étant pas utilisé) et est enfin minifié (suppression de l'indentation, renommmage des variables).

Il est toutefois possible de rétablir l'indentation et d'apprécier les similitudes dans le code.

Par exemple, l'outil de minification utilisé par néovote ne modifie pas les noms des closures (i.e. des fonctions utilisant une variable définie dans un scope parent), de fait on peut retrouver dans le code une fonction `aes_init` contenant des variables `ginit`, `ginv`, `gmul`.

À partir de là il est facile en faisant [une recherche dans github](https://github.com/search?q=language%3Ajs+aes_init+ginv+ginit+gmul&type=code) de déterminer que la bibliothèque utilisée est [asmcrypto.js](https://github.com/asmcrypto/asmcrypto.js).

De fait, la comparaison de la fonction `aes_init` donne :

Code minifié de néovote (réindenté par nos soins) :

```javascript
function aes_init() {
    if (!$WWVLmkTY) {
        ginit();
    }
    function _s($WWVLmkWW) {
        var $WWVLmYFq;
        var $WWVLmkTq;
        var $zx;
        $WWVLmkTq = $zx = ginv($WWVLmkWW);
        for ($WWVLmYFq = 0; $WWVLmYFq < 4; $WWVLmYFq++) {
            $WWVLmkTq = (($WWVLmkTq << 1) | ($WWVLmkTq >>> 7)) & 255;
            $zx ^= $WWVLmkTq;
        }
        $zx ^= 99;
        return $zx;
    }
    $aes_sbox = [];
    $aes_sinv = [];
    $aes_enc = [[], [], [], []];
    $aes_dec = [[], [], [], []];
    for (var $WWVLmVTm = 0; $WWVLmVTm < 256; $WWVLmVTm++) {
        var $WWVLmkTq = _s($WWVLmVTm);
        $aes_sbox[$WWVLmVTm] = $WWVLmkTq;
        $aes_sinv[$WWVLmkTq] = $WWVLmVTm;
        $aes_enc[0][$WWVLmVTm] = (gmul(2, $WWVLmkTq) << 24) | ($WWVLmkTq << 16) | ($WWVLmkTq << 8) | gmul(3, $WWVLmkTq);
        $aes_dec[0][$WWVLmkTq] = (gmul(14, $WWVLmVTm) << 24) | (gmul(9, $WWVLmVTm) << 16) | (gmul(13, $WWVLmVTm) << 8) | gmul(11, $WWVLmVTm);
        for (var $WWVLmkTF = 1; $WWVLmkTF < 4; $WWVLmkTF++) {
            $aes_enc[$WWVLmkTF][$WWVLmVTm] = ($aes_enc[$WWVLmkTF - 1][$WWVLmVTm] >>> 8) | ($aes_enc[$WWVLmkTF - 1][$WWVLmVTm] << 24);
            $aes_dec[$WWVLmkTF][$WWVLmkTq] = ($aes_dec[$WWVLmkTF - 1][$WWVLmkTq] >>> 8) | ($aes_dec[$WWVLmkTF - 1][$WWVLmkTq] << 24);
        }
    }
    $WWVLmkTp = true;
}
```

[code de asmcrypto.js](https://github.com/asmcrypto/asmcrypto.js/blob/8644af6a9200439b41c788692a43db5ff8249507/src/aes/aes.asm.js#L97-L136):

```javascript
  function aes_init() {
    if (!ginit_done) ginit();

    // Calculates AES S-Box value
    function _s(a) {
      var c, s, x;
      s = x = ginv(a);
      for (c = 0; c < 4; c++) {
        s = ((s << 1) | (s >>> 7)) & 255;
        x ^= s;
      }
      x ^= 99;
      return x;
    }

    // Tables
    aes_sbox = [],
      aes_sinv = [],
      aes_enc = [[], [], [], []],
      aes_dec = [[], [], [], []];

    for (var i = 0; i < 256; i++) {
      var s = _s(i);

      // S-Box and its inverse
      aes_sbox[i] = s;
      aes_sinv[s] = i;

      // Ecryption and Decryption tables
      aes_enc[0][i] = (gmul(2, s) << 24) | (s << 16) | (s << 8) | gmul(3, s);
      aes_dec[0][s] = (gmul(14, i) << 24) | (gmul(9, i) << 16) | (gmul(13, i) << 8) | gmul(11, i);
      // Rotate tables
      for (var t = 1; t < 4; t++) {
        aes_enc[t][i] = (aes_enc[t - 1][i] >>> 8) | (aes_enc[t - 1][i] << 24);
        aes_dec[t][s] = (aes_dec[t - 1][s] >>> 8) | (aes_dec[t - 1][s] << 24);
      }
    }

    aes_init_done = true;
  }
```

En outre, nous savons que l'urne contenait des données chiffrées avec RSAES-PKCS1-v1_5.
Il se trouve que RSAES-PKCS1-v1_5 pas implémenté dans asmcrypto.js, par contre une Pull Request a été ouverte pour l'ajouter (https://github.com/asmcrypto/asmcrypto.js/pull/172).

Cette PR ajoute notamment une nouvelle fonction `getNonZeroRandomValues` (https://github.com/asmcrypto/asmcrypto.js/pull/172/files#diff-cc348d6afd005d15a5a7612748435053a28d5184067811f0f4d73461f57b8ea6R24-R36) faisant appel à une autre fonction `getRandomValues` déjà présente dans asmcrypto avant la PR:

```javascript
export function getRandomValues(buf: Uint32Array | Uint8Array): void {
  if (typeof process !== 'undefined') {
    const nodeCrypto = require('crypto');
    const bytes = nodeCrypto.randomBytes(buf.length);
    buf.set(bytes);
    return;
  }
  if (window.crypto && window.crypto.getRandomValues) {
    window.crypto.getRandomValues(buf);
    return;
  }
  if (self.crypto && self.crypto.getRandomValues) {
    self.crypto.getRandomValues(buf);
    return;
  }
  // @ts-ignore
  if (window.msCrypto && window.msCrypto.getRandomValues) {
    // @ts-ignore
    window.msCrypto.getRandomValues(buf);
    return;
  }
  throw new Error('No secure random number generator available.');
}

+ export function getNonZeroRandomValues(buf: Uint8Array) {
+   getRandomValues(buf);
+   for (let i = 0; i < buf.length; i++) {
+     let byte = buf[i];
+     while (!byte) {
+       const octet = new Uint8Array(1);
+       getRandomValues(octet);
+       byte = octet[0];
+     }
+     buf[i] = byte;
+   }
+ }
```

Le code minifé de néovote contient là encore un code très proche :

```javascript
var WWVLmLmg = function (WWVLmLmH) {
    if (window.crypto && window.crypto.getRandomValues) {
        window.crypto.getRandomValues(WWVLmLmH);
        return;
    }
    if (window.msCrypto && window.msCrypto.getRandomValues) {
        window.msCrypto.getRandomValues(WWVLmLmH);
        return;
    }
    throw new Error("No secure random number generator available.");
};
var WWVLmLVx = function (WWVLmLmH) {
    WWVLmLmg(WWVLmLmH);
    for (var $WWVLmVTm = 0; $WWVLmVTm < WWVLmLmH.length; $WWVLmVTm++) {
        var $WWVLmLVs = WWVLmLmH[$WWVLmVTm];
        while (!$WWVLmLVs) {
            var $WWVLmLVr = new Uint8Array(1);
            WWVLmLmg($WWVLmLVr);
            $WWVLmLVs = $WWVLmLVr[0];
        }
        WWVLmLmH[$WWVLmVTm] = $WWVLmLVs;
    }
};
```

### Étude du chiffrement du bulletin

La présence de cette version spécifique de la biblothéque asmcrypto.js laisse penser que le chiffrement RSAES-PKCS1-v1_5 du bulletin se fasse côté client.

Cette bibliothèque ne semble pas avoir reçu d'audit de sécurité, sa dernière version publiée remonte à 2018 et la pull request apportant le support de RSAES-PKCS1-v1_5 est en attente de revue depuis août 2019.

Il ne nous est pas possible d'établir avec certitude que c'est bien cette bibliothèque qui est utilisée pour le chiffrement du bulletin . Si tel était le cas, cela pourrait aller à l'encontre du [Vade-mecum de cryptographie de l'ANSSI](https://www.ssi.gouv.fr/uploads/2021/03/anssi-guide-selection_crypto-1.0.pdf) qui indique dans sa partie `2.2.5  Utiliser des bibliothèques éprouvées` :

> C’est pourquoi il est impératif de n’employer que des bibliothèques éprouvées bénéficiant d’un suivi de leur sécurité pour tout appel à  des mécanismes cryptographiques.

## VI - Le processus de vérification

Le script de vérification disponible sur [www.verifier-mon-vote.fr](https://www.verifier-mon-vote.fr/) réalise les opérations suivantes :

1) Téléchargement des archives d'urne et de clés venant du serveur de vote

| ![php_download_box.png](php_download_box.png) |
|:--:|
| Crédits: Neovote |

2) Vérification de la preuve de vote

- Les hashes sont extraits de la preuve de vote
- Les hashes contenus dans `extra_hashes.csv` sont éliminés
- On s'assure que les hashes restant sont présents dans les urnes
- On vérifie que les hashes ne sont pas disséminés entre les deux urnes (une preuve de vote ne devant faire référence qu'à un seul tour)

3) Recomptage des votes de l'urne

- Déchiffrement de tous les votes. C'est d'ailleurs cette opération qui rend le processus de vérification aussi lent et tend à faire crasher le serveur (RSA étant un algorithme gourmand en ressource et notre election nécessite de l'exécuter pour chacun de la 100aine de millers de bulletins).
- Comptages des votes et statistiques

4) Affichage du résultat ou bien d'une erreur

| ![gestion des erreurs du script PHP](php_error_handling.png) |
|:------------------------------------------------------------:|
| Crédits: Neovote                                             |

## VII - Altération de l'urne

Comme nous l'avons vu, l'urne peut sans problème être modifiée et rechiffrée pour produire une urne valide au sens du système de vérification. Cela nous permet différentes attaques...

### 1 - Inversion des candidats

Le fichier `object_names.csv` servant à faire la correspondance entre les bulletins et le candidat, il est trivial d'inverser les résultats en changeant à qui correspond quel identifiant :

```raw
"1M-9493O-5D-2B-1C-2T-8S-3L";"fr";"Sandrine ROUSSEAU"
"1M-9493O-5D-2B-1C-2T-8S-2L";"fr";"Yannick JADOT"
"VOTEBLANC";"fr";"Vote blanc"
```

De cette façon toutes les preuves de vote restent valides, et le résultat de l'élection a changé :

| ![resultats_modifies_swap_2eme_tour.png](resultats_modifies_swap_2eme_tour.png) |
|:--:|
| Crédits: Neovote |

Bien Évidemment cette attaque est assez naïve : il y a fort à parier que la correspondance identifiant technique/nom de candidat a été mis sous scellé avant l'élection. Toutefois elle illustre assez bien les limites de la vérification du vote par l'électeur.

### 2 - Bourrage d'urne

Une attaque plus subtile (quoi que...) consiste à rajouter des faux votes dans l'urne.

De cette façon toutes les preuves de vote existantes sont toujours valides, et nous avons encore une fois changé le résultat de l'élection.

| ![resultats_modifies_add_2eme_tour.png](resultats_modifies_add_2eme_tour.png) |
|:--:|
| Crédits: Neovote |

Toutefois ce coup-ci le nombre d'enveloppes de vote ne correspond pas à la liste d'émargement. Cette dernière n'étant pas publique un électeur peut se laisser berner, mais sa publication permettrait de lever le doute.

### 3 - Remplacement des votes

Une troisième attaque consiste à substituer des votes dans l'urne au profit d'un autre candidat.

De cette manière on conserve bien le bon nombre de votants. Toutefois une personne possédant une preuve de vote contenant un des votes remplacés sera en mesure de détecter la fraude en réalisant la vérification (en admettant qu'on lui fasse confiance, cf. partie III).

Mais c'est sans compter sur le fichier `extra_hashes.csv` ! En effet ce dernier permet de lister des hashes à ignorer, de fait il suffit de mettre les hashes des anciens votes dans ce fichier et le tour est joué :

| ![resultats_modifies_replace_2eme_tour.png](resultats_modifies_replace_2eme_tour.png) |
|:--:|
| Crédits: Neovote |

Bon nombre d'enveloppes, de votes blanc, de votes nuls, toutes les preuves de vote émises sont valides.

### 4 - Tester tout ça

Les archives modifiées sont consultables [depuis un repo github](https://github.com/touilleMan/neovote-primaire-ecolo/tree/master/altered).

Pour obtenir les copies d'écran précédentes, les archives ont été hébergées sur un serveur reproduisant l'API du serveur de vote.

Il est donc possible de réaliser la vérification des archives modifiées depuis le site officiel  [www.verifier-mon-vote.fr](https://www.verifier-mon-vote.fr/) en utilisant la configuration suivante :

| type de modification            | Adresse du serveur de vote                 | Mot de passe       |
|---------------------------------|--------------------------------------------|--------------------|
| Inversion des candidats         | primaire-altered-by-swap.touilleman.xyz    | `altered_by_swap_` |
| Bourrage d'urne                 | primaire-altered-by-add.touilleman.xyz     | `_altered_by_add_` |
| Remplacement des votes          | primaire-altered-by-replace.touilleman.xyz | `alteredBYreplace` |
| Archive original (non modifiée) | primaire.neovote.com                       | `biè2Rrwû_çb7TWQà` |

Vous pouvez utiliser votre propre preuve de vote (le script tournant sur [www.verifier-mon-vote.fr](https://www.verifier-mon-vote.fr/) ne la transmettra pas à notre serveur d'archives). À défaut vous pouvez utiliser la preuve de vote suivante :

```raw
v46Vy31AZeeR6jIvGrqV240VTNr7fYdedwW-QmBKk2dWX6PM-pyDmJdulynelEEzwVj7s0ydMEB5OJQJAd9XkG30xDiDkFb9r33sMZ6SxeP7QzZTF0268xfuhMgt761DzBZTXc4PxtuezxO0W4SRuHsEmdUuwQ-2kCTqU-6tyx0T8r8HcfiN9Tz84hbJ-mf9m_sXhNTqEbxnUD_kt9_NMpJA2UY88Pj4GRkbiW1xdudGRy9kr8ln7nh1er1cSyusP50BHqGivSKZCFR7GJWgmSsJgG6n-WwChJjl5dZzhzAw4yVYVvIS6Y9rH2ME_evgbNGoTTsV7PtMiV12F_syMKQxFbTxe1MGX14FrdSRBDW7mTLQTXR7u0ViGtrR9ZmSfcfZ3Be7UKHMHifY5MYEMZSmu3OQWVowJNu2goNtsXWmdwIhqDz-UzyEyBU9UczLKjeK2CdB8RCUB5R8NZwSakRR1E9OQtoCQhXsHcQBPptQbvEe6HSNNtuTGxZlj8YQozKz0liZdaL-sflCD7LUUg@@
```

Cette preuve du 2nd tour contient les hashes de trois votes ayant été remplacés (dans le cas de la modification "remplacement des votes")
et deux autres votes ayant été pris aléatoirement dans l'urne. Malgré les modifications de l'urne, le site de vérification considère la preuve toujours valide ;-)

*Néovote nous a souligné que les urnes modifiées n'impactent en aucun cas le site officiel [primaire.neovote.com](https://primaire.neovote.com) qui doit être considéré comme la seule source des données de références. Leur authenticité étant garantie par le scellement des serveurs, ainsi qu'un programme de transparence via leur partenaire ID FACTO.*

## VIII - Conclusion

Il convient de le souligner : en l'état **rien ne permet de penser que la primaire à été l'objet d'une fraude quelconque**.

Toutefois, en tant qu'électeur, le fonctionnement du système Neovote interroge :

- absence de documentation du fonctionnement du système accessible à l'électeur
- rapport d'audit de la solution déployée pour l'élection également inaccessible à l'électeur
- possibilité triviale d'altération des preuves de votes et de l'urne
- certains choix techniques semblant en contradiction des recommandations de l'ANSSI

Les tests que nous avons réalisés ont mis en évidence qu'une urne peut être altérée entre sa production et sa publication de manière à changer le résultat de l'élection sans compromettre la vérification de la moindre preuve de vote.

De même, en cas de vérification invalide d'une preuve de vote, il n'est pas possible pour l'électeur de savoir si c'est l'intégrité de la preuve de vote ou de l'urne qui doit être remise en question.

En somme la vérification par l'électeur de la présence de son vote implique nécessairement de faire confiance à Neovote, aux organisateurs de la primaire, ainsi qu'à l'huissier de justice.

Enfin il convient de rappeler l'importance de la transparence dans le processus démocratique : cette analyse n'a été rendu possible que grace à la mise à disposition du code de vérification de l'urne (conformément à la délibération CNIL n° 2019-053). À l'inverse sa non-disponibilité n'aurait que peu entravé un acteur hostile disposant de moyens à la hauteur de l'enjeu de cette élection (rappelons que les élections présidentielles de 2012 ont été remportées par le gagnant d'une primaire).

Plus généralement, concernant le vote électronique, nous pensons que la mise à disposition publique du code source, de la documentation des mécanismes cryptographiques ainsi que la mise en oeuvre du système doivent être considérées comme un absolu minimum (de la même façon qu'une élection physique a pour absolu pré-requis d'utiliser une boite transparente comme urne).

*Néovote nous a transmis les conclusions du rapport d'expertise indépendante de la Solution déployée pour la primaire, le système est considéré conforme au niveau 3  de la Délibération CNIL n° 2019-053 du 25 avril 2019 et offre, d'un point aussi bien technique qu'organisationnel, un niveau de sécurité à la hauteur d'une solution de vote par internet pour une élection de ce niveau de risque.*
