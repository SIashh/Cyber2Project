from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=30)
    team = models.CharField(max_length=30)

    def __str__(self):
        return "Tool: {} ({})".format(self.name, self.team)


class BlueNote(models.Model):
    # Metadata
    customer_id = models.IntegerField()
    tool_id = models.IntegerField()

    # Criteria notes
    detection = models.IntegerField()
    capacite_d_analyse = models.IntegerField()
    complexite_d_analyse = models.IntegerField()
    export_des_resultats = models.IntegerField()
    creation_de_regles = models.IntegerField()
    export_de_fichier_suspect = models.IntegerField()
    prevention = models.IntegerField()

    def __str__(self):
        return "BlueNote: {} ({})".format(self.customer_id, self.tool_id)


class BlueWeight(models.Model):
    # Metadata
    customer_id = models.IntegerField()
    tool_id = models.IntegerField()

    # Criteria weights
    detection = models.IntegerField()
    capacite_d_analyse = models.IntegerField()
    complexite_d_analyse = models.IntegerField()
    export_des_resultats = models.IntegerField()
    creation_de_regles = models.IntegerField()
    export_de_fichier_suspect = models.IntegerField()
    prevention = models.IntegerField()

    def __str__(self):
        return "BlueWeight: {} ({})".format(self.customer_id, self.tool_id)


class RedNote(models.Model):
    # Metadata
    customer_id = models.IntegerField()
    tool_id = models.IntegerField()

    # Criteria notes
    mise_a_jour = models.IntegerField()
    capacite_de_detection = models.IntegerField()
    configuration = models.IntegerField()
    rapidite_d_execution = models.IntegerField()
    comsommation_de_ressources = models.IntegerField()
    explication_de_vulnerabilite = models.IntegerField()
    documentation = models.IntegerField()
    scope_de_scan = models.IntegerField()
    flexibilite = models.IntegerField()
    communaute = models.IntegerField()
    compatibilite_avec_outis_externes = models.IntegerField()

    def __str__(self):
        return "RedNote: {} ({})".format(self.customer_id, self.tool_id)


class RedWeight(models.Model):
    # Metadata
    customer_id = models.IntegerField()
    tool_id = models.IntegerField()

    # Criteria weights
    mise_a_jour = models.IntegerField()
    capacite_de_detection = models.IntegerField()
    configuration = models.IntegerField()
    rapidite_d_execution = models.IntegerField()
    comsommation_de_ressources = models.IntegerField()
    explication_de_vulnerabilite = models.IntegerField()
    documentation = models.IntegerField()
    scope_de_scan = models.IntegerField()
    flexibilite = models.IntegerField()
    communaute = models.IntegerField()
    compatibilite_avec_outis_externes = models.IntegerField()

    def __str__(self):
        return "RedWeight: {} ({})".format(self.customer_id, self.tool_id)
