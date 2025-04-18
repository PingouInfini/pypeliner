import spacy
from spacy import displacy
from langdetect import detect

# Détection de la langue
texte = """En direct, guerre en Ukraine : Kiev d’accord pour un cessez-le-feu immédiat « de trente jours », la proposition sera soumise à la Russie, annoncent les Etats-Unis

A l’issue des discussions en Arabie saoudite, le président ukrainien Zelensky a dit que « l’Ukraine est prête pour la paix » et que Washington doit désormais « convaincre la Russie » d’accepter cette proposition. Les Etats-Unis ont également acté le retour de leur aide « en matière de sécurité » et de renseignements à Kiev.

22:32

Giorgia Meloni dit « soutenir pleinement les efforts des Etats-Unis pour parvenir à une paix juste »

La présidente du conseil d’Italie, Giorgia Meloni, « accueille avec satisfaction » l’issue des négociations entre les Etats-Unis et l’Ukraine, qui ont abouti à une proposition d’un cessez-le-feu et à la reprise de l’assistance militaire américaine à Kiev, ont annoncé ses services, mardi.

« L’Italie soutient pleinement les efforts des Etats-Unis, sous la direction du président [Donald] Trump, pour parvenir à une paix juste garantissant la sécurité à long terme de l’Ukraine. La décision appartient désormais à la Russie », a déclaré Mme Meloni, dans un communiqué.

22:02

La Russie « n’exclut pas des contacts » avec les Etats-Unis dans « les prochains jours »
La porte-parole de la diplomatie russe, Maria Zakharova, à Moscou, le 11 mars 2025.
La porte-parole de la diplomatie russe, Maria Zakharova, à Moscou, le 11 mars 2025. MAXIM SHEMETOV/AFP

La porte-parole de la diplomatie russe a dit, mardi, envisager des contacts entre Moscou et Washington dans les prochains jours, après que l’Ukraine a annoncé soutenir une proposition américaine de cessez-le-feu de trente jours avec la Russie.

« Nous n’excluons pas des contacts avec des représentants des Etats-Unis pendant les prochains jours », a déclaré Maria Zakharova, citée par les agences russes TASS et RIA Novosti. Le président américain, Donald Trump, a, de son côté, dit mardi qu’il « [allait] parler à Vladimir Poutine », sans doute cette semaine.

21:00 L’essentiel

Le point sur la situation, mardi 11 mars, à 21 heures

A l’issue des discussions à Djedda, l’Ukraine a accepté une proposition américaine de cessez-le-feu immédiat de trente jours qui sera soumise à la Russie « dans les prochains jours ». Washington annonce lever ses restrictions sur l’aide militaire et l’échange de renseignements. La question de l’accord sur les minerais sera réglée par les présidents Volodymyr Zelensky et Donald Trump.
A l’issue des discussions en Arabie saoudite, le président ukrainien a publié un message sur les réseaux sociaux affirmant que les Etats-Unis « compren[aient] les arguments » de l’Ukraine et devaient « convaincre » la Russie d’accepter un cessez-le-feu. Selon des propos relayés par un journaliste accrédité auprès de la présidence russe, Vladimir Poutine a insisté « de nouveau sur le fait que l’objectif ne devrait pas être d’atteindre une trêve courte, (…) mais une paix de long terme basée sur le respect des intérêts légitimes de tout le peuple, de toutes les nations vivant dans cette région ».
Emmanuel Macron a appelé mardi les chefs militaires d’une trentaine de pays réunis à Paris à commencer à élaborer « un plan pour définir des garanties de sécurité crédibles » pour l’Ukraine en cas d’accord de paix avec la Russie, a fait savoir l’Elysée. Plus tôt dans la journée, il a estimé que la France devait lutter « en même temps » contre « les menaces géopolitiques » et « terroristes ».
Saisir les avoirs russes gelés pour financer la défense de l’Ukraine pourrait menacer la stabilité financière de l’Europe, a jugé Eric Lombard, le ministre des finances français, à l’issue d’une réunion à Bruxelles avec ses homologues de l’Union européenne.
Peter Szijjarto, le ministre des affaires étrangères hongrois, a annoncé que des infrastructures de l’oléoduc Droujba, qui relie la Russie à l’Europe centrale et orientale, ont été touchées par l’attaque de drones ukrainiens dans la nuit du 10 au 11 mars.
Se sentant menacée par son voisin russe, la Pologne veut former militairement jusqu’à 100 000 volontaires par an, a annoncé Donald Tusk, le premier ministre.
La Suède est plus exposée à la Russie depuis son adhésion à l’OTAN a affirmé, mardi lors d’un point presse, Fredrik Hallström, chef des opérations au service de la sûreté de l’Etat (Säpo) suédois.

20:57

Donald Trump envisage de parler à Vladimir Poutine rapidement, et n’exclut pas d’inviter de nouveau Volodymyr Zelensky à la Maison Blanche

Donald Trump a dit mardi qu’il « allait parler à Vladimir Poutine », sans doute cette semaine, après que l’Ukraine a annoncé soutenir une proposition américaine de cessez-le-feu de trente jours avec la Russie.

« Je pense, oui », a ajouté le président américain lorsqu’une journaliste l’a interrogé pour savoir si la conversation avec son homologue russe aurait lieu dans la semaine, avant de répondre « bien sûr » à un reporter qui lui demandait si le président ukrainien, Volodymyr Zelensky, serait invité à revenir à la Maison Blanche après une première rencontre extrêmement conflictuelle.

20:50

Des dirigeants européens saluent une « évolution positive » et une « avancée remarquable » dans les négociations de paix en Ukraine

Les deux plus hauts responsables de l’Union européenne ont salué à leur tour l’accord entre les Etats-Unis et l’Ukraine sur un projet de cessez-le-feu, ainsi que la décision de Washington de reprendre l’aide militaire à Kiev.

« Il s’agit d’une évolution positive qui peut constituer un pas vers une paix globale, juste et durable pour l’Ukraine. La balle est désormais dans le camp de la Russie », ont écrit la présidente de la Commission européenne, Ursula von der Leyen, et le président du Conseil européen, Antonio Costa, sur X.

Le premier ministre britannique, Keir Starmer, a également salué une « avancée remarquable » dans les négociations de paix en Ukraine."""

# Détecter la langue
langue = detect(texte)
print(f"Langue détectée : {langue}")

# Charger le modèle en fonction de la langue détectée
if langue == "fr":
    nlp = spacy.load("fr_core_news_md")
elif langue == "en":
    nlp = spacy.load("en_core_web_sm")
else:
    raise ValueError("Langue non prise en charge : uniquement le français (fr) et l'anglais (en)")

# Traiter le texte avec le modèle
texte = texte.replace('\n', " <br> ")
doc = nlp(texte)

# Générer le rendu HTML avec displacy
html_output = displacy.render(doc, style="ent")

# Sauvegarder le rendu HTML dans un fichier
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_output.replace("&lt;br&gt;", "<br>"))

# Extraire et afficher les entités nommées
for ent in doc.ents:
    print(ent.text, ent.label_)
