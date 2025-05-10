# Mon ia gere le calcule de moyenne et aussi un asistance vocale en apprentissage
## Commande git utilise
### Pour voir toutes les cle ssh
```bash
ls -al ~/.ssh
```
### Pour creer un nouvelle cle ssh
```bash
ssh-keygen -t ed25519 -C "sergeduvalsopnghontamia@gmail.com"
```
### Pour lancer a l'agent ssh
```bash
eval "$(ssh-agent -s)"
```
### Ajouter la cle ssh a l'agent
```bash
ssh-add ~/.ssh/id_ed25519
```
### Voir la cle
```bash
cat ~/.ssh/id_ed25519.pub
```
### Pour verifier la connexion
```bash
ssh -T git@github.com
```
### pour pousser ton code vers github
```bash
git push origin main
```
## Bibliotheque python a telecharge
```python
    from tkinter import simpledialog
    import tkinter as tk
    import speech_recognition as sr
    import pyttsx3
    import json
    import os
```
## Pour installer les bibliotheque python utiliser
```bash
pip install Nom_de la bibliotheque
```
## pour le stockage des infos conne par mon ia j'ai utiliser le JSON voici un exemple

```json
{
    "bonjour": "Bonjour cher monsieur",
    "salut": "salut \u00e0 toi",
    "hello": "hello l'ami",
    "yo": "yo !",
    "hey": "hey, comment vas-tu ?",
    "coucou": "Yo mon type",
    "rebonjour": "rebonjour \u00e0 toi"
}
```
