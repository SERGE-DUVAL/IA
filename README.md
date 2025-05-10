# Mon ia gere le calcule de moyenne et aussi un asistance vocale en apprentissage
## commande git utilise
### pour voir toutes les cle ssh
```bash
ls -al ~/.ssh
```
### pour creer un nouvelle cle ssh
```bash
ssh-keygen -t ed25519 -C "sergeduvalsopnghontamia@gmail.com"
```
### pour lancer a l'agent ssh
```bash
eval "$(ssh-agent -s)"
```
### ajouter la cle ssh a l'agent
```bash
ssh-add ~/.ssh/id_ed25519
```
### voir la cle
```bash
cat ~/.ssh/id_ed25519.pub
```
### pour verifier la connexion
```bash
ssh -T git@github.com
```
### pour pousser ton code vers github
```bash
git push origin main
```
## bibliotheque python a ajouter
```python
    import tkinter import simpledialog
    import tkinter as tk
    import speech_recognition as sr
    import pyttsx3
    import json
    import os
```