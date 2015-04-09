## Note

Le robot n'est pas prêt pour les démonstrations, il n'y a pas vraiment de sécurité qui va l'empecher de s'auto-detruire en cas de mauvaise manipulation...


## Démarrage

- Brancher le routeur WIFI
- Brancher le robot (12V).

## Connexion

- Se connecter au wifi du routeur
- Normalement, si tout va bien, on doit pouvoir ping le robot:
`ping robot-name.local`
- Si ça ping:
  - se connecter en SSH:
  - `ssh poppy@robot-name.local`
  - `password: odroid`

- Si ça ping pas ...
  - brancher un cable ethernet de la tête au routeur
  - retenter le ping et se connecter en SSH
  - checker ifconfig pour voir si wlan a une IP
    - si non: `sudo reboot`
    - si oui: debrancher l'ethernet et retenter sa chance.


## Play

Une fois connecté en SSH:

- lancer le racourci pour démarrer un ipython notebook:  `bash notebook-launcher`
- se connecter à la page `poppy-humanoid.local:8888`
- et paf tu as un notebook pour coder Poppy et il y a meme quelques trucs déjà prêts.


## Eteindre:

- se connecter en SSH
- `sudo halt`
- attendre un peu et débrancher le robot
