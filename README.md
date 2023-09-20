# SSH keys
Op de host server zijn SSH keys aangemaakt. De public key is in GitHub opgenomen als "Deploy Key" zodat de host toegang krijgt tot de GitHub repository. Daarnaast is deze toegevoegd aan de "authorized_keys" op de host. Samen met de private key (die t.b.v. de veiligheid als Git secret van de repository is opgeslagen) zorgt dit ervoor dat de Workflow zonder password op de host kan inloggen.

# Niet functionerende website voorkomen
Het eerste deel van de workflow (job run-tests) is ingericht om middels pytest (via module test_main.py) de code eerst te testen of alle apps status 200 geven en de redirection van de "home" button werkt.
Probleem: foutmeldingen m.b.t. Flask. Opgelost door 2 steps toe te voegen: virtual environment creëren en activeren en Flask installeren.

Vervolgens zorgt de step "needs test" in de job "deploy" dat de code alleen wordt doorgezet vanuit de repository naar de host indien de step "Run tests" van job "run-tests" is geslaagd.

# Contact maken met host en content overzetten
Middels de (tijdelijke) installatie van de SSH private key kan zonder wachtwoord worden ingelogd op de host.
In een shell script o.b.v. Bash (deploy.sh) zijn de op de host uit te voeren commands opgenomen.
Probleem: Git secrets beschikbaar maken in het shell script. Opgelost door ze als environment variable op te nemen in de step die het script aanroept.
Probleem: commands werden niet herkend en niet uitgevoerd. Het voorbeeld in de Winc lesomgeving is wat misleidend: het lijkt alsof de commands op aparte regels kunnen worden opgenomen, maar dat is niet zo. Opgelost door alle commands na de ssh command op te nemen in een string waarbij de commands van elkaar worden gescheiden met een ";".
